import React, { useState } from 'react';
import { X, Sparkles, Wand2, Loader2, AlertCircle } from 'lucide-react';
import { api } from '../services/api';
import { soundEffects } from '../services/audio';

interface GenerateLessonModalProps {
  courseId: string;
  courseTitle: string;
  onClose: () => void;
  onLessonGenerated: () => void;
}

const TOPIC_SUGGESTIONS = [
  { label: '🏥 Doctor & Health (Vårdcentral)', topic: 'At the doctor and health clinic' },
  { label: '☕️ Ordering Swedish Fika', topic: 'Ordering coffee and pastries at a Swedish cafe' },
  { label: '💼 Tech Job Interview', topic: 'Software developer job interview' },
  { label: '🚇 Stockholm Metro & Transit', topic: 'Riding the subway and bus in Stockholm' },
  { label: '🏨 Hotel Check-in & Keys', topic: 'Checking into a hotel room' },
  { label: '🍕 Restaurant & Ordering Food', topic: 'Dining at a restaurant and paying the bill' },
  { label: '🇸🇪 Swedish Midsommar', topic: 'Swedish Midsummer celebration and traditions' },
  { label: '🛒 Grocery Shopping (ICA & Coop)', topic: 'Supermarket grocery shopping' },
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
      setError('Could not generate lesson. Please check that the Python backend is running.');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-3xl max-w-lg w-full p-6 space-y-6 shadow-2xl animate-in zoom-in-95">
        
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-500 flex items-center justify-center text-white shadow">
              <Wand2 className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-black text-white text-lg">Generate AI Lesson</h3>
              <p className="text-xs text-indigo-400 font-semibold">
                Powered by Google Gemini for {courseTitle}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            disabled={isGenerating}
            className="p-2 hover:bg-slate-800 rounded-xl text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-2">
          <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">
            Enter Any Topic or Situation:
          </label>
          <div className="flex gap-2">
            <input
              type="text"
              value={topicInput}
              onChange={(e) => setTopicInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleGenerate(topicInput)}
              disabled={isGenerating}
              placeholder="e.g. Renting an apartment, Buying train tickets..."
              className="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>
        </div>

        <div className="space-y-2">
          <label className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-amber-400" />
            <span>Popular Suggestions:</span>
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
                className="text-xs bg-slate-800 hover:bg-indigo-950 hover:border-indigo-500/60 border border-slate-700 text-slate-300 px-3 py-2 rounded-xl transition text-left flex items-center gap-1.5 font-medium"
              >
                <span>{item.label}</span>
              </button>
            ))}
          </div>
        </div>

        {error && (
          <div className="flex items-center gap-2 p-3 bg-rose-950/60 border border-rose-500/40 rounded-xl text-xs text-rose-300">
            <AlertCircle className="w-4 h-4 shrink-0 text-rose-400" />
            <span>{error}</span>
          </div>
        )}

        <button
          onClick={() => handleGenerate(topicInput)}
          disabled={!topicInput.trim() || isGenerating}
          className="w-full py-3.5 btn-3d bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 shadow-[0_4px_0_#3730a3] text-white font-black rounded-2xl flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isGenerating ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              <span>Generating curriculum & exercises...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5 text-amber-300" />
              <span>Create Lesson Now</span>
            </>
          )}
        </button>

      </div>
    </div>
  );
};
