import React, { useState } from 'react';
import { X, Send, Bot, Sparkles, Volume2, BookOpen } from 'lucide-react';
import { api } from '../services/api';
import { speakText, soundEffects } from '../services/audio';

interface AITutorModalProps {
  onClose: () => void;
  targetLanguage: string;
}

interface ChatMessage {
  id: string;
  sender: 'user' | 'ai';
  text: string;
  suggestedFollowups?: string[];
  vocabulary?: Array<{ word: string; translation: string }>;
}

export const AITutorModal: React.FC<AITutorModalProps> = ({ onClose, targetLanguage }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome',
      sender: 'ai',
      text: "🇸🇪 **Hej! I am TrioBot**, your AI language tutor.\n\nI can explain Swedish grammar (like *en vs. ett* or the *V2 verb rule*), share Swedish cultural facts (like *Fika*), or quiz you with fun practice sentences.\n\nWhat would you like to explore?",
      suggestedFollowups: [
        'Tell me about Swedish Fika',
        'How do En and Ett articles work?',
        'Explain Swedish word order (V2 rule)',
      ],
    },
  ]);
  const [inputQuery, setInputQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (textToSend: string) => {
    if (!textToSend.trim() || isLoading) return;

    soundEffects.playClickSound();

    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      sender: 'user',
      text: textToSend,
    };

    setMessages((prev) => [...prev, userMsg]);
    setInputQuery('');
    setIsLoading(true);

    try {
      const response = await api.askAITutor(textToSend, targetLanguage);
      const aiMsg: ChatMessage = {
        id: `ai-${Date.now()}`,
        sender: 'ai',
        text: response.reply,
        suggestedFollowups: response.suggested_followups,
        vocabulary: response.swedish_vocabulary,
      };
      setMessages((prev) => [...prev, aiMsg]);
    } catch (err) {
      const errorMsg: ChatMessage = {
        id: `err-${Date.now()}`,
        sender: 'ai',
        text: 'Sorry, could not reach the AI tutor right now. Make sure the backend server is running.',
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-3xl max-w-2xl w-full h-[600px] flex flex-col shadow-2xl overflow-hidden">
        
        <div className="p-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-indigo-600 flex items-center justify-center text-white shadow">
              <Bot className="w-6 h-6" />
            </div>
            <div>
              <h3 className="font-black text-white text-base">TrioBot AI Language Tutor</h3>
              <p className="text-xs text-indigo-400 font-semibold">
                Bilingual Swedish (Svenska) & English Assistant
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 hover:bg-slate-700 rounded-xl text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex flex-col ${msg.sender === 'user' ? 'items-end' : 'items-start'}`}
            >
              <div
                className={`max-w-[85%] rounded-2xl p-4 text-sm leading-relaxed ${
                  msg.sender === 'user'
                    ? 'bg-emerald-600 text-white rounded-br-none shadow-[0_3px_0_#047857]'
                    : 'bg-slate-800 border border-slate-700 text-slate-200 rounded-bl-none'
                }`}
              >
                <div className="whitespace-pre-line">{msg.text}</div>

                {msg.vocabulary && msg.vocabulary.length > 0 && (
                  <div className="mt-3 pt-3 border-t border-slate-700/60 space-y-1.5">
                    <div className="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1">
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>Vocabulary:</span>
                    </div>
                    {msg.vocabulary.map((v, i) => (
                      <div
                        key={i}
                        className="flex items-center justify-between text-xs bg-slate-900/60 px-2.5 py-1.5 rounded-lg"
                      >
                        <span className="font-bold text-amber-300">{v.word}</span>
                        <span className="text-slate-400">{v.translation}</span>
                        <button
                          onClick={() => speakText(v.word, 'sv')}
                          className="text-slate-400 hover:text-white ml-2"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {msg.suggestedFollowups && msg.suggestedFollowups.length > 0 && (
                <div className="flex flex-wrap gap-1.5 mt-2 max-w-[85%]">
                  {msg.suggestedFollowups.map((suggestion, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleSendMessage(suggestion)}
                      className="text-xs bg-indigo-950/70 border border-indigo-500/40 text-indigo-300 px-3 py-1 rounded-full hover:bg-indigo-900/80 transition flex items-center gap-1"
                    >
                      <Sparkles className="w-3 h-3 text-indigo-400" />
                      <span>{suggestion}</span>
                    </button>
                  ))}
                </div>
              )}
            </div>
          ))}

          {isLoading && (
            <div className="flex items-center gap-2 text-slate-400 text-xs italic">
              <Bot className="w-4 h-4 animate-spin text-indigo-400" />
              <span>TrioBot is thinking...</span>
            </div>
          )}
        </div>

        <div className="p-3 bg-slate-800/90 border-t border-slate-700 flex gap-2">
          <input
            type="text"
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSendMessage(inputQuery)}
            placeholder="Ask about Swedish grammar, words, phrases..."
            className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
          />
          <button
            onClick={() => handleSendMessage(inputQuery)}
            disabled={!inputQuery.trim() || isLoading}
            className="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-white rounded-xl font-bold transition flex items-center gap-1"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>

      </div>
    </div>
  );
};
