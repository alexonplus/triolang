import React from 'react';
import { Star, Check, BookOpen, Coffee, Compass, Sparkles, Gift, Feather, Bookmark } from 'lucide-react';
import type { Unit } from '../types';
import { soundEffects } from '../services/audio';

interface LessonMapProps {
  units: Unit[];
  activeCourseTitle: string;
  onStartLesson: (lessonId: number) => void;
  onOpenGenerateModal: () => void;
}

const ICON_MAP: Record<string, React.ReactNode> = {
  Sparkles: <Sparkles className="w-5 h-5" />,
  Coffee: <Coffee className="w-5 h-5" />,
  Compass: <Compass className="w-5 h-5" />,
  BookOpen: <BookOpen className="w-5 h-5" />,
};

// Earthy, handcrafted Scandinavian color sets for Chapters
const CHAPTER_THEMES = [
  { bg: 'bg-[#2D5A3F]', border: 'border-[#1E3D2B]', shadow: 'shadow-[0_3px_0_#1E3D2B]', tag: 'Kapitel I' },
  { bg: 'bg-[#B34B32]', border: 'border-[#7A2E1C]', shadow: 'shadow-[0_3px_0_#7A2E1C]', tag: 'Kapitel II' },
  { bg: 'bg-[#2B5876]', border: 'border-[#1A374A]', shadow: 'shadow-[0_3px_0_#1A374A]', tag: 'Kapitel III' },
  { bg: 'bg-[#C9862C]', border: 'border-[#8C5917]', shadow: 'shadow-[0_3px_0_#8C5917]', tag: 'Kapitel IV' },
  { bg: 'bg-[#3F4765]', border: 'border-[#282E45]', shadow: 'shadow-[0_3px_0_#282E45]', tag: 'Kapitel V' },
];

