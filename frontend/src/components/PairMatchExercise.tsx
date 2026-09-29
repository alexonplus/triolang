import React, { useState, useEffect } from 'react';
import { Check } from 'lucide-react';
import type { Exercise } from '../types';
import { soundEffects } from '../services/audio';

interface PairMatchExerciseProps {
  exercise: Exercise;
  onAllMatched: () => void;
}

interface TileItem {
  id: string;
  text: string;
  pairKey: string;
  isMatched: boolean;
}

export const PairMatchExercise: React.FC<PairMatchExerciseProps> = ({
  exercise,
  onAllMatched,
}) => {
  const [tiles, setTiles] = useState<TileItem[]>([]);
  const [selectedTile, setSelectedTile] = useState<TileItem | null>(null);

  useEffect(() => {
    if (!exercise.pairs) return;

    const pairEntries = Object.entries(exercise.pairs);
    const generatedTiles: TileItem[] = [];

    pairEntries.forEach(([svWord, enWord], idx) => {
      generatedTiles.push({
        id: `left-${idx}`,
        text: svWord,
        pairKey: `pair-${idx}`,
        isMatched: false,
      });
      generatedTiles.push({
        id: `right-${idx}`,
        text: enWord,
        pairKey: `pair-${idx}`,
        isMatched: false,
      });
    });

    setTiles(generatedTiles.sort(() => Math.random() - 0.5));
    setSelectedTile(null);
  }, [exercise]);

  const handleTileClick = (tile: TileItem) => {
    if (tile.isMatched) return;

    soundEffects.playClickSound();

    if (!selectedTile) {
      setSelectedTile(tile);
      return;
    }

    if (selectedTile.id === tile.id) {
      setSelectedTile(null);
      return;
    }

    if (selectedTile.pairKey === tile.pairKey) {
      soundEffects.playCorrectSound();
      const updated = tiles.map((t) =>
        t.pairKey === tile.pairKey ? { ...t, isMatched: true } : t
      );
      setTiles(updated);
      setSelectedTile(null);

      if (updated.every((t) => t.isMatched)) {
        onAllMatched();
      }
    } else {
      soundEffects.playIncorrectSound();
      setSelectedTile(null);
    }
  };

  return (
    <div className="w-full max-w-xl mx-auto space-y-6">
      <div>
        <span className="text-[11px] font-mono-tag text-[#8F877B] uppercase block mb-1">
          Koppla ihop ordpar
        </span>
        <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F] leading-tight">
          {exercise.prompt_text}
        </h2>
        <p className="text-sm text-[#5C564E] font-editorial italic mt-1">
          Tryck på ett ord på svenska och dess matchande översättning på engelska
        </p>
      </div>

      <div className="grid grid-cols-2 gap-3.5 pt-2">
        {tiles.map((tile) => {
          const isSelected = selectedTile?.id === tile.id;

          return (
            <button
              key={tile.id}
              disabled={tile.isMatched}
              onClick={() => handleTileClick(tile)}
              className={`p-4 rounded-2xl font-bold transition flex items-center justify-between border-2 ${
                tile.isMatched
                  ? 'craft-tile-matched opacity-50 cursor-default shadow-none'
                  : isSelected
                  ? 'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] shadow-[0_3px_0_#2D5A3F]'
                  : 'bg-[#FFFFFF] border-[#DDD4C6] text-[#24221F] hover:bg-[#FAF7F2] hover:border-[#24221F] shadow-[0_3px_0_#DDD4C6]'
              }`}
            >
              <span className="font-semibold text-base">{tile.text}</span>
              {tile.isMatched && <Check className="w-4 h-4 text-[#2D5A3F]" />}
            </button>
          );
        })}
      </div>
    </div>
  );
};
