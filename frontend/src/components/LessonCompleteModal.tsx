import React, { useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Trophy, Zap, Flame, Gem, ArrowRight } from 'lucide-react';
import type { LessonCompleteResponse } from '../types';
import { soundEffects } from '../services/audio';

interface LessonCompleteModalProps {
  summary: LessonCompleteResponse;
  onFinish: () => void;
}

export const LessonCompleteModal: React.FC<LessonCompleteModalProps> = ({
  summary,
  onFinish,
}) => {
  useEffect(() => {
    soundEffects.playVictorySound();
    try {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
      });
    } catch {
      // Fallback
    }
  }, []);

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl p-8 max-w-md w-full text-center space-y-6 shadow-[0_16px_48px_rgba(45,35,25,0.15)] animate-in zoom-in-95">
        
        {/* Seal Trophy Stamp */}
        <div className="relative inline-block">
          <div className="w-20 h-20 rounded-3xl bg-[#FFFFFF] border-2 border-[#C9862C] flex items-center justify-center mx-auto text-[#C9862C] shadow-[0_4px_0_#C9862C]">
            <Trophy className="w-10 h-10" />
          </div>
          <span className="absolute -top-2 -right-2 text-xl">🌿</span>
        </div>

        <div>
          <span className="text-[11px] font-mono-tag text-[#2D5A3F] uppercase block mb-1">
            Kapitelsteg Avklarat
          </span>
          <h2 className="text-3xl font-bold font-display text-[#24221F]">Lektionen är klar!</h2>
          <p className="text-[#5C564E] text-xs font-editorial italic mt-1.5">{summary.message}</p>
        </div>

        <div className="grid grid-cols-3 gap-3">
          <div className="bg-[#FFFFFF] border border-[#DDD4C6] p-3.5 rounded-2xl shadow-sm">
            <Zap className="w-5 h-5 text-[#C9862C] mx-auto mb-1 fill-[#C9862C]" />
            <div className="text-[10px] font-mono-tag text-[#8F877B] uppercase">Total XP</div>
            <div className="text-lg font-bold font-display text-[#24221F]">+{summary.xp_gained}</div>
          </div>

          <div className="bg-[#FFFFFF] border border-[#DDD4C6] p-3.5 rounded-2xl shadow-sm">
            <Flame className="w-5 h-5 text-[#B34B32] mx-auto mb-1 fill-[#B34B32]" />
            <div className="text-[10px] font-mono-tag text-[#8F877B] uppercase">Streak</div>
            <div className="text-lg font-bold font-display text-[#24221F]">{summary.new_streak} d</div>
          </div>

          <div className="bg-[#FFFFFF] border border-[#DDD4C6] p-3.5 rounded-2xl shadow-sm">
            <Gem className="w-5 h-5 text-[#2B5876] mx-auto mb-1 fill-[#2B5876]" />
            <div className="text-[10px] font-mono-tag text-[#8F877B] uppercase">Gems</div>
            <div className="text-lg font-bold font-display text-[#24221F]">+{summary.gems_awarded}</div>
          </div>
        </div>

        <button
          onClick={onFinish}
          className="w-full py-3.5 btn-craft btn-stamp-forest flex items-center justify-center gap-2 text-sm font-bold shadow-md"
        >
          <span>Återvänd till kartan</span>
          <ArrowRight className="w-4 h-4 stroke-[2.5]" />
        </button>

      </div>
    </div>
  );
};
