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
      text: "🇸🇪 **Hej! Jag är TrioBot**, din personliga språklärare och studiehandledare.\n\nJag kan förklara svensk grammatik (som *en vs. ett* eller *V2-regeln*), berätta om svenska traditioner (som *Fika* och *Midsommar*), eller skapa skräddarsydda övningsmeningar åt dig.\n\nVad vill du fördjupa dig i idag?",
      suggestedFollowups: [
        'Berätta om svensk Fika-kultur',
        'Hur fungerar En och Ett-artiklar?',
        'Förklara V2-inversion och ordföljd',
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
        text: 'Kunde inte nå TrioBot just nu. Kontrollera att servern körs.',
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl max-w-2xl w-full h-[620px] flex flex-col shadow-[0_16px_48px_rgba(45,35,25,0.15)] overflow-hidden">
        
        {/* Header Bar */}
        <div className="p-4 bg-[#FFFFFF] border-b border-[#E5DDD0] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-[#24221F] text-[#FAF7F2] flex items-center justify-center shadow-[0_2px_0_#141312] border border-[#141312]">
              <Bot className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-base">TrioBot AI Handledare</h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                Tvåspråkig handledare för svenska och engelska
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Chat Stream */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-[#FAF7F2]">
          {messages.map((msg) => (
            <div
              key={msg.id}
              className={`flex flex-col ${msg.sender === 'user' ? 'items-end' : 'items-start'}`}
            >
              <div
                className={`max-w-[85%] rounded-2xl p-4 text-sm leading-relaxed shadow-[0_2px_0_#EADFCF] ${
                  msg.sender === 'user'
                    ? 'bg-[#2D5A3F] text-[#FAF7F2] rounded-br-none border border-[#1E3D2B]'
                    : 'bg-[#FFFFFF] border border-[#DDD4C6] text-[#24221F] rounded-bl-none'
                }`}
              >
                <div className="whitespace-pre-line font-sans">{msg.text}</div>

                {msg.vocabulary && msg.vocabulary.length > 0 && (
                  <div className="mt-3 pt-3 border-t border-[#EDE7DD] space-y-1.5">
                    <div className="text-[10px] font-mono-tag text-[#2B5876] uppercase tracking-wider flex items-center gap-1">
                      <BookOpen className="w-3.5 h-3.5" />
                      <span>Glosor & Uttal:</span>
                    </div>
                    {msg.vocabulary.map((v, i) => (
                      <div
                        key={i}
                        className="flex items-center justify-between text-xs bg-[#FAF7F2] px-2.5 py-1.5 rounded-xl border border-[#DDD4C6]"
                      >
                        <span className="font-bold text-[#24221F] font-editorial">{v.word}</span>
                        <span className="text-[#5C564E]">{v.translation}</span>
                        <button
                          onClick={() => speakText(v.word, 'sv')}
                          className="text-[#8F877B] hover:text-[#24221F] ml-2"
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
                      className="text-xs bg-[#FFFFFF] border border-[#DDD4C6] text-[#24221F] px-3 py-1 rounded-full hover:bg-[#F5EFEB] transition flex items-center gap-1 shadow-sm"
                    >
                      <Sparkles className="w-3 h-3 text-[#C9862C]" />
                      <span>{suggestion}</span>
                    </button>
                  ))}
                </div>
              )}
            </div>
          ))}

          {isLoading && (
            <div className="flex items-center gap-2 text-[#8F877B] text-xs font-editorial italic">
              <Bot className="w-4 h-4 animate-spin text-[#2B5876]" />
              <span>TrioBot formulerar svaret...</span>
            </div>
          )}
        </div>

        {/* Input Bar */}
        <div className="p-3 bg-[#FFFFFF] border-t border-[#E5DDD0] flex gap-2">
          <input
            type="text"
            value={inputQuery}
            onChange={(e) => setInputQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSendMessage(inputQuery)}
            placeholder="Fråga om svensk grammatik, ord, regler eller uttryck..."
            className="flex-1 bg-[#FAF7F2] border border-[#DDD4C6] rounded-xl px-4 py-2.5 text-sm text-[#24221F] placeholder-[#A89E90] focus:outline-none focus:border-[#2D5A3F]"
          />
          <button
            onClick={() => handleSendMessage(inputQuery)}
            disabled={!inputQuery.trim() || isLoading}
            className="px-4 py-2.5 btn-craft btn-stamp-dark disabled:opacity-40 text-white rounded-xl text-xs font-bold transition flex items-center gap-1"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>

      </div>
    </div>
  );
};
