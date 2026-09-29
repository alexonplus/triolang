import React, { useState, useEffect } from 'react';
import {
  X,
  Clock,
  Sparkles,
  Volume2,
  CheckCircle2,
  AlertTriangle,
  Play,
  Loader2,
  ArrowRight,
  Brain,
  RotateCcw,
  Award,
  Zap,
  Tag,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { api } from '../services/api';
import { speakText, soundEffects } from '../services/audio';
import type {
  TenseSummary,
  TenseDetail,
  TenseExerciseItem,
  AIMemoryProfileResponse,
} from '../types';

interface TensesMasteryModalProps {
  initialLanguage?: 'en' | 'sv';
  onClose: () => void;
}

const TIME_ASPECTS = ['all', 'past', 'present', 'future'] as const;

export const TensesMasteryModal: React.FC<TensesMasteryModalProps> = ({
  initialLanguage = 'en',
  onClose,
}) => {
  const [selectedLanguage, setSelectedLanguage] = useState<'en' | 'sv'>(initialLanguage);
  const [selectedAspect, setSelectedAspect] = useState<string>('all');
  const [tenses, setTenses] = useState<TenseSummary[]>([]);
  const [selectedTenseId, setSelectedTenseId] = useState<string | null>(null);
  const [activeTenseDetail, setActiveTenseDetail] = useState<TenseDetail | null>(null);
  const [aiMemoryProfile, setAiMemoryProfile] = useState<AIMemoryProfileResponse | null>(null);

  const [isLoadingTenses, setIsLoadingTenses] = useState(false);
  const [isLoadingDetail, setIsLoadingDetail] = useState(false);

  // Drill session state
  const [isDrillMode, setIsDrillMode] = useState(false);
  const [drillExercises, setDrillExercises] = useState<TenseExerciseItem[]>([]);
  const [currentDrillIndex, setCurrentDrillIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [drillAnswerSubmitted, setDrillAnswerSubmitted] = useState(false);
  const [correctAnswersCount, setCorrectAnswersCount] = useState(0);
  const [isDrillCompleted, setIsDrillCompleted] = useState(false);
  const [lastAiFeedback, setLastAiFeedback] = useState<string | null>(null);

  // Load AI memory profile
  const refreshMemoryProfile = async () => {
    try {
      const profile = await api.getAIMemoryProfile();
      setAiMemoryProfile(profile);
    } catch (err) {
      console.error('Failed to load AI memory profile:', err);
    }
  };

  useEffect(() => {
    refreshMemoryProfile();
  }, []);

  // Load tenses list
  useEffect(() => {
    const loadTenses = async () => {
      try {
        setIsLoadingTenses(true);
        const data = await api.getTenses(selectedLanguage, selectedAspect);
        setTenses(data);

        if (data.length > 0 && (!selectedTenseId || !data.some((t) => t.id === selectedTenseId))) {
          setSelectedTenseId(data[0].id);
        }
      } catch (err) {
        console.error('Failed to load tenses:', err);
      } finally {
        setIsLoadingTenses(false);
      }
    };
    loadTenses();
  }, [selectedLanguage, selectedAspect]);

  // Load active tense detail
  useEffect(() => {
    if (!selectedTenseId) return;

    const loadDetail = async () => {
      try {
        setIsLoadingDetail(true);
        setIsDrillMode(false);
        setIsDrillCompleted(false);
        const detail = await api.getTenseDetail(selectedTenseId);
        setActiveTenseDetail(detail);
      } catch (err) {
        console.error('Failed to load tense detail:', err);
      } finally {
        setIsLoadingDetail(false);
      }
    };
    loadDetail();
  }, [selectedTenseId]);

  const handleStartDrill = async () => {
    if (!selectedTenseId) return;
    try {
      soundEffects.playClickSound();
      const res = await api.getTenseDrills(selectedTenseId);
      setDrillExercises(res.exercises);
      setCurrentDrillIndex(0);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
      setCorrectAnswersCount(0);
      setIsDrillCompleted(false);
      setLastAiFeedback(null);
      setIsDrillMode(true);
    } catch (err) {
      console.error('Failed to load drills:', err);
    }
  };

  const handleSelectDrillOption = (option: string) => {
    if (drillAnswerSubmitted) return;
    soundEffects.playClickSound();
    setSelectedOption(option);
  };

  const handleSubmitDrillAnswer = async () => {
    if (!selectedOption || !currentExercise || drillAnswerSubmitted || !selectedTenseId) return;

    setDrillAnswerSubmitted(true);
    try {
      const res = await api.submitTenseDrill(selectedTenseId, currentExercise.id, selectedOption);
      setLastAiFeedback(res.ai_memory_feedback || null);

      if (res.is_correct) {
        setCorrectAnswersCount((prev) => prev + 1);
        soundEffects.playCorrectSound();
      } else {
        soundEffects.playIncorrectSound();
      }
      refreshMemoryProfile();
    } catch (err) {
      console.error('Failed to submit drill answer:', err);
    }
  };

  const handleNextDrill = () => {
    soundEffects.playClickSound();
    if (currentDrillIndex + 1 < drillExercises.length) {
      setCurrentDrillIndex((prev) => prev + 1);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
      setLastAiFeedback(null);
    } else {
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
            <div className="w-10 h-10 rounded-2xl bg-[#C9862C] text-white flex items-center justify-center shadow-[0_2px_0_#8C5917] border border-[#8C5917]">
              <Clock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-lg flex items-center gap-2">
                <span>Tidsformer & Tempuslabb</span>
                <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#FDF6EA] text-[#995E15] border border-[#F3E2C4]">
                  {selectedLanguage === 'en' ? 'Alla 12 tempus' : 'Fullständigt tidssystem'}
                </span>
              </h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                Tidslinjer, signalord och adaptiv AI-minnesanalys
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Switcher */}
            <div className="flex bg-[#F5EFEB] p-1 rounded-xl border border-[#DDD4C6]">
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
                <span>English (12)</span>
              </button>
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
            </div>

            <button
              onClick={onClose}
              className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* AI Memory Diagnostic Ribbon */}
        {aiMemoryProfile && (
          <div className="px-4 py-2 bg-[#F5EFEB] border-b border-[#E5DDD0] flex flex-wrap items-center justify-between gap-2 text-xs">
            <div className="flex items-center gap-2 text-[#24221F]">
              <Brain className="w-4 h-4 text-[#2B5876] shrink-0" />
              <span className="font-editorial italic">{aiMemoryProfile.ai_coaching_note}</span>
            </div>
            <div className="flex items-center gap-3 shrink-0">
              <div className="flex items-center gap-1 font-bold text-[#995E15] bg-[#FFFFFF] px-2 py-0.5 rounded-md border border-[#DDD4C6] font-mono-tag">
                <Zap className="w-3.5 h-3.5 text-[#C9862C]" />
                <span>Träffsäkerhet: {aiMemoryProfile.overall_accuracy}%</span>
              </div>
              {aiMemoryProfile.total_mistakes_logged > 0 && (
                <span className="text-[11px] text-[#8F877B] font-mono-tag">
                  {aiMemoryProfile.total_mistakes_logged} loggade minnen
                </span>
              )}
            </div>
          </div>
        )}

        {/* Time Aspect Filter Bar */}
        <div className="px-4 py-2 bg-[#FAF7F2] border-b border-[#E5DDD0] flex items-center gap-2 overflow-x-auto">
          <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase tracking-wider mr-1">Tidsaspekt:</span>
          {TIME_ASPECTS.map((aspect) => (
            <button
              key={aspect}
              onClick={() => {
                soundEffects.playClickSound();
                setSelectedAspect(aspect);
              }}
              className={`px-3 py-1 rounded-xl text-xs font-bold capitalize transition ${
                selectedAspect === aspect
                  ? 'bg-[#24221F] text-[#FAF7F2] shadow-sm'
                  : 'bg-[#FFFFFF] text-[#5C564E] hover:bg-[#F5EFEB] border border-[#DDD4C6]'
              }`}
            >
              {aspect === 'all' ? 'Alla' : aspect === 'past' ? 'Dåtid' : aspect === 'present' ? 'Nutid' : 'Framtid'}
            </button>
          ))}
        </div>

        {/* Main Content Body */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* Left Sidebar: Tenses Matrix */}
          <div className="w-72 md:w-80 border-r border-[#E5DDD0] bg-[#FAF7F2] overflow-y-auto p-3 space-y-2">
            {isLoadingTenses ? (
              <div className="p-8 flex flex-col items-center justify-center space-y-2 text-[#8F877B] text-xs">
                <Loader2 className="w-5 h-5 animate-spin text-[#C9862C]" />
                <span className="font-editorial italic">Hämtar tidsformer...</span>
              </div>
            ) : tenses.length === 0 ? (
              <div className="p-6 text-center text-xs text-[#8F877B] font-editorial italic">
                Inga tidsformer hittades för denna aspekt.
              </div>
            ) : (
              tenses.map((t) => {
                const isSelected = selectedTenseId === t.id;
                return (
                  <button
                    key={t.id}
                    onClick={() => {
                      soundEffects.playClickSound();
                      setSelectedTenseId(t.id);
                    }}
                    className={`w-full text-left p-3.5 rounded-2xl border transition flex flex-col gap-1.5 ${
                      isSelected
                        ? 'bg-[#FFFFFF] border-[#C9862C] text-[#24221F] shadow-[0_2px_0_#C9862C]'
                        : 'bg-[#FFFFFF] border-[#E5DDD0] text-[#5C564E] hover:bg-[#FAF7F2] hover:border-[#24221F]'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#F5EFEB] text-[#24221F] uppercase border border-[#DDD4C6]">
                        {t.time_aspect}
                      </span>
                      <span className="text-[10px] font-mono-tag text-[#2D5A3F]">
                        {t.mastery_percentage > 0 ? `${t.mastery_percentage}% Behärskning` : '10 Övningar'}
                      </span>
                    </div>
                    <div className="font-bold text-xs line-clamp-1 font-display text-[#24221F]">{t.title}</div>
                    <div className="text-[11px] text-[#8F877B] line-clamp-2 leading-tight">
                      {t.summary}
                    </div>
                  </button>
                );
              })
            )}
          </div>

          {/* Right Pane: Tense Breakdown or Interactive Drill Session */}
          <div className="flex-1 overflow-y-auto p-6 bg-[#FFFFFF]">
            {isLoadingDetail ? (
              <div className="h-full flex flex-col items-center justify-center space-y-3">
                <Loader2 className="w-6 h-6 animate-spin text-[#C9862C]" />
                <span className="text-[#8F877B] text-xs font-editorial italic">Laddar tidslinjestruktur...</span>
              </div>
            ) : isDrillMode ? (
              /* --- Drill Practice Mode --- */
              isDrillCompleted ? (
                /* Celebration Summary */
                <div className="max-w-md mx-auto py-8 text-center space-y-6 animate-in zoom-in-95">
                  <div className="w-18 h-18 mx-auto rounded-3xl bg-[#FDF6EA] border-2 border-[#C9862C] flex items-center justify-center text-[#C9862C] shadow-[0_4px_0_#C9862C]">
                    <Award className="w-9 h-9" />
                  </div>

                  <div className="space-y-1.5">
                    <h2 className="text-2xl font-bold font-display text-[#24221F]">Övningspasset är klart!</h2>
                    <p className="text-xs text-[#5C564E] font-editorial italic">
                      AI-minnet har uppdaterats för <span className="text-[#C9862C] font-bold">{activeTenseDetail?.title}</span>
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
                      <div className="text-[11px] text-[#8F877B] mt-0.5">Tempusbehärskning</div>
                    </div>
                  </div>

                  <div className="space-y-2.5 pt-2">
                    <button
                      onClick={handleStartDrill}
                      className="w-full py-3.5 btn-craft btn-stamp-ochre flex items-center justify-center gap-2 text-xs font-bold"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>Öva igen</span>
                    </button>

                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="w-full py-3 bg-[#FAF7F2] hover:bg-[#F5EFEB] text-[#5C564E] border border-[#DDD4C6] rounded-2xl text-xs font-bold transition"
                    >
                      Tillbaka till tidslinjeteori
                    </button>
                  </div>
                </div>
              ) : currentExercise ? (
                /* Active Drill Question */
                <div className="max-w-xl mx-auto space-y-5 animate-in fade-in">
                  
                  {/* Progress Header */}
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-[#C9862C] flex items-center gap-1.5 font-mono-tag">
                        <Clock className="w-4 h-4 text-[#C9862C]" />
                        <span>Fråga {currentDrillIndex + 1} av {drillExercises.length}</span>
                      </span>
                      <span className="text-[#8F877B] font-mono-tag text-xs">
                        Poäng: {correctAnswersCount} rätt
                      </span>
                    </div>

                    <div className="h-2.5 bg-[#EBE4D8] rounded-full overflow-hidden border border-[#DDD4C6]">
                      <div
                        className="h-full bg-[#C9862C] transition-all duration-300"
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
                          btnStyle = 'bg-[#FDF6EA] border-[#C9862C] text-[#995E15] font-bold shadow-[0_2px_0_#C9862C]';
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

                    {/* AI Memory & Explanation feedback */}
                    {drillAnswerSubmitted && (
                      <div className="p-4 bg-[#FFFFFF] rounded-2xl border border-[#DDD4C6] space-y-1.5 animate-in fade-in">
                        <div className="text-xs font-bold text-[#2D5A3F] flex items-center gap-1.5 font-mono-tag">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Grammatikförklaring:</span>
                        </div>
                        <p className="text-xs text-[#5C564E] leading-relaxed font-sans">
                          {currentExercise.explanation}
                        </p>
                        {lastAiFeedback && (
                          <div className="pt-2 text-[11px] text-[#995E15] font-semibold flex items-center gap-1 border-t border-[#EDE7DD] mt-2 font-editorial italic">
                            <Brain className="w-3.5 h-3.5 text-[#C9862C]" />
                            <span>{lastAiFeedback}</span>
                          </div>
                        )}
                      </div>
                    )}

                    {/* Action Button */}
                    {!drillAnswerSubmitted ? (
                      <button
                        onClick={handleSubmitDrillAnswer}
                        disabled={!selectedOption}
                        className="w-full py-3.5 btn-craft btn-stamp-ochre disabled:opacity-50 text-xs font-bold"
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
                      Avsluta övning och gå tillbaka till tidslinjen
                    </button>
                  </div>

                </div>
              ) : null
            ) : activeTenseDetail ? (
              /* --- Tense Theory & Timeline View (Artisanal Linguistic Sheet) --- */
              <div className="max-w-3xl mx-auto space-y-6">
                
                {/* Header Title & Badges */}
                <div className="space-y-1.5">
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-0.5 rounded-md bg-[#FDF6EA] border border-[#F3E2C4] text-[#995E15] font-mono-tag text-xs uppercase">
                      {activeTenseDetail.time_aspect} • CEFR {activeTenseDetail.level}
                    </span>
                    <span className="text-xs font-semibold text-[#8F877B] font-editorial italic">
                      {activeTenseDetail.swedish_title}
                    </span>
                  </div>
                  <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F]">{activeTenseDetail.title}</h2>
                  <p className="text-xs sm:text-sm text-[#5C564E] font-sans">{activeTenseDetail.summary}</p>
                </div>

                {/* Formula Highlight Banner */}
                <div className="p-4 bg-[#F5EFEB] border border-[#DDD4C6] rounded-2xl flex items-center gap-3.5 shadow-[0_2px_0_#DDD4C6]">
                  <div className="p-2.5 bg-[#FFFFFF] rounded-xl text-[#995E15] border border-[#DDD4C6]">
                    <Sparkles className="w-4 h-4 text-[#C9862C]" />
                  </div>
                  <div>
                    <div className="text-[10px] font-mono-tag uppercase text-[#8F877B]">
                      Tempusformel & Hjälpverksböjning
                    </div>
                    <div className="text-xs sm:text-sm font-mono font-bold text-[#24221F] mt-0.5">
                      {activeTenseDetail.formula}
                    </div>
                  </div>
                </div>

                {/* Timeline & Signal Words */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Timeline */}
                  <div className="p-4 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl space-y-1.5">
                    <div className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                      <Clock className="w-3.5 h-3.5 text-[#2B5876]" />
                      <span>Tidslinjeplacering:</span>
                    </div>
                    <p className="text-xs text-[#5C564E] leading-relaxed font-sans">
                      {activeTenseDetail.timeline_description}
                    </p>
                  </div>

                  {/* Signal Words */}
                  {activeTenseDetail.signal_words.length > 0 && (
                    <div className="p-4 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl space-y-1.5">
                      <div className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                        <Tag className="w-3.5 h-3.5 text-[#2D5A3F]" />
                        <span>Typiska signalord:</span>
                      </div>
                      <div className="flex flex-wrap gap-1.5 pt-0.5">
                        {activeTenseDetail.signal_words.map((word, idx) => (
                          <span
                            key={idx}
                            className="px-2 py-0.5 rounded-md bg-[#FFFFFF] text-[#2D5A3F] border border-[#DDD4C6] text-[11px] font-mono-tag"
                          >
                            {word}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}
                </div>

                {/* Examples with Audio */}
                {activeTenseDetail.examples.length > 0 && (
                  <div className="space-y-2.5">
                    <h4 className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                      <Volume2 className="w-3.5 h-3.5 text-[#2B5876]" />
                      <span>Konkreta exempel med uttal:</span>
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {activeTenseDetail.examples.map((ex, idx) => (
                        <div
                          key={idx}
                          className="p-3.5 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl space-y-1 hover:border-[#24221F] transition"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-bold text-sm text-[#24221F] font-editorial">{ex.english}</span>
                            <button
                              onClick={() => speakText(ex.english, 'en')}
                              title="Spela upp ljud"
                              className="p-1 text-[#8F877B] hover:text-[#24221F] rounded-lg transition"
                            >
                              <Volume2 className="w-3.5 h-3.5" />
                            </button>
                          </div>
                          <div className="text-xs text-[#5C564E]">{ex.swedish}</div>
                          {ex.target_highlight && (
                            <span className="inline-block text-[10px] px-1.5 py-0.5 rounded bg-[#FFFFFF] text-[#2B5876] border border-[#DDD4C6] font-mono-tag">
                              Mönster: {ex.target_highlight}
                            </span>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Common Pitfalls */}
                {activeTenseDetail.common_pitfalls.length > 0 && (
                  <div className="p-4 bg-[#FAECE8] border border-[#F6D3C8] rounded-2xl space-y-1.5">
                    <div className="flex items-center gap-1.5 text-[#B34B32] font-bold text-xs font-mono-tag">
                      <AlertTriangle className="w-3.5 h-3.5" />
                      <span>Vanliga misstag & fallgropar:</span>
                    </div>
                    <ul className="space-y-1 text-xs text-[#632415]">
                      {activeTenseDetail.common_pitfalls.map((pitfall, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-[#B34B32] font-bold">•</span>
                          <span>{pitfall}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Practice Button */}
                <div className="pt-2">
                  <button
                    onClick={handleStartDrill}
                    className="w-full py-3.5 btn-craft btn-stamp-ochre flex items-center justify-center gap-2 text-xs font-bold"
                  >
                    <Play className="w-4 h-4 fill-white" />
                    <span>Starta tempuspass ({activeTenseDetail.exercises_count} övningar)</span>
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
