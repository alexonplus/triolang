import React from 'react';
import { Flame, Heart, Gem, Bot, RefreshCw, Target, BookOpen, Clock, MessageSquare, Volume2, ChevronDown } from 'lucide-react';
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
  onOpenTenses?: () => void;
  onOpenDialogue?: () => void;
  onOpenPronunciation?: () => void;
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
  onOpenTenses,
  onOpenDialogue,
  onOpenPronunciation,
  onRefillHearts,
}) => {
  const currentCourse = courses.find((c) => c.id === currentCourseId) || courses[0];

  return (
    <header className="sticky top-0 z-40 bg-[#FAF7F2]/95 backdrop-blur-md border-b border-[#E5DDD0] shadow-[0_1px_3px_rgba(45,35,25,0.04)] px-4 py-3 transition-colors">
      <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
        
        {/* Brand & Language Selector */}
        <div className="flex items-center gap-3 md:gap-5">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-[#24221F] text-[#FAF7F2] flex items-center justify-center text-lg shadow-[0_2px_0_#141312] border border-[#141312]">
              🦉
            </div>
            <div>
              <span className="text-xl font-black tracking-tight font-display text-[#24221F] block leading-none">
                TrioLang
              </span>
              <span className="text-[10px] font-mono-tag text-[#8F877B] tracking-wider uppercase">
                Hantverk & Språkstudio
              </span>
            </div>
          </div>

          <div className="relative group">
            <button
              className="flex items-center gap-2 px-3 py-1.5 bg-[#FFFFFF] hover:bg-[#F5EFEB] border border-[#DDD4C6] rounded-xl transition text-xs font-bold text-[#24221F] shadow-[0_2px_0_#DDD4C6]"
              onClick={() => soundEffects.playClickSound()}
            >
              <span className="text-base">{currentCourse?.flag_emoji || '🇸🇪'}</span>
              <span className="font-editorial text-sm font-semibold">{currentCourse?.native_title || 'Svenska'}</span>
              <ChevronDown className="w-3 h-3 text-[#8F877B]" />
            </button>

            <div className="absolute left-0 mt-2 w-52 bg-[#FFFFFF] border border-[#DDD4C6] rounded-2xl shadow-[0_8px_24px_rgba(45,35,25,0.08)] py-1.5 hidden group-hover:block transition-all z-50">
              <div className="px-3 py-1 text-[10px] font-mono-tag text-[#8F877B] uppercase border-b border-[#EDE7DD] mb-1">
                Välj studiekurs
              </div>
              {courses.map((course) => (
                <button
                  key={course.id}
                  onClick={() => {
                    soundEffects.playClickSound();
                    onSelectCourse(course.id);
                  }}
                  className={`w-full text-left px-3.5 py-2 flex items-center gap-3 text-xs font-semibold transition ${
                    course.id === currentCourseId
                      ? 'bg-[#EBF3ED] text-[#2D5A3F] border-l-3 border-[#2D5A3F]'
                      : 'text-[#5C564E] hover:bg-[#F8F4EC]'
                  }`}
                >
                  <span className="text-lg">{course.flag_emoji}</span>
                  <div>
                    <div className="font-bold text-[#24221F] font-editorial text-sm">{course.native_title}</div>
                    <div className="text-[10px] text-[#8F877B]">{course.title}</div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Stats & Navigation Atelier Buttons */}
        <div className="flex items-center gap-2 sm:gap-3 flex-wrap justify-end">
          
          {/* Streak Tag */}
          <div className="flex items-center gap-1.5 font-bold text-xs text-[#995E15] bg-[#FDF6EA] px-2.5 py-1.5 rounded-xl border border-[#F3E2C4] shadow-[0_1px_0_#EAD6B4]">
            <Flame className="w-4 h-4 text-[#C9862C] fill-[#C9862C]" />
            <span>{user?.streak_days || 1} d</span>
          </div>

          {/* Gems Tag */}
          <div className="flex items-center gap-1.5 font-bold text-xs text-[#204961] bg-[#EEF5F9] px-2.5 py-1.5 rounded-xl border border-[#D5E5EE] shadow-[0_1px_0_#C5D8E3]">
            <Gem className="w-4 h-4 text-[#2B5876] fill-[#2B5876]" />
            <span>{user?.gems || 0}</span>
          </div>

          {/* Hearts Tag */}
          <div className="flex items-center gap-1.5 font-bold text-xs text-[#8A321E] bg-[#FCF0EC] px-2.5 py-1.5 rounded-xl border border-[#F6D3C8] shadow-[0_1px_0_#EBC1B4]">
            <Heart className={`w-4 h-4 ${user?.hearts ? 'fill-[#B34B32] text-[#B34B32]' : 'text-[#C5BBAE]'}`} />
            <span>{user?.hearts ?? 5}</span>
            {(user?.hearts ?? 5) < 5 && (
              <button
                onClick={onRefillHearts}
                title="Fyll på hjärtan (+5)"
                className="text-xs bg-[#B34B32] text-white rounded-md p-1 hover:bg-[#C6573C] transition"
              >
                <RefreshCw className="w-3 h-3" />
              </button>
            )}
          </div>

          <div className="h-5 w-[1px] bg-[#E5DDD0] hidden md:block mx-1" />

          {/* Dialogue Button */}
          {onOpenDialogue && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenDialogue();
              }}
              title="Samtalslabb & Dialogrollspel"
              className="btn-craft px-3 py-1.5 text-xs bg-[#FFFFFF] hover:bg-[#F7F3EC] text-[#24221F] border border-[#DDD4C6] shadow-[0_2.5px_0_#DDD4C6]"
            >
              <MessageSquare className="w-3.5 h-3.5 text-[#2B5876] mr-1.5" />
              <span className="font-bold">Samtal</span>
            </button>
          )}

          {/* Tenses Button */}
          {onOpenTenses && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenTenses();
              }}
              title="Tidsformer & Tempuslabb"
              className="btn-craft px-3 py-1.5 text-xs bg-[#FFFFFF] hover:bg-[#F7F3EC] text-[#24221F] border border-[#DDD4C6] shadow-[0_2.5px_0_#DDD4C6]"
            >
              <Clock className="w-3.5 h-3.5 text-[#C9862C] mr-1.5" />
              <span className="font-bold">Tempus</span>
            </button>
          )}

          {/* Grammar Button */}
          {onOpenGrammar && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenGrammar();
              }}
              title="Grammatikstudio & Regler"
              className="btn-craft px-3 py-1.5 text-xs bg-[#FFFFFF] hover:bg-[#F7F3EC] text-[#24221F] border border-[#DDD4C6] shadow-[0_2.5px_0_#DDD4C6]"
            >
              <BookOpen className="w-3.5 h-3.5 text-[#2D5A3F] mr-1.5" />
              <span className="font-bold">Grammatik</span>
            </button>
          )}

          {/* Level Test Button */}
          {onOpenPlacementTest && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenPlacementTest();
              }}
              title="Diagnostiskt nivåtest"
              className="btn-craft px-3 py-1.5 text-xs bg-[#FFFFFF] hover:bg-[#F7F3EC] text-[#24221F] border border-[#DDD4C6] shadow-[0_2.5px_0_#DDD4C6]"
            >
              <Target className="w-3.5 h-3.5 text-[#8A321E] mr-1.5" />
              <span className="font-bold">Nivåtest</span>
            </button>
          )}

          {/* Pronunciation Button */}
          {onOpenPronunciation && (
            <button
              onClick={() => {
                soundEffects.playClickSound();
                onOpenPronunciation();
              }}
              title="Uttalsstudio & Fonetiklabb"
              className="btn-craft px-3 py-1.5 text-xs bg-[#FFFFFF] hover:bg-[#F7F3EC] text-[#24221F] border border-[#DDD4C6] shadow-[0_2.5px_0_#DDD4C6]"
            >
              <Volume2 className="w-3.5 h-3.5 text-[#5C564E] mr-1.5" />
              <span className="font-bold">Uttal</span>
            </button>
          )}

          {/* TrioBot AI Button */}
          <button
            onClick={() => {
              soundEffects.playClickSound();
              onOpenAITutor();
            }}
            className="btn-craft px-3.5 py-1.5 text-xs bg-[#24221F] hover:bg-[#383430] text-[#FAF7F2] border border-[#141312] shadow-[0_2.5px_0_#141312]"
          >
            <Bot className="w-3.5 h-3.5 text-[#D4CABE] mr-1.5" />
            <span className="font-bold">TrioBot</span>
          </button>
        </div>

      </div>
    </header>
  );
};
