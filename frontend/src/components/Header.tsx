import { Flame, Heart, Gem, Bot, RefreshCw, Target, BookOpen } from 'lucide-react';
import type { Course, UserStats } from '../types';
import { soundEffects } from '../services/audio';

interface HeaderProps {
  user: UserStats | null;
  courses: Course[];
  currentCourseId: string;
  onSelectCourse: (courseId: string) => void;
  onOpenAITutor: () => void;
  onOpenPlacementTest?: () => void;
  onOpenGrammar?: () => void;
  onRefillHearts: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  user,
  courses,
  currentCourseId,
  onSelectCourse,
  onOpenAITutor,
  onOpenPlacementTest,
  onOpenGrammar,
  onRefillHearts,
}) => {
  const currentCourse = courses.find((c) => c.id === currentCourseId) || courses[0];

  return (
    <header className="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 py-3">
      <div className="max-w-5xl mx-auto flex items-center justify-between">
        
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2">
            <span className="text-2xl">🦉</span>
            <span className="text-xl font-black tracking-tight bg-gradient-to-r from-emerald-400 via-teal-300 to-sky-400 bg-clip-text text-transparent">
              TrioLang
            </span>
          </div>

          <div className="relative group">
            <button
              className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-xl transition text-sm font-bold text-slate-200"
              onClick={() => soundEffects.playClickSound()}
            >
              <span>{currentCourse?.flag_emoji || '🇸🇪'}</span>
              <span>{currentCourse?.native_title || 'Svenska'}</span>
            </button>

            <div className="absolute left-0 mt-2 w-48 bg-slate-800 border border-slate-700 rounded-xl shadow-xl py-1 hidden group-hover:block transition-all z-50">
              {courses.map((course) => (
                <button
                  key={course.id}
                  onClick={() => {
                    soundEffects.playClickSound();
                    onSelectCourse(course.id);
                  }}
                  className={`w-full text-left px-4 py-2.5 flex items-center gap-3 text-sm font-semibold transition ${
                    course.id === currentCourseId
                      ? 'bg-emerald-500/20 text-emerald-400 border-l-4 border-emerald-500'
                      : 'text-slate-300 hover:bg-slate-700'
                  }`}
                >
                  <span className="text-xl">{course.flag_emoji}</span>
                  <div>
                    <div className="font-bold">{course.native_title}</div>
                    <div className="text-xs text-slate-400">{course.title}</div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>

        <div className="flex items-center gap-3 md:gap-5">
          <div className="flex items-center gap-1.5 font-black text-amber-400 bg-amber-400/10 px-3 py-1.5 rounded-xl border border-amber-500/30">
            <Flame className="w-5 h-5 fill-amber-400 animate-pulse" />
            <span>{user?.streak_days || 1}</span>
          </div>

          <div className="flex items-center gap-1.5 font-black text-cyan-400 bg-cyan-400/10 px-3 py-1.5 rounded-xl border border-cyan-500/30">
            <Gem className="w-5 h-5 fill-cyan-400" />
            <span>{user?.gems || 0}</span>
          </div>

          <div className="flex items-center gap-2 font-black text-rose-400 bg-rose-400/10 px-3 py-1.5 rounded-xl border border-rose-500/30">
            <Heart className={`w-5 h-5 ${user?.hearts ? 'fill-rose-500' : 'text-slate-500'}`} />
            <span>{user?.hearts ?? 5}</span>
            {(user?.hearts ?? 5) < 5 && (
              <button
                onClick={onRefillHearts}
                title="Refill Hearts (+5)"
                className="text-xs bg-rose-500 text-white rounded-md p-1 hover:bg-rose-400 transition"
              >
                <RefreshCw className="w-3 h-3" />
              </button>
            )}
          </div>

          {onOpenGrammar && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenGrammar();
              }}
              title="Grammar Hub (CEFR Rules & Drills)"
              className="flex items-center gap-1.5 px-3 py-1.5 btn-3d bg-sky-600 hover:bg-sky-500 text-white font-black rounded-xl shadow-[0_3px_0_#0369a1] text-sm"
            >
              <BookOpen className="w-4 h-4 text-sky-200" />
              <span className="hidden sm:inline">Grammar</span>
            </button>
          )}

          {onOpenPlacementTest && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenPlacementTest();
              }}
              title="Take AI Diagnostic Placement Test"
              className="flex items-center gap-1.5 px-3 py-1.5 btn-3d bg-amber-500 hover:bg-amber-400 text-slate-950 font-black rounded-xl shadow-[0_3px_0_#b45309] text-sm"
            >
              <Target className="w-4 h-4" />
              <span className="hidden sm:inline">Level Test</span>
            </button>
          )}

          <button
            onClick={() => {
              soundEffects.playClickSound();
              onOpenAITutor();
            }}
            className="flex items-center gap-1.5 px-3.5 py-1.5 btn-3d bg-indigo-600 hover:bg-indigo-500 text-white font-bold rounded-xl shadow-[0_3px_0_#3730a3] text-sm"
          >
            <Bot className="w-4 h-4 text-indigo-200" />
            <span className="hidden sm:inline">TrioBot AI</span>
          </button>
        </div>

      </div>
    </header>
  );
};