export const LessonMap: React.FC<LessonMapProps> = ({
  units,
  activeCourseTitle,
  onStartLesson,
  onOpenGenerateModal,
}) => {
  return (
    <div className="max-w-2xl mx-auto py-10 px-4">
      
      {/* Editorial Header */}
      <div className="text-center mb-10 pb-6 border-b border-[#E5DDD0]">
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#EFE9DF] border border-[#DDD4C6] text-[11px] font-mono-tag text-[#5C564E] uppercase mb-3">
          <Bookmark className="w-3 h-3 text-[#2D5A3F]" />
          <span>Språkkurs & Studieplan</span>
        </div>
        
        <h1 className="text-3xl sm:text-4xl font-bold font-display text-[#24221F] tracking-tight">
          {activeCourseTitle}
        </h1>
        <p className="text-[#5C564E] font-editorial text-base sm:text-lg italic mt-1.5 max-w-lg mx-auto">
          Ett hantverksmässigt tillvägagångssätt för naturlig språkinlärning och flyt
        </p>

        <div className="mt-5">
          <button
            onClick={() => {
              soundEffects.playClickSound();
              onOpenGenerateModal();
            }}
            className="btn-craft px-5 py-2.5 text-xs sm:text-sm bg-[#FFFFFF] hover:bg-[#F5EFEB] text-[#24221F] border border-[#DDD4C6] shadow-[0_3px_0_#DDD4C6] transition"
          >
            <Feather className="w-4 h-4 text-[#B34B32] mr-2" />
            <span className="font-bold">Skapa anpassad AI-lektion</span>
          </button>
        </div>
      </div>

      {/* Chapters & Stamped Lesson Nodes */}
      <div className="space-y-16">
        {units.map((unit, unitIdx) => {
          const theme = CHAPTER_THEMES[unitIdx % CHAPTER_THEMES.length];

          return (
            <div key={unit.id} className="relative">
              
              {/* Chapter Card (Styled like a book cover / field guide chapter) */}
              <div
                className={`rounded-2xl p-6 mb-10 text-[#FAF7F2] relative overflow-hidden border ${theme.border} ${theme.bg} ${theme.shadow}`}
              >
                {/* Subtle paper texture overlay */}
                <div className="absolute inset-0 bg-[radial-gradient(#FAF7F2_1px,transparent_1px)] [background-size:16px_16px] opacity-10 pointer-events-none" />

                <div className="relative z-10 flex items-start justify-between gap-4">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="text-[10px] font-mono-tag tracking-widest uppercase bg-black/25 px-2 py-0.5 rounded border border-white/20">
                        {theme.tag}
                      </span>
                      <span className="text-xs font-semibold uppercase tracking-wider opacity-90">
                        {unit.title}
                      </span>
                    </div>

                    <h2 className="text-2xl font-bold font-display mt-1 text-white">
                      {unit.swedish_title}
                    </h2>
                    <p className="text-xs sm:text-sm text-[#FAF7F2]/85 mt-1.5 max-w-md leading-relaxed font-sans">
                      {unit.description}
                    </p>
                  </div>

                  <div className="p-3 bg-white/20 rounded-2xl backdrop-blur-sm border border-white/25 flex-shrink-0">
                    {ICON_MAP[unit.icon_name] || <Sparkles className="w-5 h-5 text-white" />}
                  </div>
                </div>
              </div>

              {/* Lesson Pathway (Handcrafted letterpress seals) */}
              <div className="flex flex-col items-center space-y-8 relative">
                
                {/* Background dashed journey thread */}
                <div className="absolute top-4 bottom-12 w-0.5 border-r-2 border-dashed border-[#D5CBBA] z-0" />

                {unit.lessons.map((lesson, idx) => {
                  const xOffsets = [0, 42, -42, 24, -24];
                  const offset = xOffsets[idx % xOffsets.length];

                  return (
                    <div
                      key={lesson.id}
                      className="flex flex-col items-center relative z-10"
                      style={{ transform: `translateX(${offset}px)` }}
                    >
                      <button
                        onClick={() => {
                          soundEffects.playClickSound();
                          onStartLesson(lesson.id);
                        }}
                        className={`relative w-18 h-18 sm:w-20 sm:h-20 rounded-2xl flex items-center justify-center font-bold transition-all btn-craft ${
                          lesson.is_completed
                            ? 'bg-[#EBF3ED] text-[#2D5A3F] border-2 border-[#2D5A3F] shadow-[0_4px_0_#2D5A3F] hover:bg-[#DEF0E2]'
                            : 'bg-[#FFFFFF] text-[#24221F] border-2 border-[#DDD4C6] shadow-[0_4px_0_#DDD4C6] hover:bg-[#FAF7F2] hover:border-[#24221F] hover:shadow-[0_4px_0_#24221F]'
                        }`}
                        title={lesson.title}
                      >
                        {lesson.is_completed ? (
                          <Check className="w-8 h-8 stroke-[3]" />
                        ) : (
                          <Star className="w-7 h-7 fill-[#C9862C] text-[#C9862C]" />
                        )}

                        {/* XP Badge Stamp */}
                        <span className="absolute -bottom-2.5 bg-[#FAF7F2] border border-[#D5CBBA] text-[#5C564E] text-[10px] font-mono-tag px-2 py-0.5 rounded-full shadow-sm">
                          +{lesson.xp_reward} XP
                        </span>
                      </button>

                      <span className="mt-4 font-bold text-xs text-[#24221F] max-w-[160px] text-center font-editorial leading-tight">
                        {lesson.swedish_title}
                      </span>
                    </div>
                  );
                })}

                {/* Chapter Completion Seal / Chest */}
                <div className="pt-4 flex flex-col items-center relative z-10">
                  <div className="w-14 h-14 rounded-2xl bg-[#FFFFFF] border-2 border-dashed border-[#C9862C] flex items-center justify-center text-[#C9862C] shadow-[0_2px_0_#EADFCF]">
                    <Gift className="w-6 h-6 animate-pulse" />
                  </div>
                  <span className="text-[11px] text-[#8F877B] font-mono-tag uppercase mt-2">
                    Kapitelbonus
                  </span>
                </div>

              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
