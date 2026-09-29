import React, { useEffect } from 'react';
import { Volume2 } from 'lucide-react';
import type { Exercise } from '../types';
import { speakText, soundEffects } from '../services/audio';

interface AudioExerciseProps {
  exercise: Exercise;
  selectedOption: string | null;
  onSelectOption: (option: string) => void;
}

export const AudioExercise: React.FC<AudioExerciseProps> = ({
  exercise,
  selectedOption,
  onSelectOption,
}) => {
  useEffect(() => {
    if (exercise.target_audio_text) {
      speakText(exercise.target_audio_text, exercise.target_language);
    }
  }, [exercise]);

  const handlePlayAudio = () => {
    if (exercise.target_audio_text) {
      speakText(exercise.target_audio_text, exercise.target_language);
    }
  };

  return (
    <div className="w-full max-w-xl mx-auto space-y-8 text-center">
      <div>
        <span className="text-[11px] font-mono-tag text-[#8F877B] uppercase block mb-1">
          Lyssna & Förstå
        </span>
        <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F] leading-tight">
          {exercise.prompt_text}
        </h2>
        <p className="text-sm text-[#5C564E] font-editorial italic mt-1">
          Tryck på högtalaren för att lyssna på uttalet igen
        </p>
      </div>

      <div className="flex justify-center py-4">
        <button
          onClick={handlePlayAudio}
          className="w-22 h-22 rounded-3xl bg-[#FFFFFF] hover:bg-[#F5EFEB] text-[#2B5876] border-2 border-[#DDD4C6] flex items-center justify-center btn-craft shadow-[0_4px_0_#DDD4C6] transition transform active:scale-95"
          title="Spela upp ljud"
        >
          <Volume2 className="w-10 h-10 stroke-[2.2]" />
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 text-left">
        {exercise.options?.map((option, idx) => {
          const isSelected = selectedOption === option;

          return (
            <button
              key={idx}
              onClick={() => {
                soundEffects.playClickSound();
                onSelectOption(option);
              }}
              className={`p-4 rounded-2xl font-bold transition flex items-center justify-between border-2 ${
                isSelected
                  ? 'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] shadow-[0_3px_0_#2D5A3F]'
                  : 'bg-[#FFFFFF] border-[#DDD4C6] text-[#24221F] hover:bg-[#FAF7F2] hover:border-[#24221F] shadow-[0_3px_0_#DDD4C6]'
              }`}
            >
              <span className="font-semibold text-base">{option}</span>
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
