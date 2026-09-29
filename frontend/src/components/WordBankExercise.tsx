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
      
      {/* Exercise Prompt Title */}
      <div>
        <span className="text-[11px] font-mono-tag text-[#8F877B] uppercase block mb-1">
          Bygg meningen
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
            <span>Lyssna ({exercise.target_language === 'sv' ? 'Svenska' : 'Engelska'})</span>
          </button>
        )}
      </div>

      {/* Selected Words Canvas (Paper Slot) */}
      <div className="min-h-[100px] p-5 bg-[#FFFFFF] border-2 border-dashed border-[#D5CBBA] rounded-2xl flex flex-wrap gap-2.5 items-center shadow-inner">
        {selectedWords.length === 0 ? (
          <span className="text-[#8F877B] font-editorial italic text-base">
            Tryck på orden nedan för att bygga meningen...
          </span>
        ) : (
          selectedWords.map((word, idx) => (
            <button
              key={`selected-${idx}`}
              onClick={() => {
                soundEffects.playClickSound();
                onRemoveWord(idx);
              }}
              className="px-4 py-2 bg-[#2D5A3F] text-[#FAF7F2] font-bold rounded-xl shadow-[0_3px_0_#1E3D2B] border border-[#1E3D2B] hover:bg-[#386D4E] transition transform active:scale-95 text-base"
            >
              {word}
            </button>
          ))
        )}
      </div>

      {/* Word Bank Bank Tiles (Handcrafted letterpress tiles) */}
      <div className="flex flex-wrap gap-3 justify-center pt-4">
        {availableWords.map((item) => (
          <button
            key={`bank-${item.id}`}
            disabled={item.isUsed}
            onClick={() => {
              soundEffects.playClickSound();
              onToggleWord(item.word, item.id);
            }}
            className={`px-4 py-2.5 rounded-xl font-semibold text-base transition ${
              item.isUsed
                ? 'craft-tile-selected cursor-not-allowed opacity-40'
                : 'craft-tile'
            }`}
          >
            {item.word}
          </button>
        ))}
      </div>
    </div>
  );
};
