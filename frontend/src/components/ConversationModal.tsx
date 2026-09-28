import React, { useState, useEffect, useRef } from 'react';
import {
  X,
  Send,
  Volume2,
  Sparkles,
  Bot,
  User,
  AlertTriangle,
  CheckCircle2,
  Lightbulb,
  ArrowLeft,
  MessageSquare,
  PlusCircle,
  Loader2,
  Languages,
} from 'lucide-react';
import type {
  DialogueScenarioSummary,
  DialogueTurnMessage,
} from '../types';
import { api } from '../services/api';
import { soundEffects, speakText } from '../services/audio';

interface ConversationModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialLanguage?: string;
}

export const ConversationModal: React.FC<ConversationModalProps> = ({
  isOpen,
  onClose,
  initialLanguage = 'sv',
}) => {
  const [selectedLanguage, setSelectedLanguage] = useState<string>(initialLanguage);
  const [scenarios, setScenarios] = useState<DialogueScenarioSummary[]>([]);
  const [loadingScenarios, setLoadingScenarios] = useState(false);

  // Active dialogue state
  const [activeScenario, setActiveScenario] = useState<DialogueScenarioSummary | null>(null);
  const [customTopic, setCustomTopic] = useState('');
  const [isStartingDialogue, setIsStartingDialogue] = useState(false);
  const [isSendingTurn, setIsSendingTurn] = useState(false);

  const [messages, setMessages] = useState<DialogueTurnMessage[]>([]);
  const [suggestedChips, setSuggestedChips] = useState<string[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const [showTranslations, setShowTranslations] = useState<Record<number, boolean>>({});

  const chatEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Load available scenarios when modal opens or language changes
  useEffect(() => {
    if (!isOpen) return;

    const fetchScenarios = async () => {
      try {
        setLoadingScenarios(true);
        const data = await api.getDialogueScenarios(selectedLanguage);
        setScenarios(data);
      } catch (err) {
        console.error('Failed to load dialogue scenarios:', err);
      } finally {
        setLoadingScenarios(false);
      }
    };

    fetchScenarios();
  }, [isOpen, selectedLanguage]);

  // Scroll to bottom when messages update
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isSendingTurn]);

  if (!isOpen) return null;

  const handleStartScenario = async (scenario: DialogueScenarioSummary) => {
    try {
      soundEffects.playClickSound();
      setIsStartingDialogue(true);
      setActiveScenario(scenario);
      setMessages([]);
      setSuggestedChips([]);

      const response = await api.startDialogueScenario(scenario.id, selectedLanguage);
      const initialTurn: DialogueTurnMessage = {
        ...response.initial_message,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages([initialTurn]);
      setSuggestedChips(response.suggested_starter_chips || []);

      // Speak opening AI phrase
      if (initialTurn.text) {
        speakText(initialTurn.text, selectedLanguage);
      }
    } catch (err) {
      console.error('Failed to start scenario:', err);
    } finally {
      setIsStartingDialogue(false);
      setTimeout(() => inputRef.current?.focus(), 150);
    }
  };

  const handleStartCustomScenario = async () => {
    if (!customTopic.trim()) return;
    try {
      soundEffects.playClickSound();
      setIsStartingDialogue(true);

      const customScenarioObj: DialogueScenarioSummary = {
        id: 'custom-user-topic',
        language: selectedLanguage,
        title: customTopic.trim(),
        swedish_title: customTopic.trim(),
        description: `Custom interactive roleplay on: "${customTopic.trim()}"`,
        persona: 'Conversation Partner',
        avatar: '🎭',
        level: 'A2-B2',
        tags: ['Custom', 'Free Conversation'],
        initial_prompt: selectedLanguage === 'sv' ? `Hej! Låt oss prata om: ${customTopic}. Vad tycker du?` : `Hello! Let's talk about: ${customTopic}. What do you think?`,
        suggested_starter_chips: selectedLanguage === 'sv' ? ['Det låter spännande!', 'Berätta mer.', 'Vad tycker du själv?'] : ['Sounds exciting!', 'Tell me more.', 'What do you think?'],
      };

      setActiveScenario(customScenarioObj);
      setMessages([]);
      setSuggestedChips([]);

      const response = await api.startDialogueScenario('custom', selectedLanguage, customTopic.trim());
      const initialTurn: DialogueTurnMessage = {
        ...response.initial_message,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages([initialTurn]);
      setSuggestedChips(response.suggested_starter_chips || []);

      if (initialTurn.text) {
        speakText(initialTurn.text, selectedLanguage);
      }
    } catch (err) {
      console.error('Failed to start custom dialogue:', err);
    } finally {
      setIsStartingDialogue(false);
      setCustomTopic('');
      setTimeout(() => inputRef.current?.focus(), 150);
    }
  };

  const handleSendMessage = async (textToSend?: string) => {
    const message = (textToSend || inputMessage).trim();
    if (!message || !activeScenario || isSendingTurn) return;

    soundEffects.playClickSound();
    setInputMessage('');

    const userTurn: DialogueTurnMessage = {
      sender: 'User',
      text: message,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    const newHistory = [...messages, userTurn];
    setMessages(newHistory);
    setIsSendingTurn(true);
    setSuggestedChips([]);

    try {
      const response = await api.sendDialogueTurn(
        activeScenario.id,
        selectedLanguage,
        message,
        newHistory
      );

      // Attach any correction feedback to the user's turn
      if (response.correction_feedback && response.correction_feedback.has_errors) {
        soundEffects.playIncorrectSound();
        userTurn.correction_feedback = response.correction_feedback;
      } else {
        soundEffects.playCorrectSound();
      }

      const aiTurn: DialogueTurnMessage = {
        ...response.ai_reply,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setMessages([...newHistory, aiTurn]);
      setSuggestedChips(response.suggested_next_chips || []);

      // Auto-pronounce AI response
      if (aiTurn.text) {
        speakText(aiTurn.text, selectedLanguage);
      }
    } catch (err) {
      console.error('Failed to send turn:', err);
    } finally {
      setIsSendingTurn(false);
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  };

  const toggleTranslation = (index: number) => {
    setShowTranslations((prev) => ({ ...prev, [index]: !prev[index] }));
  };

  const handleResetToScenarios = () => {
    soundEffects.playClickSound();
    setActiveScenario(null);
    setMessages([]);
    setSuggestedChips([]);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden">
        
        {/* Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-900/90 backdrop-blur">
          <div className="flex items-center gap-3">
            {activeScenario ? (
              <button
                onClick={handleResetToScenarios}
                className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition"
                title="Back to Scenario Selection"
              >
                <ArrowLeft className="w-5 h-5" />
              </button>
            ) : null}

            <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-xl shadow-lg shadow-indigo-500/20">
              {activeScenario ? activeScenario.avatar : '🎭'}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black text-white">
                  {activeScenario ? activeScenario.title : 'Conversational AI Dialogue Simulator'}
                </h2>
                {activeScenario && (
                  <span className="px-2 py-0.5 text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 rounded-full">
                    {activeScenario.persona}
                  </span>
                )}
              </div>
              <p className="text-xs text-slate-400">
                {activeScenario
                  ? `Interactive roleplay with real-time grammar feedback`
                  : `Choose a real-world scenario or create your own topic`}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Selector */}
            {!activeScenario && (
              <div className="flex items-center bg-slate-800 border border-slate-700 rounded-xl p-1">
                <button
                  onClick={() => {
                    soundEffects.playClickSound();
                    setSelectedLanguage('sv');
                  }}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition ${
                    selectedLanguage === 'sv'
                      ? 'bg-emerald-600 text-white shadow'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  <span>🇸🇪</span> Svenska
                </button>
                <button
                  onClick={() => {
                    soundEffects.playClickSound();
                    setSelectedLanguage('en');
                  }}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition ${
                    selectedLanguage === 'en'
                      ? 'bg-emerald-600 text-white shadow'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  <span>🇬🇧</span> English
                </button>
              </div>
            )}

            <button
              onClick={() => {
                soundEffects.playClickSound();
                onClose();
              }}
              className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-xl transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Modal Body */}
        {!activeScenario ? (
          /* =========================================================================
             1. SCENARIO SELECTION VIEW
             ========================================================================= */
          <div className="p-6 overflow-y-auto max-h-[calc(92vh-90px)] space-y-6">
            
            {/* Custom Topic Generator Card */}
            <div className="bg-gradient-to-r from-indigo-950/60 via-purple-950/40 to-slate-900 border border-indigo-500/30 rounded-2xl p-5 shadow-lg">
              <div className="flex items-center gap-2 mb-2">
                <Sparkles className="w-5 h-5 text-indigo-400 animate-pulse" />
                <h3 className="text-base font-black text-white">Create Custom Scenario</h3>
                <span className="text-xs bg-indigo-500/20 text-indigo-300 font-bold px-2 py-0.5 rounded-full border border-indigo-500/30">
                  AI Dynamic
                </span>
              </div>
              <p className="text-xs text-slate-300 mb-3">
                Type any situation, role, or conversation topic you want to simulate (e.g., &quot;Ordering at a Stockholm bakery&quot; or &quot;Tech job interview in London&quot;).
              </p>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={customTopic}
                  onChange={(e) => setCustomTopic(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleStartCustomScenario()}
                  placeholder={
                    selectedLanguage === 'sv'
                      ? 'T.ex. Beställa mat på restaurang eller fråga om vägen i Stockholm...'
                      : 'E.g., Negotiating rent with a landlord or checking into a hotel...'
                  }
                  className="flex-1 bg-slate-900/90 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                />
                <button
                  onClick={handleStartCustomScenario}
                  disabled={!customTopic.trim() || isStartingDialogue}
                  className="btn-3d px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white font-bold rounded-xl text-sm shadow-[0_3px_0_#3730a3] flex items-center gap-2"
                >
                  <PlusCircle className="w-4 h-4" />
                  <span>Start Roleplay</span>
                </button>
              </div>
            </div>

            {/* Predefined Scenarios List */}
            <div>
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                  <MessageSquare className="w-5 h-5 text-emerald-400" />
                  <h3 className="text-base font-black text-white">Choose a Roleplay Scenario</h3>
                </div>
                <span className="text-xs text-slate-400 font-medium">
                  {scenarios.length} situations available
                </span>
              </div>

              {loadingScenarios ? (
                <div className="flex items-center justify-center py-12 text-slate-400 gap-3">
                  <Loader2 className="w-6 h-6 animate-spin text-emerald-400" />
                  <span>Loading scenarios...</span>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {scenarios.map((scenario) => (
                    <div
                      key={scenario.id}
                      onClick={() => handleStartScenario(scenario)}
                      className="group bg-slate-800/60 hover:bg-slate-800 border border-slate-700/80 hover:border-emerald-500/50 rounded-2xl p-5 cursor-pointer transition-all duration-200 hover:shadow-xl hover:shadow-emerald-950/20 flex flex-col justify-between"
                    >
                      <div>
                        <div className="flex items-start justify-between gap-3 mb-2">
                          <div className="flex items-center gap-3">
                            <span className="text-3xl p-2 bg-slate-900/80 rounded-xl border border-slate-700 group-hover:scale-110 transition-transform">
                              {scenario.avatar}
                            </span>
                            <div>
                              <h4 className="font-bold text-white text-base group-hover:text-emerald-300 transition">
                                {scenario.title}
                              </h4>
                              {scenario.swedish_title && scenario.swedish_title !== scenario.title && (
                                <p className="text-xs text-emerald-400/80 font-medium">
                                  {scenario.swedish_title}
                                </p>
                              )}
                            </div>
                          </div>
                          <span className="text-xs font-black px-2.5 py-1 bg-slate-900 border border-slate-700 text-slate-300 rounded-lg">
                            {scenario.level}
                          </span>
                        </div>

                        <p className="text-xs text-slate-300 line-clamp-2 my-2.5">
                          {scenario.description}
                        </p>

                        <div className="flex items-center gap-2 text-xs text-slate-400 my-2">
                          <Bot className="w-3.5 h-3.5 text-indigo-400" />
                          <span>Persona: <strong className="text-slate-200">{scenario.persona}</strong></span>
                        </div>
                      </div>

                      <div className="flex items-center justify-between pt-3 border-t border-slate-700/50 mt-2">
                        <div className="flex flex-wrap gap-1.5">
                          {scenario.tags.slice(0, 2).map((tag, idx) => (
                            <span
                              key={idx}
                              className="text-[10px] px-2 py-0.5 bg-slate-900/60 text-slate-400 border border-slate-700/40 rounded-md"
                            >
                              #{tag}
                            </span>
                          ))}
                        </div>

                        <button className="btn-3d text-xs font-black px-3.5 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl shadow-[0_2px_0_#065f46]">
                          Start Chat →
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        ) : (
          /* =========================================================================
             2. ACTIVE INTERACTIVE CONVERSATION VIEW
             ========================================================================= */
          <div className="flex flex-col flex-1 h-[calc(92vh-90px)]">
            
            {/* Persona Info Ribbon */}
            <div className="bg-slate-800/60 border-b border-slate-800 px-6 py-2.5 flex items-center justify-between">
              <div className="flex items-center gap-2 text-xs text-slate-300">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                <span>Active Roleplay:</span>
                <strong className="text-white">{activeScenario.title}</strong>
                <span className="text-slate-500">•</span>
                <span>AI Partner: <strong className="text-indigo-300">{activeScenario.persona}</strong></span>
              </div>

              <div className="flex items-center gap-2">
                <button
                  onClick={handleResetToScenarios}
                  className="text-xs text-slate-400 hover:text-slate-200 font-bold px-2 py-1 rounded hover:bg-slate-700 transition"
                >
                  Change Scenario
                </button>
              </div>
            </div>

            {/* Chat Timeline */}
            <div className="flex-1 p-6 overflow-y-auto space-y-4">
              {messages.map((turn, index) => {
                const isAi = turn.sender === 'AI';
                return (
                  <div
                    key={index}
                    className={`flex flex-col ${isAi ? 'items-start' : 'items-end'} space-y-1.5`}
                  >
                    <div className="flex items-end gap-2 max-w-[85%]">
                      {isAi && (
                        <div className="w-8 h-8 rounded-full bg-indigo-600 flex items-center justify-center text-sm flex-shrink-0 shadow-md">
                          {activeScenario.avatar || '🤖'}
                        </div>
                      )}

                      <div
                        className={`rounded-2xl px-4 py-3 shadow-md ${
                          isAi
                            ? 'bg-slate-800 border border-slate-700 text-slate-100 rounded-bl-sm'
                            : 'bg-emerald-600 text-white rounded-br-sm'
                        }`}
                      >
                        <div className="flex items-start justify-between gap-4">
                          <p className="text-sm font-medium leading-relaxed">{turn.text}</p>
                          
                          {/* Speak & Translate buttons for AI turns */}
                          {isAi && (
                            <div className="flex items-center gap-1.5 flex-shrink-0">
                              <button
                                onClick={() => speakText(turn.text, selectedLanguage)}
                                title="Listen to pronunciation"
                                className="p-1 text-slate-400 hover:text-white transition rounded"
                              >
                                <Volume2 className="w-4 h-4" />
                              </button>
                              {turn.translation && (
                                <button
                                  onClick={() => toggleTranslation(index)}
                                  title="Toggle English Translation"
                                  className={`p-1 transition rounded text-xs ${
                                    showTranslations[index] ? 'text-emerald-400' : 'text-slate-400 hover:text-white'
                                  }`}
                                >
                                  <Languages className="w-4 h-4" />
                                </button>
                              )}
                            </div>
                          )}
                        </div>

                        {/* Translation Accordion */}
                        {isAi && turn.translation && showTranslations[index] && (
                          <div className="mt-2 pt-2 border-t border-slate-700/60 text-xs text-slate-300 italic">
                            🇬🇧 {turn.translation}
                          </div>
                        )}
                      </div>

                      {!isAi && (
                        <div className="w-8 h-8 rounded-full bg-emerald-700 flex items-center justify-center text-white text-xs font-bold flex-shrink-0 shadow-md">
                          <User className="w-4 h-4" />
                        </div>
                      )}
                    </div>

                    {/* ✨ Embedded Real-Time Grammar Correction Card (When user made a mistake) */}
                    {!isAi && turn.correction_feedback && turn.correction_feedback.has_errors && (
                      <div className="max-w-[85%] mr-10 bg-rose-950/40 border border-rose-500/40 rounded-2xl p-4 shadow-lg animate-fade-in space-y-2">
                        <div className="flex items-center gap-2 text-rose-400 font-bold text-xs">
                          <AlertTriangle className="w-4 h-4" />
                          <span>Grammar Insight & Correction</span>
                        </div>

                        {/* Highlighted Issues */}
                        {turn.correction_feedback.highlighted_issues && turn.correction_feedback.highlighted_issues.length > 0 && (
                          <div className="flex flex-wrap gap-1">
                            {turn.correction_feedback.highlighted_issues.map((issue, i) => (
                              <span
                                key={i}
                                className="text-[10px] font-bold px-2 py-0.5 bg-rose-500/20 text-rose-300 border border-rose-500/30 rounded"
                              >
                                {issue}
                              </span>
                            ))}
                          </div>
                        )}

                        {/* Corrected Text */}
                        {turn.correction_feedback.corrected_text && (
                          <div className="bg-slate-900/80 rounded-xl p-2.5 border border-slate-800 text-xs flex items-start gap-2">
                            <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                            <div>
                              <span className="text-slate-400 text-[11px] block">Correct phrasing:</span>
                              <strong className="text-emerald-300 text-sm">
                                {turn.correction_feedback.corrected_text}
                              </strong>
                            </div>
                          </div>
                        )}

                        {/* Pedagogical Rule Explanation */}
                        {turn.correction_feedback.grammar_rule_explanation && (
                          <div className="text-xs text-slate-300 flex items-start gap-2 bg-slate-900/50 p-2.5 rounded-xl border border-slate-800/80">
                            <Lightbulb className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                            <div>
                              <span className="text-amber-300 font-semibold text-[11px] block">Grammar Rule:</span>
                              <p className="text-slate-300 leading-snug">
                                {turn.correction_feedback.grammar_rule_explanation}
                              </p>
                            </div>
                          </div>
                        )}

                        {/* Native Alternative Phrasing */}
                        {turn.correction_feedback.improved_native_alternative && (
                          <div className="text-xs text-slate-400 italic">
                            💡 Native alternative: &quot;{turn.correction_feedback.improved_native_alternative}&quot;
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}

              {isSendingTurn && (
                <div className="flex items-center gap-3 text-slate-400 text-xs py-2 animate-pulse">
                  <div className="w-7 h-7 rounded-full bg-indigo-600 flex items-center justify-center text-xs">
                    {activeScenario.avatar || '🤖'}
                  </div>
                  <span>{activeScenario.persona} is typing and analyzing grammar...</span>
                </div>
              )}

              <div ref={chatEndRef} />
            </div>

            {/* Quick Suggestion Chips */}
            {suggestedChips && suggestedChips.length > 0 && !isSendingTurn && (
              <div className="px-6 py-2 bg-slate-900/90 border-t border-slate-800/80 flex items-center gap-2 overflow-x-auto">
                <span className="text-[11px] font-bold text-slate-400 uppercase flex-shrink-0">
                  Quick Replies:
                </span>
                <div className="flex items-center gap-2 flex-wrap">
                  {suggestedChips.map((chip, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleSendMessage(chip)}
                      className="text-xs font-semibold px-3 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-emerald-500/30 hover:border-emerald-400 rounded-full transition whitespace-nowrap shadow-sm"
                    >
                      {chip}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Input Bar */}
            <div className="p-4 bg-slate-900 border-t border-slate-800 flex items-center gap-3">
              <input
                ref={inputRef}
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}
                placeholder={
                  selectedLanguage === 'sv'
                    ? 'Skriv ditt svar på svenska (eller välj ett snabbsvar ovan)...'
                    : 'Type your message in English...'
                }
                disabled={isSendingTurn}
                className="flex-1 bg-slate-800/90 border border-slate-700 rounded-2xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 disabled:opacity-50"
              />

              <button
                onClick={() => handleSendMessage()}
                disabled={!inputMessage.trim() || isSendingTurn}
                className="btn-3d p-3 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white rounded-2xl shadow-[0_3px_0_#065f46] transition flex items-center justify-center"
                title="Send message"
              >
                <Send className="w-5 h-5" />
              </button>
            </div>

          </div>
        )}

      </div>
    </div>
  );
};
