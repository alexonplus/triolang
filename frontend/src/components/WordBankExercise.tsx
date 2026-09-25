import React from 'react';
import { Volume2 } from 'lucide-react';
import type { Exercise } from '../types';
import { speakText, soundEffects } from '../services/audio';

interface WordBankExerciseProps {
  exercise: Exercise;
  selectedWords: string[];
  onToggleWord: (word: string, index: number) => void;
  onRemoveWord: (index: number) => void;
  availableWords: Array<{ id: number; word: string; isUsed: boolean }>;
}

export const WordBankExercise: React.FC<WordBankExerciseProps> = ({
  exercise,
  selectedWords,
  onToggleWord,
  onRemoveWord,
  availableWords,
}) => {
  return (
    <div className="w-full max-w-xl mx-auto space-y-8">
      <div>
        <h2 className="text-xl sm:text-2xl font-black text-white">
          {exercise.prompt_text}
        </h2>
        {exercise.target_audio_text && (
          <button
            onClick={() => {
              speakText(exercise.target_audio_text!, exercise.target_language);
            }}
            className="mt-3 flex items-center gap-2 px-3 py-1.5 bg-sky-500/20 text-sky-400 hover:bg-sky-500/30 rounded-xl font-bold text-sm transition"
          >
            <Volume2 className="w-4 h-4" />
            <span>Listen ({exercise.target_language === 'sv' ? 'Svenska' : 'English'})</span>
          </button>
        )}
      </div>

      <div className="min-h-[90px] p-4 bg-slate-800/80 border-2 border-dashed border-slate-600 rounded-2xl flex flex-wrap gap-2 items-center">
        {selectedWords.length === 0 ? (
          <span className="text-slate-500 text-sm italic">
            Tap words below to build your sentence...
          </span>
        ) : (
          selectedWords.map((word, idx) => (
            <button
              key={`selected-${idx}`}
              onClick={() => {
                soundEffects.playClickSound();
                onRemoveWord(idx);
              }}
              className="px-4 py-2 bg-emerald-500 text-white font-bold rounded-xl shadow-[0_3px_0_#047857] hover:bg-emerald-400 transition transform active:scale-95"
            >
              {word}
            </button>
          ))
        )}
      </div>

      <div className="flex flex-wrap gap-3 justify-center pt-4">
        {availableWords.map((item) => (
          <button
            key={`bank-${item.id}`}
            disabled={item.isUsed}
            onClick={() => {
              soundEffects.playClickSound();
              onToggleWord(item.word, item.id);
            }}
            className={`px-4 py-2.5 font-bold rounded-xl transition text-base ${
              item.isUsed
                ? 'bg-slate-800 text-slate-600 border border-slate-700/50 cursor-not-allowed opacity-40'
                : 'btn-3d-tile'
            }`}
          >
            {item.word}
          </button>
        ))}
      </div>
    </div>
  );
};
