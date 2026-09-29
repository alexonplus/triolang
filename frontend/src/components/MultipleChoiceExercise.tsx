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
    <div className="w-full max-w-xl mx-auto space-y-8">
      <div>
        <span className="text-[11px] font-mono-tag text-[#8F877B] uppercase block mb-1">
          Flervalsfråga
        </span>
        <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F] leading-tight">
          {exercise.prompt_text}
        </h2>
        {exercise.target_audio_text && (
          <button
            onClick={() => {
              speakText(exercise.target_audio_text!, exercise.target_language);
            }}
            className="mt-3 flex items-center gap-2 px-3 py-1.5 bg-[#FFFFFF] border border-[#DDD4C6] text-[#2B5876] hover:bg-[#F5EFEB] rounded-xl font-bold text-xs shadow-[0_2px_0_#DDD4C6] transition"
          >
            <Volume2 className="w-4 h-4 text-[#2B5876]" />
            <span>Uttal ({exercise.target_language === 'sv' ? 'Svenska' : 'Engelska'})</span>
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-2">
        {exercise.options?.map((option, idx) => {
          const isSelected = selectedOption === option;

          return (
            <button
              key={idx}
              onClick={() => {
                soundEffects.playClickSound();
                onSelectOption(option);
              }}
              className={`p-4 rounded-2xl font-bold text-left transition flex items-center justify-between border-2 ${
                isSelected
                  ? 'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] shadow-[0_3px_0_#2D5A3F]'
                  : 'bg-[#FFFFFF] border-[#DDD4C6] text-[#24221F] hover:bg-[#FAF7F2] hover:border-[#24221F] shadow-[0_3px_0_#DDD4C6]'
              }`}
            >
              <span className="text-base font-sans font-semibold">{option}</span>
              <span
                className={`w-7 h-7 rounded-lg border flex items-center justify-center text-xs font-mono-tag transition ${
                  isSelected
                    ? 'border-[#2D5A3F] bg-[#2D5A3F] text-white'
                    : 'border-[#DDD4C6] bg-[#FAF7F2] text-[#8F877B]'
                }`}
              >
                {String.fromCharCode(65 + idx)}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
