import React from 'react';
import { Volume2 } from 'lucide-react';
import type { Exercise } from '../types';
import { speakText, soundEffects } from '../services/audio';

interface MultipleChoiceExerciseProps {
  exercise: Exercise;
  selectedOption: string | null;
  onSelectOption: (option: string) => void;
}

export const MultipleChoiceExercise: React.FC<MultipleChoiceExerciseProps> = ({
  exercise,
  selectedOption,
  onSelectOption,
}) => {
  return (
    <div className="w-full max-w-xl mx-auto space-y-6">
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
            <span>Hear pronunciation ({exercise.target_language === 'sv' ? 'Svenska' : 'English'})</span>
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-4">
        {exercise.options?.map((option, idx) => {
          const isSelected = selectedOption === option;

          return (
            <button
              key={idx}
              onClick={() => {
                soundEffects.playClickSound();
                onSelectOption(option);
              }}
              className={`p-4 rounded-2xl font-bold text-left transition border-2 flex items-center justify-between ${
                isSelected
                  ? 'bg-sky-500/20 border-sky-400 text-sky-200 shadow-[0_4px_0_#0284c7]'
                  : 'bg-slate-800 border-slate-700 text-slate-200 hover:bg-slate-750 hover:border-slate-600 shadow-[0_4px_0_#0f172a]'
              }`}
            >
              <span>{option}</span>
              <span className="w-7 h-7 rounded-lg border border-slate-600 flex items-center justify-center text-xs font-mono text-slate-400">
                {idx + 1}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
