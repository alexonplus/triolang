import React from 'react';
import { Star, Check, BookOpen, Coffee, Compass, Sparkles, Gift, Wand2 } from 'lucide-react';
import type { Unit } from '../types';
import { soundEffects } from '../services/audio';

interface LessonMapProps {
  units: Unit[];
  activeCourseTitle: string;
  onStartLesson: (lessonId: number) => void;
  onOpenGenerateModal: () => void;
}

const ICON_MAP: Record<string, React.ReactNode> = {
  Sparkles: <Sparkles className="w-6 h-6" />,
  Coffee: <Coffee className="w-6 h-6" />,
  Compass: <Compass className="w-6 h-6" />,
  BookOpen: <BookOpen className="w-6 h-6" />,
};

export const LessonMap: React.FC<LessonMapProps> = ({
  units,
  activeCourseTitle,
  onStartLesson,
  onOpenGenerateModal,
}) => {
  return (
    <div className="max-w-2xl mx-auto py-8 px-4">
      <div className="text-center mb-6">
        <h1 className="text-3xl font-black text-white tracking-tight">
          {activeCourseTitle}
        </h1>
        <p className="text-slate-400 text-sm mt-1">
          Master daily vocabulary, Swedish fika dialogues, and conversational grammar
        </p>

        <div className="mt-4">
          <button
            onClick={() => {
              soundEffects.playClickSound();
              onOpenGenerateModal();
            }}
            className="inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-purple-600 via-indigo-600 to-sky-600 hover:from-purple-500 hover:to-sky-500 text-white font-black text-sm rounded-2xl shadow-[0_4px_0_#3730a3] btn-3d transition"
          >
            <Wand2 className="w-4 h-4 text-amber-300" />
            <span>✨ Generate Custom AI Lesson</span>
          </button>
        </div>
      </div>

      <div className="space-y-12">
        {units.map((unit) => (
          <div key={unit.id} className="relative">
            <div
              className="rounded-2xl p-5 mb-8 shadow-lg border border-slate-700 text-white relative overflow-hidden"
              style={{ backgroundColor: unit.theme_color || '#10B981' }}
            >
              <div className="relative z-10 flex items-start justify-between">
                <div>
                  <div className="text-xs font-black uppercase tracking-wider opacity-80">
                    {unit.title}
                  </div>
                  <h2 className="text-xl font-black mt-0.5">{unit.swedish_title}</h2>
                  <p className="text-sm opacity-90 mt-1 max-w-md">{unit.description}</p>
                </div>
                <div className="p-3 bg-white/15 rounded-2xl backdrop-blur-sm">
                  {ICON_MAP[unit.icon_name] || <Sparkles className="w-6 h-6" />}
                </div>
              </div>
            </div>

            <div className="flex flex-col items-center space-y-6">
              {unit.lessons.map((lesson, idx) => {
                const xOffsets = [0, 40, -40, 20, -20];
                const offset = xOffsets[idx % xOffsets.length];

                return (
                  <div
                    key={lesson.id}
                    className="flex flex-col items-center"
                    style={{ transform: `translateX(${offset}px)` }}
                  >
                    <button
                      onClick={() => {
                        soundEffects.playClickSound();
                        onStartLesson(lesson.id);
                      }}
                      className={`relative w-20 h-20 rounded-full flex items-center justify-center font-black transition-all btn-3d ${
                        lesson.is_completed
                          ? 'bg-amber-400 text-amber-950 shadow-[0_6px_0_#d97706] hover:bg-amber-300'
                          : 'bg-emerald-500 text-white shadow-[0_6px_0_#059669] hover:bg-emerald-400'
                      }`}
                      title={lesson.title}
                    >
                      {lesson.is_completed ? (
                        <Check className="w-10 h-10 stroke-[3.5]" />
                      ) : (
                        <Star className="w-9 h-9 fill-white" />
                      )}

                      <span className="absolute -bottom-2 bg-slate-900 border border-slate-700 text-emerald-400 text-xs font-bold px-2 py-0.5 rounded-full shadow">
                        +{lesson.xp_reward} XP
                      </span>
                    </button>

                    <span className="mt-4 font-bold text-xs text-slate-300 max-w-[150px] text-center">
                      {lesson.swedish_title}
                    </span>
                  </div>
                );
              })}

              <div className="pt-4 flex flex-col items-center">
                <div className="w-16 h-16 rounded-2xl bg-slate-800 border-2 border-dashed border-amber-500/50 flex items-center justify-center text-amber-400 shadow-inner">
                  <Gift className="w-8 h-8 animate-bounce" />
                </div>
                <span className="text-xs text-slate-500 font-bold mt-2">Unit Bonus Chest</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
