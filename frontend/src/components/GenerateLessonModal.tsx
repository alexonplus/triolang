import React, { useState } from 'react';
import { X, Sparkles, Feather, Loader2, AlertCircle } from 'lucide-react';
import { api } from '../services/api';
import { soundEffects } from '../services/audio';

interface GenerateLessonModalProps {
  courseId: string;
  courseTitle: string;
  onClose: () => void;
  onLessonGenerated: () => void;
}

const TOPIC_SUGGESTIONS = [
  { label: '🏥 Läkarbesök & Hälsa (Vårdcentral)', topic: 'At the doctor and health clinic' },
  { label: '☕️ Svensk Fika & Bakverk', topic: 'Ordering coffee and pastries at a Swedish cafe' },
  { label: '💼 Tech Jobbintervju', topic: 'Software developer job interview' },
  { label: '🚇 Stockholms Tunnelbana', topic: 'Riding the subway and bus in Stockholm' },
  { label: '🏨 Hotellincheckning', topic: 'Checking into a hotel room' },
  { label: '🍽️ Restaurangbesök & Notan', topic: 'Dining at a restaurant and paying the bill' },
  { label: '🇸🇪 Svenskt Midsommarfirande', topic: 'Swedish Midsummer celebration and traditions' },
  { label: '🛒 Handla mat på ICA & Coop', topic: 'Supermarket grocery shopping' },
];

export const GenerateLessonModal: React.FC<GenerateLessonModalProps> = ({
  courseId,
  courseTitle,
  onClose,
  onLessonGenerated,
}) => {
  const [topicInput, setTopicInput] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async (selectedTopic: string) => {
    if (!selectedTopic.trim() || isGenerating) return;

    soundEffects.playClickSound();
    setIsGenerating(true);
    setError(null);

    try {
      await api.generateAILesson(selectedTopic.trim(), courseId);
      soundEffects.playCorrectSound();
      onLessonGenerated();
      onClose();
    } catch (err: unknown) {
      console.error('Failed to generate lesson:', err);
      setError('Kunde inte generera lektionen. Kontrollera att servern körs.');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl max-w-lg w-full p-6 space-y-6 shadow-[0_16px_48px_rgba(45,35,25,0.15)] animate-in zoom-in-95">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-[#24221F] text-[#FAF7F2] flex items-center justify-center shadow-[0_2px_0_#141312] border border-[#141312]">
              <Feather className="w-5 h-5 text-[#FAF7F2]" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-lg">Skapa Skräddarsydd Lektion</h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                AI-genererad pedagogisk lektion för {courseTitle}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            disabled={isGenerating}
            className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Input */}
        <div className="space-y-2">
          <label className="text-xs font-mono-tag text-[#8F877B] uppercase tracking-wider block">
            Ange ett ämne eller situation:
          </label>
          <div className="flex gap-2">
            <input
              type="text"
              value={topicInput}
              onChange={(e) => setTopicInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleGenerate(topicInput)}
              disabled={isGenerating}
              placeholder="T.ex. Hyra stuga i skärgården, Köpa tågbiljett..."
              className="flex-1 bg-[#FFFFFF] border border-[#DDD4C6] rounded-xl px-4 py-3 text-sm text-[#24221F] placeholder-[#A89E90] focus:outline-none focus:border-[#2D5A3F]"
            />
          </div>
        </div>

        {/* Suggestions */}
        <div className="space-y-2">
          <label className="text-xs font-mono-tag text-[#8F877B] uppercase tracking-wider flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-[#C9862C]" />
            <span>Populära ämnesförslag:</span>
          </label>
          <div className="flex flex-wrap gap-2 max-h-44 overflow-y-auto pr-1">
            {TOPIC_SUGGESTIONS.map((item, idx) => (
              <button
                key={idx}
                disabled={isGenerating}
                onClick={() => {
                  setTopicInput(item.topic);
                  handleGenerate(item.topic);
                }}
                className="text-xs bg-[#FFFFFF] hover:bg-[#F5EFEB] border border-[#DDD4C6] hover:border-[#24221F] text-[#24221F] px-3 py-2 rounded-xl transition text-left flex items-center gap-1.5 font-medium shadow-sm"
              >
                <span>{item.label}</span>
              </button>
            ))}
          </div>
        </div>

        {error && (
          <div className="flex items-center gap-2 p-3 bg-[#FAECE8] border border-[#F6D3C8] rounded-xl text-xs text-[#632415]">
            <AlertCircle className="w-4 h-4 shrink-0 text-[#B34B32]" />
            <span>{error}</span>
          </div>
        )}

        <button
          onClick={() => handleGenerate(topicInput)}
          disabled={!topicInput.trim() || isGenerating}
          className="w-full py-3.5 btn-craft btn-stamp-dark text-white rounded-2xl flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed text-sm font-bold shadow-md"
        >
          {isGenerating ? (
            <>
              <Loader2 className="w-4 h-4 animate-spin text-[#FAF7F2]" />
              <span className="font-editorial italic">Formar övningar och ordförråd...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-4 h-4 text-[#C9862C]" />
              <span>Generera lektion nu</span>
            </>
          )}
        </button>

      </div>
    </div>
  );
};
