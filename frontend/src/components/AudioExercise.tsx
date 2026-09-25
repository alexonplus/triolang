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
        <h2 className="text-xl sm:text-2xl font-black text-white">
          {exercise.prompt_text}
        </h2>
        <p className="text-sm text-slate-400 mt-1">
          Tap the big speaker to replay the voice
        </p>
      </div>

      <div className="flex justify-center py-4">
        <button
          onClick={handlePlayAudio}
          className="w-24 h-24 rounded-3xl bg-sky-500 hover:bg-sky-400 text-white flex items-center justify-center btn-3d shadow-[0_6px_0_#0284c7] transition transform active:scale-95"
          title="Play audio"
        >
          <Volume2 className="w-12 h-12 stroke-[2.5]" />
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-left">
        {exercise.options?.map((option, idx) => {
          const isSelected = selectedOption === option;

          return (
            <button
              key={idx}
              onClick={() => {
                soundEffects.playClickSound();
                onSelectOption(option);
              }}
              className={`p-4 rounded-2xl font-bold transition border-2 flex items-center justify-between ${
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
