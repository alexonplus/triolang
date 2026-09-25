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
        <h2 className="text-xl sm:text-2xl font-black text-white">
          {exercise.prompt_text}
        </h2>
        <p className="text-sm text-slate-400 mt-1">
          Tap one word in Swedish and its matching word in English
        </p>
      </div>

      <div className="grid grid-cols-2 gap-3 pt-2">
        {tiles.map((tile) => {
          const isSelected = selectedTile?.id === tile.id;

          return (
            <button
              key={tile.id}
              disabled={tile.isMatched}
              onClick={() => handleTileClick(tile)}
              className={`p-4 rounded-2xl font-bold transition flex items-center justify-between border-2 ${
                tile.isMatched
                  ? 'bg-slate-900/50 border-slate-800 text-slate-600 opacity-40 cursor-default'
                  : isSelected
                  ? 'bg-emerald-500/20 border-emerald-400 text-emerald-200 shadow-[0_4px_0_#059669]'
                  : 'bg-slate-800 border-slate-700 text-slate-200 hover:bg-slate-750 hover:border-slate-600 shadow-[0_4px_0_#0f172a]'
              }`}
            >
              <span>{tile.text}</span>
              {tile.isMatched && <Check className="w-5 h-5 text-slate-600" />}
            </button>
          );
        })}
      </div>
    </div>
  );
};
