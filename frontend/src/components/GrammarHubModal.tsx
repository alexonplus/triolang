import React, { useState, useEffect } from 'react';
import {
  X,
  BookOpen,
  Volume2,
  Sparkles,
  CheckCircle2,
  AlertTriangle,
  Play,
  Loader2,
  ArrowRight,
  Layers,
  Award,
  RotateCcw,
  Flame,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { api } from '../services/api';
import { speakText, soundEffects } from '../services/audio';
import type {
  GrammarTopicSummary,
  GrammarTopicDetail,
  GrammarExerciseItem,
} from '../types';

interface GrammarHubModalProps {
  initialLanguage?: 'sv' | 'en';
  onClose: () => void;
}

const CEFR_LEVELS = ['ALL', 'A1', 'A2', 'B1', 'B2', 'C1'] as const;

export const GrammarHubModal: React.FC<GrammarHubModalProps> = ({
  initialLanguage = 'sv',
  onClose,
}) => {
  const [selectedLanguage, setSelectedLanguage] = useState<'sv' | 'en'>(initialLanguage);
  const [selectedLevel, setSelectedLevel] = useState<string>('ALL');
  const [topics, setTopics] = useState<GrammarTopicSummary[]>([]);
  const [selectedTopicId, setSelectedTopicId] = useState<string | null>(null);
  const [activeTopicDetail, setActiveTopicDetail] = useState<GrammarTopicDetail | null>(null);

  const [isLoadingTopics, setIsLoadingTopics] = useState(false);
  const [isLoadingDetail, setIsLoadingDetail] = useState(false);

  // Drill practice state
  const [isDrillMode, setIsDrillMode] = useState(false);
  const [drillExercises, setDrillExercises] = useState<GrammarExerciseItem[]>([]);
  const [currentDrillIndex, setCurrentDrillIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [drillAnswerSubmitted, setDrillAnswerSubmitted] = useState(false);
  const [isGeneratingAIDrills, setIsGeneratingAIDrills] = useState(false);
  const [correctAnswersCount, setCorrectAnswersCount] = useState(0);
  const [isDrillCompleted, setIsDrillCompleted] = useState(false);

  // Load topics list when language or level changes
  useEffect(() => {
    const loadTopics = async () => {
      try {
        setIsLoadingTopics(true);
        const levelParam = selectedLevel === 'ALL' ? undefined : selectedLevel;
        const data = await api.getGrammarTopics(selectedLanguage, levelParam);
        setTopics(data);

        if (data.length > 0 && (!selectedTopicId || !data.some((t) => t.id === selectedTopicId))) {
          setSelectedTopicId(data[0].id);
        }
      } catch (err) {
        console.error('Failed to load grammar topics:', err);
      } finally {
        setIsLoadingTopics(false);
      }
    };
    loadTopics();
  }, [selectedLanguage, selectedLevel]);

  // Load selected topic detail
  useEffect(() => {
    if (!selectedTopicId) return;

    const loadDetail = async () => {
      try {
        setIsLoadingDetail(true);
        setIsDrillMode(false);
        setIsDrillCompleted(false);
        const detail = await api.getGrammarTopicDetail(selectedTopicId);
        setActiveTopicDetail(detail);
      } catch (err) {
        console.error('Failed to load topic detail:', err);
      } finally {
        setIsLoadingDetail(false);
      }
    };
    loadDetail();
  }, [selectedTopicId]);

  const handleStartDrill = async (useAi: boolean = false) => {
    if (!selectedTopicId) return;
    try {
      soundEffects.playClickSound();
      if (useAi) {
        setIsGeneratingAIDrills(true);
        const res = await api.generateGrammarAIDrills(selectedTopicId);
        setDrillExercises(res.exercises);
      } else {
        const res = await api.getGrammarPracticeDrills(selectedTopicId);
        setDrillExercises(res.exercises);
      }

      setCurrentDrillIndex(0);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
      setCorrectAnswersCount(0);
      setIsDrillCompleted(false);
      setIsDrillMode(true);
    } catch (err) {
      console.error('Failed to fetch drills:', err);
    } finally {
      setIsGeneratingAIDrills(false);
    }
  };

  const handleSelectDrillOption = (option: string) => {
    if (drillAnswerSubmitted) return;
    soundEffects.playClickSound();
    setSelectedOption(option);
  };

  const handleSubmitDrillAnswer = () => {
    if (!selectedOption || !currentExercise || drillAnswerSubmitted) return;

    const isCorrect =
      selectedOption.trim().toLowerCase() === currentExercise.correct_answer.trim().toLowerCase();

    if (isCorrect) {
      soundEffects.playCorrectSound();
      setCorrectAnswersCount((prev) => prev + 1);
    } else {
      soundEffects.playIncorrectSound();
    }

    setDrillAnswerSubmitted(true);
  };

  const handleNextDrill = () => {
    soundEffects.playClickSound();
    if (currentDrillIndex + 1 < drillExercises.length) {
      setCurrentDrillIndex((prev) => prev + 1);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
    } else {
      soundEffects.playVictorySound();
      try {
        confetti({
          particleCount: 70,
          spread: 60,
          origin: { y: 0.6 },
        });
      } catch {
        // Confetti fallback
      }
      setIsDrillCompleted(true);
    }
  };

  const currentExercise = drillExercises[currentDrillIndex];
  const drillProgressPercent = drillExercises.length > 0 ? ((currentDrillIndex + 1) / drillExercises.length) * 100 : 0;
  const accuracyPercentage = drillExercises.length > 0 ? Math.round((correctAnswersCount / drillExercises.length) * 100) : 100;

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl max-w-5xl w-full h-[90vh] flex flex-col shadow-[0_16px_48px_rgba(45,35,25,0.15)] overflow-hidden">
        
        {/* Top Header */}
        <div className="p-4 bg-[#FFFFFF] border-b border-[#E5DDD0] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-[#2D5A3F] text-white flex items-center justify-center shadow-[0_2px_0_#1E3D2B] border border-[#1E3D2B]">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-lg flex items-center gap-2">
                <span>Grammatikstudio</span>
                <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#EBF3ED] text-[#2D5A3F] border border-[#D1E5D7]">
                  CEFR A1–C1
                </span>
              </h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                Strukturerade regler, mönsterformler och fördjupande övningspass
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Switcher */}
            <div className="flex bg-[#F5EFEB] p-1 rounded-xl border border-[#DDD4C6]">
              <button
                onClick={() => {
                  soundEffects.playClickSound();
                  setSelectedLanguage('sv');
                }}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition ${
                  selectedLanguage === 'sv'
                    ? 'bg-[#FFFFFF] text-[#24221F] shadow-[0_1px_2px_rgba(0,0,0,0.05)] border border-[#DDD4C6]'
                    : 'text-[#8F877B] hover:text-[#24221F]'
                }`}
              >
                <span>🇸🇪</span>
                <span>Svenska</span>
              </button>
              <button
                onClick={() => {
                  soundEffects.playClickSound();
                  setSelectedLanguage('en');
                }}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition ${
                  selectedLanguage === 'en'
                    ? 'bg-[#FFFFFF] text-[#24221F] shadow-[0_1px_2px_rgba(0,0,0,0.05)] border border-[#DDD4C6]'
                    : 'text-[#8F877B] hover:text-[#24221F]'
                }`}
              >
                <span>🇬🇧</span>
                <span>English</span>
              </button>
            </div>

            <button
              onClick={onClose}
              className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Level Selector Tabs */}
        <div className="px-4 py-2 bg-[#F5EFEB] border-b border-[#E5DDD0] flex items-center gap-2 overflow-x-auto">
          <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase tracking-wider mr-1">Nivå:</span>
          {CEFR_LEVELS.map((level) => (
            <button
              key={level}
              onClick={() => {
                soundEffects.playClickSound();
                setSelectedLevel(level);
              }}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition ${
                selectedLevel === level
                  ? 'bg-[#24221F] text-[#FAF7F2] shadow-sm'
                  : 'bg-[#FFFFFF] text-[#5C564E] hover:bg-[#FAF7F2] border border-[#DDD4C6]'
              }`}
            >
              {level}
            </button>
          ))}
        </div>

        {/* Main Content Body */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* Left Sidebar: Topics list */}
          <div className="w-72 md:w-80 border-r border-[#E5DDD0] bg-[#FAF7F2] overflow-y-auto p-3 space-y-2">
            {isLoadingTopics ? (
              <div className="p-8 flex flex-col items-center justify-center space-y-2 text-[#8F877B] text-xs">
                <Loader2 className="w-5 h-5 animate-spin text-[#2D5A3F]" />
                <span className="font-editorial italic">Hämtar grammatikavsnitt...</span>
              </div>
            ) : topics.length === 0 ? (
              <div className="p-6 text-center text-xs text-[#8F877B] font-editorial italic">
                Inga regler hittades för denna nivå.
              </div>
            ) : (
              topics.map((t) => (
                <button
                  key={t.id}
                  onClick={() => {
                    soundEffects.playClickSound();
                    setSelectedTopicId(t.id);
                  }}
                  className={`w-full text-left p-3.5 rounded-2xl border transition flex flex-col gap-1 ${
                    selectedTopicId === t.id
                      ? 'bg-[#FFFFFF] border-[#2D5A3F] text-[#24221F] shadow-[0_2px_0_#2D5A3F]'
                      : 'bg-[#FFFFFF] border-[#E5DDD0] text-[#5C564E] hover:bg-[#FAF7F2] hover:border-[#24221F]'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#F5EFEB] text-[#24221F] uppercase border border-[#DDD4C6]">
                      {t.level}
                    </span>
                    <span className="text-[10px] font-mono-tag text-[#2D5A3F]">
                      10 Övningar
                    </span>
                  </div>
                  <div className="font-bold text-xs line-clamp-1 mt-1 font-display text-[#24221F]">{t.title}</div>
                  <div className="text-[11px] text-[#8F877B] line-clamp-2 leading-tight">
                    {t.summary}
                  </div>
                </button>
              ))
            )}
          </div>

          {/* Right Pane: Topic Detail & Rule Explanation OR Practice Drills */}
          <div className="flex-1 overflow-y-auto p-6 bg-[#FFFFFF]">
            {isLoadingDetail ? (
              <div className="h-full flex flex-col items-center justify-center space-y-3">
                <Loader2 className="w-6 h-6 animate-spin text-[#2D5A3F]" />
                <span className="text-[#8F877B] text-xs font-editorial italic">Öppnar grammatikregel...</span>
              </div>
            ) : isDrillMode ? (
              /* --- Drill Mode: Finished or Active --- */
              isDrillCompleted ? (
                /* Celebration Summary */
                <div className="max-w-md mx-auto py-8 text-center space-y-6 animate-in zoom-in-95">
                  <div className="w-18 h-18 mx-auto rounded-3xl bg-[#EBF3ED] border-2 border-[#2D5A3F] flex items-center justify-center text-[#2D5A3F] shadow-[0_4px_0_#2D5A3F]">
                    <Award className="w-9 h-9" />
                  </div>

                  <div className="space-y-1.5">
                    <h2 className="text-2xl font-bold font-display text-[#24221F]">Övningspasset slutfört!</h2>
                    <p className="text-xs text-[#5C564E] font-editorial italic">
                      Du övade på <span className="text-[#2D5A3F] font-bold">{activeTopicDetail?.title}</span>
                    </p>
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    <div className="p-4 bg-[#FAF7F2] rounded-2xl border border-[#DDD4C6]">
                      <div className="text-[10px] text-[#8F877B] font-mono-tag uppercase">Träffsäkerhet</div>
                      <div className="text-2xl font-bold font-display text-[#2D5A3F] mt-1">{accuracyPercentage}%</div>
                      <div className="text-[11px] text-[#8F877B] mt-0.5">{correctAnswersCount} av {drillExercises.length} rätt</div>
                    </div>
                    <div className="p-4 bg-[#FAF7F2] rounded-2xl border border-[#DDD4C6]">
                      <div className="text-[10px] text-[#8F877B] font-mono-tag uppercase">Erfarenhetspoäng</div>
                      <div className="text-2xl font-bold font-display text-[#C9862C] mt-1">+{correctAnswersCount * 10} XP</div>
                      <div className="text-[11px] text-[#8F877B] mt-0.5">Grammatikbehärskning</div>
                    </div>
                  </div>

                  <div className="space-y-2.5 pt-2">
                    <button
                      onClick={() => handleStartDrill(false)}
                      className="w-full py-3.5 btn-craft btn-stamp-forest flex items-center justify-center gap-2 text-xs font-bold"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>Öva igen</span>
                    </button>

                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="w-full py-3 bg-[#FAF7F2] hover:bg-[#F5EFEB] text-[#5C564E] border border-[#DDD4C6] rounded-2xl text-xs font-bold transition"
                    >
                      Tillbaka till regelteorin
                    </button>
                  </div>
                </div>
              ) : currentExercise ? (
                /* Active Drill Question View */
                <div className="max-w-xl mx-auto space-y-5 animate-in fade-in">
                  
                  {/* Progress Header */}
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-[#C9862C] flex items-center gap-1.5 font-mono-tag">
                        <Flame className="w-4 h-4 fill-[#C9862C]" />
                        <span>Fråga {currentDrillIndex + 1} av {drillExercises.length}</span>
                      </span>
                      <span className="text-[#8F877B] font-mono-tag text-xs">
                        Poäng: {correctAnswersCount} rätt
                      </span>
                    </div>

                    <div className="h-2.5 bg-[#EBE4D8] rounded-full overflow-hidden border border-[#DDD4C6]">
                      <div
                        className="h-full bg-[#2D5A3F] transition-all duration-300"
                        style={{ width: `${drillProgressPercent}%` }}
                      />
                    </div>
                  </div>

                  {/* Question Card */}
                  <div className="bg-[#FAF7F2] border border-[#DDD4C6] p-6 rounded-3xl space-y-5 shadow-[0_2px_0_#EADFCF]">
                    <div className="text-base sm:text-lg font-bold font-display text-[#24221F] leading-relaxed">
                      {currentExercise.prompt}
                    </div>

                    {/* Options */}
                    <div className="space-y-2.5">
                      {currentExercise.options?.map((opt, idx) => {
                        const isSelected = selectedOption === opt;
                        const isCorrect = opt.trim().toLowerCase() === currentExercise.correct_answer.trim().toLowerCase();

                        let btnStyle = 'bg-[#FFFFFF] border-[#DDD4C6] text-[#24221F] hover:bg-[#FAF7F2] hover:border-[#24221F] shadow-[0_2px_0_#DDD4C6]';
                        if (drillAnswerSubmitted) {
                          if (isCorrect) {
                            btnStyle = 'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] font-bold shadow-[0_2px_0_#2D5A3F]';
                          } else if (isSelected) {
                            btnStyle = 'bg-[#FAECE8] border-[#B34B32] text-[#8A321E] font-bold shadow-[0_2px_0_#B34B32]';
                          }
                        } else if (isSelected) {
                          btnStyle = 'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] font-bold shadow-[0_2px_0_#2D5A3F]';
                        }

                        return (
                          <button
                            key={idx}
                            onClick={() => handleSelectDrillOption(opt)}
                            disabled={drillAnswerSubmitted}
                            className={`w-full text-left p-3.5 rounded-2xl border transition flex items-center justify-between text-xs sm:text-sm ${btnStyle}`}
                          >
                            <span>{opt}</span>
                            {drillAnswerSubmitted && isCorrect && (
                              <CheckCircle2 className="w-4 h-4 text-[#2D5A3F]" />
                            )}
                          </button>
                        );
                      })}
                    </div>

                    {/* Explanation feedback */}
                    {drillAnswerSubmitted && (
                      <div className="p-4 bg-[#FFFFFF] rounded-2xl border border-[#DDD4C6] space-y-1.5 animate-in fade-in">
                        <div className="text-xs font-bold text-[#2D5A3F] flex items-center gap-1.5 font-mono-tag">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Grammatisk förklaring:</span>
                        </div>
                        <p className="text-xs text-[#5C564E] leading-relaxed font-sans">
                          {currentExercise.explanation}
                        </p>
                      </div>
                    )}

                    {/* Action Button */}
                    {!drillAnswerSubmitted ? (
                      <button
                        onClick={handleSubmitDrillAnswer}
                        disabled={!selectedOption}
                        className="w-full py-3.5 btn-craft btn-stamp-forest disabled:opacity-50 text-xs font-bold"
                      >
                        Kontrollera svar
                      </button>
                    ) : (
                      <button
                        onClick={handleNextDrill}
                        className="w-full py-3.5 btn-craft btn-stamp-dark flex items-center justify-center gap-2 text-xs font-bold"
                      >
                        <span>
                          {currentDrillIndex + 1 < drillExercises.length ? 'Nästa fråga' : 'Slutför övning'}
                        </span>
                        <ArrowRight className="w-4 h-4" />
                      </button>
                    )}
                  </div>

                  <div className="text-center">
                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="text-xs text-[#8F877B] hover:text-[#24221F] underline font-editorial"
                    >
                      Avsluta övning och gå tillbaka till teorin
                    </button>
                  </div>

                </div>
              ) : null
            ) : activeTopicDetail ? (
              /* --- Topic Detail / Theory Breakdown View (Artisanal Linguistic Sheet) --- */
              <div className="max-w-3xl mx-auto space-y-6">
                
                {/* Header Title & Badges */}
                <div className="space-y-1.5">
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-0.5 rounded-md bg-[#FDF6EA] border border-[#F3E2C4] text-[#995E15] font-mono-tag text-xs">
                      CEFR {activeTopicDetail.level}
                    </span>
                    <span className="text-xs font-semibold text-[#8F877B] font-editorial italic">
                      {activeTopicDetail.swedish_title}
                    </span>
                  </div>
                  <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F]">{activeTopicDetail.title}</h2>
                  <p className="text-xs sm:text-sm text-[#5C564E] font-sans">{activeTopicDetail.summary}</p>
                </div>

                {/* Formula Highlight Banner (Linocut card) */}
                <div className="p-4 bg-[#F5EFEB] border border-[#DDD4C6] rounded-2xl flex items-center gap-3.5 shadow-[0_2px_0_#DDD4C6]">
                  <div className="p-2.5 bg-[#FFFFFF] rounded-xl text-[#2B5876] border border-[#DDD4C6]">
                    <Sparkles className="w-4 h-4 text-[#C9862C]" />
                  </div>
                  <div>
                    <div className="text-[10px] font-mono-tag uppercase text-[#8F877B]">
                      Grammatisk mönsterformel
                    </div>
                    <div className="text-xs sm:text-sm font-mono font-bold text-[#24221F] mt-0.5">
                      {activeTopicDetail.formula}
                    </div>
                  </div>
                </div>

                {/* Rule Explanation */}
                <div className="space-y-2">
                  <h4 className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                    <Layers className="w-3.5 h-3.5 text-[#2D5A3F]" />
                    <span>Regelgenomgång & Struktur:</span>
                  </h4>
                  <div className="bg-[#FAF7F2] border border-[#DDD4C6] p-5 rounded-2xl text-xs sm:text-sm text-[#24221F] leading-relaxed whitespace-pre-line font-sans">
                    {activeTopicDetail.rule_explanation}
                  </div>
                </div>

                {/* Examples with Audio */}
                {activeTopicDetail.examples.length > 0 && (
                  <div className="space-y-2.5">
                    <h4 className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                      <Volume2 className="w-3.5 h-3.5 text-[#2B5876]" />
                      <span>Konkreta exempel med uttal:</span>
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {activeTopicDetail.examples.map((ex, idx) => (
                        <div
                          key={idx}
                          className="p-3.5 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl space-y-1 hover:border-[#24221F] transition"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-bold text-sm text-[#24221F] font-editorial">{ex.swedish}</span>
                            <button
                              onClick={() => speakText(ex.swedish, selectedLanguage)}
                              title="Spela upp ljud"
                              className="p-1 text-[#8F877B] hover:text-[#24221F] rounded-lg transition"
                            >
                              <Volume2 className="w-3.5 h-3.5" />
                            </button>
                          </div>
                          <div className="text-xs text-[#5C564E]">{ex.english}</div>
                          {ex.target_highlight && (
                            <span className="inline-block text-[10px] px-1.5 py-0.5 rounded bg-[#FFFFFF] text-[#2B5876] border border-[#DDD4C6] font-mono-tag">
                              Nyckel: {ex.target_highlight}
                            </span>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Common Pitfalls / Traps */}
                {activeTopicDetail.common_pitfalls.length > 0 && (
                  <div className="p-4 bg-[#FAECE8] border border-[#F6D3C8] rounded-2xl space-y-1.5">
                    <div className="flex items-center gap-1.5 text-[#B34B32] font-bold text-xs font-mono-tag">
                      <AlertTriangle className="w-3.5 h-3.5" />
                      <span>Vanliga fallgropar & misstag:</span>
                    </div>
                    <ul className="space-y-1 text-xs text-[#632415]">
                      {activeTopicDetail.common_pitfalls.map((pitfall, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-[#B34B32] font-bold">•</span>
                          <span>{pitfall}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Practice Actions Bar */}
                <div className="pt-2 flex flex-col sm:flex-row gap-3">
                  <button
                    onClick={() => handleStartDrill(false)}
                    className="flex-1 py-3.5 btn-craft btn-stamp-forest flex items-center justify-center gap-2 text-xs font-bold"
                  >
                    <Play className="w-4 h-4 fill-white" />
                    <span>Starta övningspass ({activeTopicDetail.exercises_count} frågor)</span>
                  </button>

                  <button
                    onClick={() => handleStartDrill(true)}
                    disabled={isGeneratingAIDrills}
                    className="py-3.5 px-5 btn-craft btn-stamp-paper flex items-center justify-center gap-2 text-xs font-bold disabled:opacity-50"
                  >
                    {isGeneratingAIDrills ? (
                      <Loader2 className="w-4 h-4 animate-spin text-[#C9862C]" />
                    ) : (
                      <Sparkles className="w-4 h-4 text-[#C9862C]" />
                    )}
                    <span>Generera fler AI-övningar</span>
                  </button>
                </div>

              </div>
            ) : null}
          </div>

        </div>

      </div>
    </div>
  );
};
