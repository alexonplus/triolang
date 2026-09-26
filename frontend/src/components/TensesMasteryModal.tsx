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

        // Auto-select first tense if none selected or not in filtered list
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
        const detail = await api.getTenseDetail(selectedTenseId);
        setActiveTenseDetail(detail);
        setIsDrillMode(false);
        setIsDrillCompleted(false);
      } catch (err) {
        console.error('Failed to load tense detail:', err);
      } finally {
        setIsLoadingDetail(false);
      }
    };
    loadDetail();
  }, [selectedTenseId]);

  // Start drill practice
  const handleStartDrill = async () => {
    if (!selectedTenseId) return;
    try {
      soundEffects.playClickSound();
      const drillData = await api.getTenseDrills(selectedTenseId);
      setDrillExercises(drillData.exercises);
      setCurrentDrillIndex(0);
      setCorrectAnswersCount(0);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
      setIsDrillCompleted(false);
      setLastAiFeedback(null);
      setIsDrillMode(true);
    } catch (err) {
      console.error('Failed to load tense drills:', err);
    }
  };

  const handleSelectDrillOption = (option: string) => {
    if (drillAnswerSubmitted) return;
    soundEffects.playClickSound();
    setSelectedOption(option);
  };

  const handleSubmitDrillAnswer = async () => {
    if (!selectedOption || drillAnswerSubmitted || !selectedTenseId) return;
    const currentEx = drillExercises[currentDrillIndex];

    try {
      const result = await api.submitTenseDrill(selectedTenseId, currentEx.id, selectedOption);
      setDrillAnswerSubmitted(true);
      setLastAiFeedback(result.ai_memory_feedback || null);

      if (result.is_correct) {
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
    <div className="fixed inset-0 bg-slate-950/85 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-3xl max-w-5xl w-full h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in zoom-in-95">
        
        {/* Top Header */}
        <div className="p-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-rose-600 flex items-center justify-center text-white shadow">
              <Clock className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-black text-white text-lg flex items-center gap-2">
                <span>Verb Tenses Lab</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold">
                  {selectedLanguage === 'en' ? 'All 12 Tenses' : 'Complete Temporal System'}
                </span>
              </h3>
              <p className="text-xs text-slate-400">
                Timelines, Signal Words & AI Persistent Memory Tracker
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Switcher */}
            <div className="flex bg-slate-900 p-1 rounded-xl border border-slate-700">
              <button
                onClick={() => {
                  soundEffects.playClickSound();
                  setSelectedLanguage('en');
                }}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition ${
                  selectedLanguage === 'en'
                    ? 'bg-indigo-600 text-white shadow'
                    : 'text-slate-400 hover:text-white'
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
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition ${
                  selectedLanguage === 'sv'
                    ? 'bg-emerald-500 text-white shadow'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                <span>🇸🇪</span>
                <span>Svenska</span>
              </button>
            </div>

            <button
              onClick={onClose}
              className="p-2 hover:bg-slate-700 rounded-xl text-slate-400 hover:text-white transition"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* AI Memory Diagnostic Ribbon */}
        {aiMemoryProfile && (
          <div className="px-4 py-2 bg-indigo-950/40 border-b border-indigo-500/20 flex flex-wrap items-center justify-between gap-2 text-xs">
            <div className="flex items-center gap-2 text-indigo-300 font-semibold">
              <Brain className="w-4 h-4 text-indigo-400 shrink-0" />
              <span>{aiMemoryProfile.ai_coaching_note}</span>
            </div>
            <div className="flex items-center gap-3 shrink-0">
              <div className="flex items-center gap-1 font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-md border border-amber-500/20">
                <Zap className="w-3.5 h-3.5" />
                <span>Accuracy: {aiMemoryProfile.overall_accuracy}%</span>
              </div>
              {aiMemoryProfile.total_mistakes_logged > 0 && (
                <span className="text-[11px] text-slate-400">
                  {aiMemoryProfile.total_mistakes_logged} mistakes remembered
                </span>
              )}
            </div>
          </div>
        )}

        {/* Time Aspect Filter Bar */}
        <div className="px-4 py-2 bg-slate-950/60 border-b border-slate-800 flex items-center gap-2 overflow-x-auto">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider mr-1">Aspect:</span>
          {TIME_ASPECTS.map((aspect) => (
            <button
              key={aspect}
              onClick={() => {
                soundEffects.playClickSound();
                setSelectedAspect(aspect);
              }}
              className={`px-3 py-1 rounded-xl text-xs font-black capitalize transition ${
                selectedAspect === aspect
                  ? 'bg-gradient-to-r from-amber-500 to-rose-500 text-white shadow scale-105'
                  : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
              }`}
            >
              {aspect}
            </button>
          ))}
        </div>

        {/* Main Content Body */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* Left Sidebar: Tenses Matrix */}
          <div className="w-72 md:w-80 border-r border-slate-800 bg-slate-900/50 overflow-y-auto p-3 space-y-2">
            {isLoadingTenses ? (
              <div className="p-8 flex flex-col items-center justify-center space-y-2 text-slate-400 text-xs">
                <Loader2 className="w-6 h-6 animate-spin text-amber-400" />
                <span>Loading tenses...</span>
              </div>
            ) : tenses.length === 0 ? (
              <div className="p-6 text-center text-xs text-slate-500">
                No tenses found for this aspect.
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
                    className={`w-full text-left p-3 rounded-2xl border transition flex flex-col gap-1.5 ${
                      isSelected
                        ? 'bg-gradient-to-r from-amber-500/15 to-rose-500/15 border-amber-500 text-white shadow-lg ring-1 ring-amber-500/50'
                        : 'bg-slate-800/60 border-slate-700/80 text-slate-300 hover:bg-slate-800 hover:border-slate-600'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] font-black px-2 py-0.5 rounded-md bg-slate-700 text-amber-300 uppercase">
                        {t.time_aspect}
                      </span>
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                        {t.mastery_percentage > 0 ? `${t.mastery_percentage}% Mastery` : '10 Drills'}
                      </span>
                    </div>
                    <div className="font-bold text-xs line-clamp-1">{t.title}</div>
                    <div className="text-[11px] text-slate-400 line-clamp-2 leading-tight">
                      {t.summary}
                    </div>
                  </button>
                );
              })
            )}
          </div>

          {/* Right Pane: Tense Breakdown or Interactive Drill Session */}
          <div className="flex-1 overflow-y-auto p-6 bg-slate-900">
            {isLoadingDetail ? (
              <div className="h-full flex flex-col items-center justify-center space-y-3">
                <Loader2 className="w-8 h-8 animate-spin text-amber-400" />
                <span className="text-slate-400 text-sm">Loading tense structure & timeline...</span>
              </div>
            ) : isDrillMode ? (
              /* --- Drill Practice Mode --- */
              isDrillCompleted ? (
                /* Celebration Summary */
                <div className="max-w-md mx-auto py-8 text-center space-y-6 animate-in zoom-in-95">
                  <div className="w-20 h-20 mx-auto rounded-3xl bg-gradient-to-tr from-amber-400 to-rose-500 flex items-center justify-center text-slate-950 shadow-xl">
                    <Award className="w-10 h-10" />
                  </div>

                  <div className="space-y-2">
                    <h2 className="text-2xl font-black text-white">Tense Drill Completed!</h2>
                    <p className="text-sm text-slate-400">
                      TrioBot AI memory updated for <span className="text-amber-300 font-bold">{activeTenseDetail?.title}</span>
                    </p>
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    <div className="p-4 bg-slate-800 rounded-2xl border border-slate-700">
                      <div className="text-xs text-slate-400 font-bold uppercase">Accuracy</div>
                      <div className="text-2xl font-black text-emerald-400 mt-1">{accuracyPercentage}%</div>
                      <div className="text-xs text-slate-500 mt-0.5">{correctAnswersCount} of {drillExercises.length} correct</div>
                    </div>
                    <div className="p-4 bg-slate-800 rounded-2xl border border-slate-700">
                      <div className="text-xs text-slate-400 font-bold uppercase">XP Earned</div>
                      <div className="text-2xl font-black text-amber-400 mt-1">+{correctAnswersCount * 10} XP</div>
                      <div className="text-xs text-slate-500 mt-0.5">Persistent mastery</div>
                    </div>
                  </div>

                  <div className="space-y-2.5 pt-2">
                    <button
                      onClick={handleStartDrill}
                      className="w-full py-3.5 btn-3d bg-emerald-500 hover:bg-emerald-400 text-white font-black rounded-2xl shadow-[0_3px_0_#047857] flex items-center justify-center gap-2 text-sm"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>Practice Again</span>
                    </button>

                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="w-full py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold rounded-2xl text-sm"
                    >
                      Back to Tense Theory & Timeline
                    </button>
                  </div>
                </div>
              ) : currentExercise ? (
                /* Active Drill Question */
                <div className="max-w-xl mx-auto space-y-5 animate-in fade-in">
                  
                  {/* Progress Header */}
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-amber-400 flex items-center gap-1.5">
                        <Clock className="w-4 h-4 text-amber-400" />
                        <span>Question {currentDrillIndex + 1} of {drillExercises.length}</span>
                      </span>
                      <span className="text-slate-400 font-bold">
                        Score: {correctAnswersCount} correct
                      </span>
                    </div>

                    <div className="h-2.5 bg-slate-800 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-amber-500 via-rose-500 to-indigo-500 transition-all duration-300"
                        style={{ width: `${drillProgressPercent}%` }}
                      />
                    </div>
                  </div>

                  {/* Question Card */}
                  <div className="bg-slate-800/90 border border-slate-700 p-6 rounded-3xl space-y-5 shadow-xl">
                    <div className="text-base sm:text-lg font-black text-white leading-relaxed">
                      {currentExercise.prompt}
                    </div>

                    {/* Options */}
                    <div className="space-y-2.5">
                      {currentExercise.options?.map((opt, idx) => {
                        const isSelected = selectedOption === opt;
                        const isCorrect = opt.trim().toLowerCase() === currentExercise.correct_answer.trim().toLowerCase();

                        let btnStyle = 'bg-slate-900/90 border-slate-700 text-slate-200 hover:border-slate-500';
                        if (drillAnswerSubmitted) {
                          if (isCorrect) {
                            btnStyle = 'bg-emerald-500/20 border-emerald-500 text-emerald-300 font-bold ring-2 ring-emerald-500/30';
                          } else if (isSelected) {
                            btnStyle = 'bg-rose-500/20 border-rose-500 text-rose-300 font-bold ring-2 ring-rose-500/30';
                          }
                        } else if (isSelected) {
                          btnStyle = 'bg-amber-500/20 border-amber-500 text-white font-bold ring-2 ring-amber-500/50';
                        }

                        return (
                          <button
                            key={idx}
                            onClick={() => handleSelectDrillOption(opt)}
                            disabled={drillAnswerSubmitted}
                            className={`w-full text-left p-3.5 rounded-2xl border transition flex items-center justify-between text-sm ${btnStyle}`}
                          >
                            <span>{opt}</span>
                            {drillAnswerSubmitted && isCorrect && (
                              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                            )}
                          </button>
                        );
                      })}
                    </div>

                    {/* AI Memory & Explanation feedback */}
                    {drillAnswerSubmitted && (
                      <div className="p-4 bg-slate-900/90 rounded-2xl border border-slate-700 space-y-1.5 animate-in fade-in">
                        <div className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                          <span>Grammar Explanation:</span>
                        </div>
                        <p className="text-xs text-slate-300 leading-relaxed">
                          {currentExercise.explanation}
                        </p>
                        {lastAiFeedback && (
                          <div className="pt-2 text-[11px] text-amber-300 font-semibold flex items-center gap-1 border-t border-slate-800 mt-2">
                            <Brain className="w-3.5 h-3.5 text-amber-400" />
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
                        className="w-full py-4 btn-3d bg-amber-500 hover:bg-amber-400 disabled:opacity-40 text-slate-950 font-black rounded-2xl shadow-[0_3px_0_#b45309] text-sm"
                      >
                        Check Answer
                      </button>
                    ) : (
                      <button
                        onClick={handleNextDrill}
                        className="w-full py-4 btn-3d bg-emerald-500 hover:bg-emerald-400 text-white font-black rounded-2xl shadow-[0_3px_0_#047857] flex items-center justify-center gap-2 text-sm"
                      >
                        <span>
                          {currentDrillIndex + 1 < drillExercises.length ? 'Next Question' : 'Complete Tense Session'}
                        </span>
                        <ArrowRight className="w-4 h-4" />
                      </button>
                    )}
                  </div>

                  <div className="text-center">
                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="text-xs text-slate-400 hover:text-slate-200 underline"
                    >
                      Exit drill and return to theory
                    </button>
                  </div>

                </div>
              ) : null
            ) : activeTenseDetail ? (
              /* --- Tense Theory & Timeline View --- */
              <div className="max-w-3xl mx-auto space-y-6">
                
                {/* Header Title & Badges */}
                <div className="space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-3 py-1 rounded-full bg-amber-400/20 border border-amber-400 text-amber-300 font-black text-xs uppercase">
                      {activeTenseDetail.time_aspect} • CEFR {activeTenseDetail.level}
                    </span>
                    <span className="text-xs font-semibold text-slate-400">
                      {activeTenseDetail.swedish_title}
                    </span>
                  </div>
                  <h2 className="text-2xl font-black text-white">{activeTenseDetail.title}</h2>
                  <p className="text-sm text-slate-400">{activeTenseDetail.summary}</p>
                </div>

                {/* Formula Highlight Banner */}
                <div className="p-4 bg-amber-950/40 border border-amber-500/30 rounded-2xl flex items-center gap-3">
                  <div className="p-2.5 bg-amber-500/20 rounded-xl text-amber-300">
                    <Sparkles className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="text-[10px] font-bold uppercase tracking-wider text-amber-300">
                      Tense Formula & Auxiliary Conjugation
                    </div>
                    <div className="text-sm font-mono font-bold text-white mt-0.5">
                      {activeTenseDetail.formula}
                    </div>
                  </div>
                </div>

                {/* Timeline & Signal Words */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Timeline */}
                  <div className="p-4 bg-slate-800/80 border border-slate-700 rounded-2xl space-y-2">
                    <div className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                      <Clock className="w-4 h-4 text-sky-400" />
                      <span>Timeline Placement:</span>
                    </div>
                    <p className="text-xs text-slate-300 leading-relaxed">
                      {activeTenseDetail.timeline_description}
                    </p>
                  </div>

                  {/* Signal Words */}
                  {activeTenseDetail.signal_words.length > 0 && (
                    <div className="p-4 bg-slate-800/80 border border-slate-700 rounded-2xl space-y-2">
                      <div className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                        <Tag className="w-4 h-4 text-emerald-400" />
                        <span>Key Signal Words:</span>
                      </div>
                      <div className="flex flex-wrap gap-1.5">
                        {activeTenseDetail.signal_words.map((word, idx) => (
                          <span
                            key={idx}
                            className="px-2 py-0.5 rounded-md bg-slate-900 text-emerald-300 border border-emerald-500/30 text-[11px] font-mono"
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
                  <div className="space-y-3">
                    <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                      <Volume2 className="w-4 h-4 text-sky-400" />
                      <span>Concrete Examples & Pronunciation:</span>
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {activeTenseDetail.examples.map((ex, idx) => (
                        <div
                          key={idx}
                          className="p-3.5 bg-slate-800/60 border border-slate-700/80 rounded-2xl space-y-1.5 hover:border-slate-600 transition"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-bold text-sm text-white">{ex.english}</span>
                            <button
                              onClick={() => speakText(ex.english, 'en')}
                              title="Play audio"
                              className="p-1 text-slate-400 hover:text-white rounded-lg transition"
                            >
                              <Volume2 className="w-4 h-4 text-sky-400" />
                            </button>
                          </div>
                          <div className="text-xs text-slate-400">{ex.swedish}</div>
                          {ex.target_highlight && (
                            <span className="inline-block text-[10px] px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 font-mono">
                              Pattern: {ex.target_highlight}
                            </span>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Common Pitfalls */}
                {activeTenseDetail.common_pitfalls.length > 0 && (
                  <div className="p-4 bg-rose-950/40 border border-rose-500/30 rounded-2xl space-y-2">
                    <div className="flex items-center gap-2 text-rose-400 font-bold text-xs uppercase tracking-wider">
                      <AlertTriangle className="w-4 h-4" />
                      <span>Common Pitfalls & Mistakes:</span>
                    </div>
                    <ul className="space-y-1 text-xs text-slate-300">
                      {activeTenseDetail.common_pitfalls.map((pitfall, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-rose-400 font-bold">•</span>
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
                    className="w-full py-4 btn-3d bg-gradient-to-r from-amber-500 to-rose-500 hover:from-amber-400 hover:to-rose-400 text-white font-black rounded-2xl shadow-[0_4px_0_#b45309] flex items-center justify-center gap-2 text-base"
                  >
                    <Play className="w-5 h-5 fill-white" />
                    <span>Start Tense Practice Session ({activeTenseDetail.exercises_count} Questions)</span>
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
