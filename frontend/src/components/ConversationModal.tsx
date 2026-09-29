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
  PlusCircle,
  Loader2,
  Languages,
  BookOpen,
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
      setSuggestedChips(response.suggested_chips || []);

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
        level: 'A2-B2',
        category: 'Eget ämne',
        persona_name: 'Samtalspartner',
        avatar_emoji: '🎭',
        scenario_context: `Eget interaktivt samtal om: "${customTopic.trim()}"`,
        suggested_chips: selectedLanguage === 'sv' ? ['Det låter spännande!', 'Berätta mer.', 'Vad tycker du själv?'] : ['Sounds exciting!', 'Tell me more.', 'What do you think?'],
        target_grammar: 'Fritt samtal och naturlig dialog',
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
      setSuggestedChips(response.suggested_chips || []);

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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-stone-900/60 backdrop-blur-sm animate-fade-in font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-[0_16px_48px_rgba(45,35,25,0.15)] overflow-hidden">
        
        {/* Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-[#E5DDD0] bg-[#FFFFFF]">
          <div className="flex items-center gap-3">
            {activeScenario ? (
              <button
                onClick={handleResetToScenarios}
                className="p-2 text-[#8F877B] hover:text-[#24221F] hover:bg-[#F5EFEB] rounded-xl transition"
                title="Tillbaka till scenarier"
              >
                <ArrowLeft className="w-5 h-5" />
              </button>
            ) : null}

            <div className="w-10 h-10 rounded-2xl bg-[#2B5876] text-white flex items-center justify-center text-xl shadow-[0_2px_0_#1A374A] border border-[#1A374A]">
              {activeScenario ? activeScenario.avatar_emoji : '🎭'}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-bold font-display text-[#24221F]">
                  {activeScenario ? activeScenario.title : 'Samtalslabb & Dialogsimulator'}
                </h2>
                {activeScenario && (
                  <span className="px-2 py-0.5 text-[11px] font-mono-tag bg-[#EEF5F9] text-[#2B5876] border border-[#D5E5EE] rounded-md">
                    {activeScenario.persona_name}
                  </span>
                )}
              </div>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                {activeScenario
                  ? `Interaktivt rollspel med direkt grammatikinsikt`
                  : `Välj ett vardagsscenario eller skapa ett eget samtalsämne`}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Selector */}
            {!activeScenario && (
              <div className="flex items-center bg-[#F5EFEB] border border-[#DDD4C6] rounded-xl p-1">
                <button
                  onClick={() => {
                    soundEffects.playClickSound();
                    setSelectedLanguage('sv');
                  }}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition ${
                    selectedLanguage === 'sv'
                      ? 'bg-[#FFFFFF] text-[#24221F] shadow-[0_1px_2px_rgba(0,0,0,0.05)] border border-[#DDD4C6]'
                      : 'text-[#8F877B] hover:text-[#24221F]'
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
                      ? 'bg-[#FFFFFF] text-[#24221F] shadow-[0_1px_2px_rgba(0,0,0,0.05)] border border-[#DDD4C6]'
                      : 'text-[#8F877B] hover:text-[#24221F]'
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
              className="p-2 text-[#8F877B] hover:text-[#24221F] hover:bg-[#F5EFEB] rounded-xl transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Modal Body */}
        {!activeScenario ? (
          /* =========================================================================
             1. SCENARIO SELECTION VIEW (Artisanal postcards)
             ========================================================================= */
          <div className="p-6 overflow-y-auto max-h-[calc(92vh-90px)] space-y-6">
            
            {/* Custom Topic Generator Card */}
            <div className="bg-[#FFFFFF] border border-[#DDD4C6] rounded-2xl p-5 shadow-[0_2px_0_#EADFCF]">
              <div className="flex items-center gap-2 mb-1.5">
                <Sparkles className="w-4 h-4 text-[#C9862C]" />
                <h3 className="text-base font-bold font-display text-[#24221F]">Skapa eget samtalsämne</h3>
                <span className="text-[10px] font-mono-tag bg-[#FDF6EA] text-[#995E15] border border-[#F3E2C4] px-2 py-0.5 rounded">
                  AI Atelier
                </span>
              </div>
              <p className="text-xs text-[#5C564E] font-editorial italic mb-3">
                Beskriv vilken situation du vill simulera (t.ex. &quot;Beställa fika på bageri i Stockholm&quot; eller &quot;Teknisk anställningsintervju i London&quot;).
              </p>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={customTopic}
                  onChange={(e) => setCustomTopic(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleStartCustomScenario()}
                  placeholder={
                    selectedLanguage === 'sv'
                      ? 'T.ex. Förhandla hyra med en hyresvärd eller fråga om vägen...'
                      : 'E.g., Negotiating rent with a landlord or checking into a boutique hotel...'
                  }
                  className="flex-1 bg-[#FAF7F2] border border-[#DDD4C6] rounded-xl px-4 py-2.5 text-xs sm:text-sm text-[#24221F] placeholder-[#A89E90] focus:outline-none focus:border-[#2D5A3F] focus:ring-1 focus:ring-[#2D5A3F]"
                />
                <button
                  onClick={handleStartCustomScenario}
                  disabled={!customTopic.trim() || isStartingDialogue}
                  className="btn-craft px-5 py-2.5 btn-stamp-dark disabled:opacity-50 text-xs sm:text-sm flex items-center gap-2"
                >
                  <PlusCircle className="w-4 h-4" />
                  <span>Starta dialog</span>
                </button>
              </div>
            </div>

            {/* Predefined Scenarios List */}
            <div>
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                  <BookOpen className="w-4 h-4 text-[#2D5A3F]" />
                  <h3 className="text-base font-bold font-display text-[#24221F]">Välj ett hantverksrollspel</h3>
                </div>
                <span className="text-xs text-[#8F877B] font-mono-tag">
                  {scenarios.length} scenarier tillgängliga
                </span>
              </div>

              {loadingScenarios ? (
                <div className="flex items-center justify-center py-12 text-[#8F877B] gap-3">
                  <Loader2 className="w-5 h-5 animate-spin text-[#2D5A3F]" />
                  <span className="font-editorial text-sm">Hämtar samtalsstudion...</span>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {scenarios.map((scenario) => (
                    <div
                      key={scenario.id}
                      onClick={() => handleStartScenario(scenario)}
                      className="group bg-[#FFFFFF] hover:bg-[#FAF7F2] border border-[#E5DDD0] hover:border-[#24221F] rounded-2xl p-5 cursor-pointer transition-all duration-150 shadow-[0_2px_0_#EADFCF] hover:shadow-[0_4px_0_#24221F] flex flex-col justify-between"
                    >
                      <div>
                        <div className="flex items-start justify-between gap-3 mb-2">
                          <div className="flex items-center gap-3">
                            <span className="text-2xl p-2 bg-[#F5EFEB] rounded-xl border border-[#DDD4C6] group-hover:scale-105 transition-transform">
                              {scenario.avatar_emoji}
                            </span>
                            <div>
                              <h4 className="font-bold text-[#24221F] font-display text-base group-hover:text-[#2D5A3F] transition">
                                {scenario.title}
                              </h4>
                              {scenario.swedish_title && scenario.swedish_title !== scenario.title && (
                                <p className="text-xs text-[#5C564E] font-editorial italic">
                                  {scenario.swedish_title}
                                </p>
                              )}
                            </div>
                          </div>
                          <span className="text-[10px] font-mono-tag px-2 py-0.5 bg-[#FAF7F2] border border-[#DDD4C6] text-[#5C564E] rounded">
                            {scenario.level}
                          </span>
                        </div>

                        <p className="text-xs text-[#5C564E] font-sans leading-relaxed line-clamp-2 my-2.5">
                          {scenario.scenario_context}
                        </p>

                        <div className="flex items-center gap-2 text-xs text-[#8F877B] my-2">
                          <Bot className="w-3.5 h-3.5 text-[#2B5876]" />
                          <span>Roll: <strong className="text-[#24221F]">{scenario.persona_name}</strong></span>
                        </div>
                      </div>

                      <div className="flex items-center justify-between pt-3 border-t border-[#EDE7DD] mt-2">
                        <div className="flex flex-wrap gap-1.5">
                          <span className="text-[10px] font-mono-tag px-2 py-0.5 bg-[#F5EFEB] text-[#5C564E] border border-[#DDD4C6] rounded">
                            #{scenario.category}
                          </span>
                        </div>

                        <button className="btn-craft text-xs px-3.5 py-1.5 btn-stamp-forest">
                          Starta samtal →
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
             2. ACTIVE INTERACTIVE CONVERSATION VIEW (Literary correspondence)
             ========================================================================= */
          <div className="flex flex-col flex-1 h-[calc(92vh-90px)]">
            
            {/* Persona Info Ribbon */}
            <div className="bg-[#FFFFFF] border-b border-[#E5DDD0] px-6 py-2.5 flex items-center justify-between">
              <div className="flex items-center gap-2 text-xs text-[#5C564E]">
                <span className="w-2 h-2 rounded-full bg-[#2D5A3F]"></span>
                <span className="font-bold text-[#24221F] font-display">{activeScenario.title}</span>
                <span className="text-[#DDD4C6]">•</span>
                <span>Samtalspartner: <strong className="text-[#2B5876]">{activeScenario.persona_name}</strong></span>
              </div>

              <div className="flex items-center gap-2">
                <button
                  onClick={handleResetToScenarios}
                  className="text-xs text-[#8F877B] hover:text-[#24221F] font-bold px-2 py-1 rounded-lg hover:bg-[#F5EFEB] transition"
                >
                  Byt scenario
                </button>
              </div>
            </div>

            {/* Chat Timeline */}
            <div className="flex-1 p-6 overflow-y-auto space-y-4 bg-[#FAF7F2]">
              {messages.map((turn, index) => {
                const isAi = turn.sender === 'AI';
                return (
                  <div
                    key={index}
                    className={`flex flex-col ${isAi ? 'items-start' : 'items-end'} space-y-1.5`}
                  >
                    <div className="flex items-end gap-2 max-w-[85%]">
                      {isAi && (
                        <div className="w-8 h-8 rounded-xl bg-[#2B5876] text-white flex items-center justify-center text-sm flex-shrink-0 shadow-sm border border-[#1A374A]">
                          {activeScenario.avatar_emoji || '🤖'}
                        </div>
                      )}

                      <div
                        className={`rounded-2xl px-4 py-3 shadow-[0_2px_0_#EADFCF] ${
                          isAi
                            ? 'bg-[#FFFFFF] border border-[#DDD4C6] text-[#24221F] rounded-bl-sm'
                            : 'bg-[#2D5A3F] border border-[#1E3D2B] text-[#FAF7F2] rounded-br-sm'
                        }`}
                      >
                        <div className="flex items-start justify-between gap-4">
                          <p className="text-sm font-medium leading-relaxed font-sans">{turn.text}</p>
                          
                          {/* Speak & Translate buttons for AI turns */}
                          {isAi && (
                            <div className="flex items-center gap-1.5 flex-shrink-0">
                              <button
                                onClick={() => speakText(turn.text, selectedLanguage)}
                                title="Lyssna på uttal"
                                className="p-1 text-[#8F877B] hover:text-[#24221F] transition rounded"
                              >
                                <Volume2 className="w-4 h-4" />
                              </button>
                              {turn.translation && (
                                <button
                                  onClick={() => toggleTranslation(index)}
                                  title="Visa engelsk översättning"
                                  className={`p-1 transition rounded text-xs ${
                                    showTranslations[index] ? 'text-[#2D5A3F]' : 'text-[#8F877B] hover:text-[#24221F]'
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
                          <div className="mt-2 pt-2 border-t border-[#EDE7DD] text-xs text-[#5C564E] font-editorial italic">
                            🇬🇧 {turn.translation}
                          </div>
                        )}
                      </div>

                      {!isAi && (
                        <div className="w-8 h-8 rounded-xl bg-[#24221F] flex items-center justify-center text-white text-xs font-bold flex-shrink-0 shadow-sm">
                          <User className="w-4 h-4" />
                        </div>
                      )}
                    </div>

                    {/* ✨ Embedded Real-Time Grammar Correction Card (Editor's marginalia) */}
                    {!isAi && turn.correction_feedback && turn.correction_feedback.has_errors && (
                      <div className="max-w-[85%] mr-10 bg-[#FAECE8] border border-[#F6D3C8] rounded-2xl p-4 shadow-sm animate-fade-in space-y-2 text-[#632415]">
                        <div className="flex items-center gap-2 text-[#B34B32] font-bold text-xs">
                          <AlertTriangle className="w-4 h-4" />
                          <span className="font-display">Grammatikinsikt & Rättning</span>
                        </div>

                        {/* Highlighted Issues */}
                        {turn.correction_feedback.highlighted_issues && turn.correction_feedback.highlighted_issues.length > 0 && (
                          <div className="flex flex-wrap gap-1">
                            {turn.correction_feedback.highlighted_issues.map((issue, i) => (
                              <span
                                key={i}
                                className="text-[10px] font-mono-tag px-2 py-0.5 bg-[#FFFFFF] text-[#8A321E] border border-[#F6D3C8] rounded"
                              >
                                {issue}
                              </span>
                            ))}
                          </div>
                        )}

                        {/* Corrected Text */}
                        {turn.correction_feedback.corrected_text && (
                          <div className="bg-[#FFFFFF] rounded-xl p-2.5 border border-[#F6D3C8] text-xs flex items-start gap-2 shadow-inner">
                            <CheckCircle2 className="w-4 h-4 text-[#2D5A3F] flex-shrink-0 mt-0.5" />
                            <div>
                              <span className="text-[#8F877B] text-[11px] block font-mono-tag">Korrekt formulering:</span>
                              <strong className="text-[#2D5A3F] text-sm font-editorial">
                                {turn.correction_feedback.corrected_text}
                              </strong>
                            </div>
                          </div>
                        )}

                        {/* Pedagogical Rule Explanation */}
                        {turn.correction_feedback.grammar_rule_explanation && (
                          <div className="text-xs text-[#5C564E] flex items-start gap-2 bg-[#FFFFFF] p-2.5 rounded-xl border border-[#F6D3C8]">
                            <Lightbulb className="w-4 h-4 text-[#C9862C] flex-shrink-0 mt-0.5" />
                            <div>
                              <span className="text-[#995E15] font-bold text-[11px] block font-mono-tag">Grammatikregel:</span>
                              <p className="text-[#5C564E] leading-snug">
                                {turn.correction_feedback.grammar_rule_explanation}
                              </p>
                            </div>
                          </div>
                        )}

                        {/* Native Alternative Phrasing */}
                        {turn.correction_feedback.improved_native_alternative && (
                          <div className="text-xs text-[#8F877B] font-editorial italic">
                            💡 Naturligt uttryckssätt: &quot;{turn.correction_feedback.improved_native_alternative}&quot;
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}

              {isSendingTurn && (
                <div className="flex items-center gap-3 text-[#8F877B] text-xs py-2 animate-pulse">
                  <div className="w-7 h-7 rounded-lg bg-[#2B5876] text-white flex items-center justify-center text-xs">
                    {activeScenario.avatar_emoji || '🤖'}
                  </div>
                  <span className="font-editorial italic">{activeScenario.persona_name} funderar och formulerar svar...</span>
                </div>
              )}

              <div ref={chatEndRef} />
            </div>

            {/* Quick Suggestion Chips */}
            {suggestedChips && suggestedChips.length > 0 && !isSendingTurn && (
              <div className="px-6 py-2.5 bg-[#FFFFFF] border-t border-[#E5DDD0] flex items-center gap-2 overflow-x-auto">
                <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase flex-shrink-0">
                  Snabbsvar:
                </span>
                <div className="flex items-center gap-2 flex-wrap">
                  {suggestedChips.map((chip, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleSendMessage(chip)}
                      className="text-xs font-semibold px-3 py-1 bg-[#FAF7F2] hover:bg-[#F5EFEB] text-[#24221F] border border-[#DDD4C6] rounded-full transition whitespace-nowrap shadow-sm"
                    >
                      {chip}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Input Bar */}
            <div className="p-4 bg-[#FFFFFF] border-t border-[#E5DDD0] flex items-center gap-3">
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
                className="flex-1 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl px-4 py-3 text-sm text-[#24221F] placeholder-[#A89E90] focus:outline-none focus:border-[#2D5A3F] focus:ring-1 focus:ring-[#2D5A3F] disabled:opacity-50"
              />

              <button
                onClick={() => handleSendMessage()}
                disabled={!inputMessage.trim() || isSendingTurn}
                className="btn-craft p-3 btn-stamp-forest disabled:opacity-50 text-white rounded-2xl shadow-[0_3px_0_#1B3827] transition flex items-center justify-center"
                title="Skicka meddelande"
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
