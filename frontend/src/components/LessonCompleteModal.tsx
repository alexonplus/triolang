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
    confetti({
      particleCount: 100,
      spread: 70,
      origin: { y: 0.6 },
    });
  }, []);

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border-2 border-emerald-500/50 rounded-3xl p-8 max-w-md w-full text-center space-y-6 shadow-2xl animate-in zoom-in-95">
        
        <div className="relative inline-block">
          <div className="w-24 h-24 rounded-3xl bg-amber-400/20 border-2 border-amber-400 flex items-center justify-center mx-auto text-amber-400 shadow-[0_0_30px_rgba(251,191,36,0.3)]">
            <Trophy className="w-14 h-14" />
          </div>
          <span className="absolute -top-2 -right-2 text-2xl animate-bounce">✨</span>
        </div>

        <div>
          <h2 className="text-3xl font-black text-white">Lektion Klar!</h2>
          <p className="text-slate-400 text-sm mt-1">{summary.message}</p>
        </div>

        <div className="grid grid-cols-3 gap-3">
          <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-2xl">
            <Zap className="w-6 h-6 text-amber-400 mx-auto mb-1 fill-amber-400" />
            <div className="text-xs font-bold text-slate-400 uppercase">Total XP</div>
            <div className="text-xl font-black text-amber-400">+{summary.xp_gained}</div>
          </div>

          <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-2xl">
            <Flame className="w-6 h-6 text-orange-400 mx-auto mb-1 fill-orange-400" />
            <div className="text-xs font-bold text-slate-400 uppercase">Streak</div>
            <div className="text-xl font-black text-orange-400">{summary.new_streak} D</div>
          </div>

          <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-2xl">
            <Gem className="w-6 h-6 text-cyan-400 mx-auto mb-1 fill-cyan-400" />
            <div className="text-xs font-bold text-slate-400 uppercase">Gems</div>
            <div className="text-xl font-black text-cyan-400">+{summary.gems_awarded}</div>
          </div>
        </div>

        <button
          onClick={onFinish}
          className="w-full py-4 btn-3d bg-emerald-500 hover:bg-emerald-400 shadow-[0_4px_0_#047857] text-white font-black rounded-2xl flex items-center justify-center gap-2 text-lg"
        >
          <span>Continue Learning</span>
          <ArrowRight className="w-6 h-6" />
        </button>

      </div>
    </div>
  );
};
