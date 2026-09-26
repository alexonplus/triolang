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

        // Auto-select first topic if none selected or not in filtered list
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

  // Load active topic detail when selectedTopicId changes
  useEffect(() => {
    if (!selectedTopicId) return;

    const loadDetail = async () => {
      try {
        setIsLoadingDetail(true);
        const detail = await api.getGrammarTopicDetail(selectedTopicId);
        setActiveTopicDetail(detail);
        setIsDrillMode(false);
        setIsDrillCompleted(false);
      } catch (err) {
        console.error('Failed to load topic detail:', err);
      } finally {
        setIsLoadingDetail(false);
      }
    };
    loadDetail();
  }, [selectedTopicId]);

  // Start practice drill
  const handleStartDrill = async (isAI: boolean = false) => {
    if (!selectedTopicId) return;
    try {
      soundEffects.playClickSound();
      if (isAI) {
        setIsGeneratingAIDrills(true);
        const drillData = await api.generateGrammarAIDrills(selectedTopicId);
        setDrillExercises(drillData.exercises);
      } else {
        const drillData = await api.getGrammarPracticeDrills(selectedTopicId);
        setDrillExercises(drillData.exercises);
      }
      setCurrentDrillIndex(0);
      setCorrectAnswersCount(0);
      setSelectedOption(null);
      setDrillAnswerSubmitted(false);
      setIsDrillCompleted(false);
      setIsDrillMode(true);
    } catch (err) {
      console.error('Failed to load practice drills:', err);
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
    if (!selectedOption || drillAnswerSubmitted) return;
    const currentEx = drillExercises[currentDrillIndex];
    const isCorrect = selectedOption.trim().toLowerCase() === currentEx.correct_answer.trim().toLowerCase();

    setDrillAnswerSubmitted(true);
    if (isCorrect) {
      setCorrectAnswersCount((prev) => prev + 1);
      soundEffects.playCorrectSound();
    } else {
      soundEffects.playIncorrectSound();
    }
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
    <div className="fixed inset-0 bg-slate-950/85 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-3xl max-w-5xl w-full h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in zoom-in-95">
        
        {/* Top Header */}
        <div className="p-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-white shadow">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-black text-white text-lg flex items-center gap-2">
                <span>Grammar Hub</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-bold">
                  CEFR A1–C1
                </span>
              </h3>
              <p className="text-xs text-slate-400">
                Structured Rules, Concrete Formulas & In-Depth Practice Drills
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {/* Language Switcher */}
            <div className="flex bg-slate-900 p-1 rounded-xl border border-slate-700">
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
                <span>English</span>
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

        {/* Level Selector Tabs */}
        <div className="px-4 py-2.5 bg-slate-950/60 border-b border-slate-800 flex items-center gap-2 overflow-x-auto">
          <span className="text-xs font-bold text-slate-400 uppercase tracking-wider mr-1">Level:</span>
          {CEFR_LEVELS.map((level) => (
            <button
              key={level}
              onClick={() => {
                soundEffects.playClickSound();
                setSelectedLevel(level);
              }}
              className={`px-3 py-1 rounded-xl text-xs font-black transition ${
                selectedLevel === level
                  ? 'bg-amber-400 text-slate-950 shadow-md scale-105'
                  : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
              }`}
            >
              {level}
            </button>
          ))}
        </div>

        {/* Main Content Body */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* Left Sidebar: Topics list */}
          <div className="w-72 md:w-80 border-r border-slate-800 bg-slate-900/50 overflow-y-auto p-3 space-y-2">
            {isLoadingTopics ? (
              <div className="p-8 flex flex-col items-center justify-center space-y-2 text-slate-400 text-xs">
                <Loader2 className="w-6 h-6 animate-spin text-indigo-400" />
                <span>Loading topics...</span>
              </div>
            ) : topics.length === 0 ? (
              <div className="p-6 text-center text-xs text-slate-500">
                No grammar topics found for this level.
              </div>
            ) : (
              topics.map((t) => (
                <button
                  key={t.id}
                  onClick={() => {
                    soundEffects.playClickSound();
                    setSelectedTopicId(t.id);
                  }}
                  className={`w-full text-left p-3 rounded-2xl border transition flex flex-col gap-1 ${
                    selectedTopicId === t.id
                      ? 'bg-indigo-600/20 border-indigo-500 text-white shadow-lg ring-1 ring-indigo-500/50'
                      : 'bg-slate-800/60 border-slate-700/80 text-slate-300 hover:bg-slate-800 hover:border-slate-600'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-black px-2 py-0.5 rounded-md bg-slate-700 text-amber-300 uppercase">
                      {t.level}
                    </span>
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                      10 Drills
                    </span>
                  </div>
                  <div className="font-bold text-xs line-clamp-1 mt-1">{t.title}</div>
                  <div className="text-[11px] text-slate-400 line-clamp-2 leading-tight">
                    {t.summary}
                  </div>
                </button>
              ))
            )}
          </div>

          {/* Right Pane: Topic Detail & Rule Explanation OR Practice Drills */}
          <div className="flex-1 overflow-y-auto p-6 bg-slate-900">
            {isLoadingDetail ? (
              <div className="h-full flex flex-col items-center justify-center space-y-3">
                <Loader2 className="w-8 h-8 animate-spin text-indigo-400" />
                <span className="text-slate-400 text-sm">Loading rule breakdown...</span>
              </div>
            ) : isDrillMode ? (
              /* --- Drill Mode: Finished or Active --- */
              isDrillCompleted ? (
                /* Celebration Summary */
                <div className="max-w-md mx-auto py-8 text-center space-y-6 animate-in zoom-in-95">
                  <div className="w-20 h-20 mx-auto rounded-3xl bg-gradient-to-tr from-amber-400 to-emerald-400 flex items-center justify-center text-slate-950 shadow-xl">
                    <Award className="w-10 h-10" />
                  </div>

                  <div className="space-y-2">
                    <h2 className="text-2xl font-black text-white">Drill Session Completed!</h2>
                    <p className="text-sm text-slate-400">
                      You practiced <span className="text-indigo-300 font-bold">{activeTopicDetail?.title}</span>
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
                      <div className="text-xs text-slate-500 mt-0.5">Mastery points</div>
                    </div>
                  </div>

                  <div className="space-y-2.5 pt-2">
                    <button
                      onClick={() => handleStartDrill(false)}
                      className="w-full py-3.5 btn-3d bg-emerald-500 hover:bg-emerald-400 text-white font-black rounded-2xl shadow-[0_3px_0_#047857] flex items-center justify-center gap-2 text-sm"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>Practice Again</span>
                    </button>

                    <button
                      onClick={() => setIsDrillMode(false)}
                      className="w-full py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold rounded-2xl text-sm"
                    >
                      Back to Rule Theory
                    </button>
                  </div>
                </div>
              ) : currentExercise ? (
                /* Active Drill Question View */
                <div className="max-w-xl mx-auto space-y-5 animate-in fade-in">
                  
                  {/* Progress Header */}
                  <div className="space-y-2">
                    <div className="flex items-center justify-between text-xs">
                      <span className="font-bold text-amber-400 flex items-center gap-1.5">
                        <Flame className="w-4 h-4 fill-amber-400" />
                        <span>Question {currentDrillIndex + 1} of {drillExercises.length}</span>
                      </span>
                      <span className="text-slate-400 font-bold">
                        Score: {correctAnswersCount} correct
                      </span>
                    </div>

                    <div className="h-2.5 bg-slate-800 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-gradient-to-r from-amber-500 via-emerald-400 to-indigo-500 transition-all duration-300"
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
                          btnStyle = 'bg-indigo-600/30 border-indigo-500 text-white font-bold ring-2 ring-indigo-500/50';
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

                    {/* Explanation feedback */}
                    {drillAnswerSubmitted && (
                      <div className="p-4 bg-slate-900/90 rounded-2xl border border-slate-700 space-y-1.5 animate-in fade-in">
                        <div className="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                          <span>Grammar Breakdown:</span>
                        </div>
                        <p className="text-xs text-slate-300 leading-relaxed">
                          {currentExercise.explanation}
                        </p>
                      </div>
                    )}

                    {/* Action Button */}
                    {!drillAnswerSubmitted ? (
                      <button
                        onClick={handleSubmitDrillAnswer}
                        disabled={!selectedOption}
                        className="w-full py-4 btn-3d bg-indigo-600 hover:bg-indigo-500 disabled:opacity-40 text-white font-black rounded-2xl shadow-[0_3px_0_#3730a3] text-sm"
                      >
                        Check Answer
                      </button>
                    ) : (
                      <button
                        onClick={handleNextDrill}
                        className="w-full py-4 btn-3d bg-emerald-500 hover:bg-emerald-400 text-white font-black rounded-2xl shadow-[0_3px_0_#047857] flex items-center justify-center gap-2 text-sm"
                      >
                        <span>
                          {currentDrillIndex + 1 < drillExercises.length ? 'Next Question' : 'Complete Session'}
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
            ) : activeTopicDetail ? (
              /* --- Topic Detail / Theory Breakdown View --- */
              <div className="max-w-3xl mx-auto space-y-6">
                
                {/* Header Title & Badges */}
                <div className="space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="px-3 py-1 rounded-full bg-amber-400/20 border border-amber-400 text-amber-300 font-black text-xs">
                      CEFR {activeTopicDetail.level}
                    </span>
                    <span className="text-xs font-semibold text-slate-400">
                      {activeTopicDetail.swedish_title}
                    </span>
                  </div>
                  <h2 className="text-2xl font-black text-white">{activeTopicDetail.title}</h2>
                  <p className="text-sm text-slate-400">{activeTopicDetail.summary}</p>
                </div>

                {/* Formula Highlight Banner */}
                <div className="p-4 bg-indigo-950/60 border border-indigo-500/40 rounded-2xl flex items-center gap-3">
                  <div className="p-2 bg-indigo-600/40 rounded-xl text-indigo-300">
                    <Sparkles className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="text-[10px] font-bold uppercase tracking-wider text-indigo-300">
                      Grammar Formula / Key Pattern
                    </div>
                    <div className="text-sm font-mono font-bold text-white mt-0.5">
                      {activeTopicDetail.formula}
                    </div>
                  </div>
                </div>

                {/* Rule Explanation */}
                <div className="space-y-2">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                    <Layers className="w-4 h-4 text-emerald-400" />
                    <span>Detailed Rule Breakdown:</span>
                  </h4>
                  <div className="bg-slate-800/80 border border-slate-700 p-4 rounded-2xl text-xs sm:text-sm text-slate-200 leading-relaxed whitespace-pre-line">
                    {activeTopicDetail.rule_explanation}
                  </div>
                </div>

                {/* Examples with Audio */}
                {activeTopicDetail.examples.length > 0 && (
                  <div className="space-y-3">
                    <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                      <Volume2 className="w-4 h-4 text-sky-400" />
                      <span>Concrete Examples & Pronunciation:</span>
                    </h4>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {activeTopicDetail.examples.map((ex, idx) => (
                        <div
                          key={idx}
                          className="p-3.5 bg-slate-800/60 border border-slate-700/80 rounded-2xl space-y-1.5 hover:border-slate-600 transition"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-bold text-sm text-white">{ex.swedish}</span>
                            <button
                              onClick={() => speakText(ex.swedish, selectedLanguage)}
                              title="Play audio"
                              className="p-1 text-slate-400 hover:text-white rounded-lg transition"
                            >
                              <Volume2 className="w-4 h-4 text-sky-400" />
                            </button>
                          </div>
                          <div className="text-xs text-slate-400">{ex.english}</div>
                          {ex.target_highlight && (
                            <span className="inline-block text-[10px] px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 font-mono">
                              Key: {ex.target_highlight}
                            </span>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Common Pitfalls / Traps */}
                {activeTopicDetail.common_pitfalls.length > 0 && (
                  <div className="p-4 bg-rose-950/40 border border-rose-500/30 rounded-2xl space-y-2">
                    <div className="flex items-center gap-2 text-rose-400 font-bold text-xs uppercase tracking-wider">
                      <AlertTriangle className="w-4 h-4" />
                      <span>Common Pitfalls & Exam Traps:</span>
                    </div>
                    <ul className="space-y-1 text-xs text-slate-300">
                      {activeTopicDetail.common_pitfalls.map((pitfall, idx) => (
                        <li key={idx} className="flex items-start gap-1.5">
                          <span className="text-rose-400 font-bold">•</span>
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
                    className="flex-1 py-4 btn-3d bg-emerald-500 hover:bg-emerald-400 text-white font-black rounded-2xl shadow-[0_3px_0_#047857] flex items-center justify-center gap-2 text-sm"
                  >
                    <Play className="w-4 h-4 fill-white" />
                    <span>Start Practice Session ({activeTopicDetail.exercises_count} Questions)</span>
                  </button>

                  <button
                    onClick={() => handleStartDrill(true)}
                    disabled={isGeneratingAIDrills}
                    className="py-4 px-5 btn-3d bg-gradient-to-r from-amber-500 to-rose-500 hover:from-amber-400 hover:to-rose-400 text-white font-black rounded-2xl shadow-[0_3px_0_#b45309] flex items-center justify-center gap-2 text-sm disabled:opacity-50"
                  >
                    {isGeneratingAIDrills ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Sparkles className="w-4 h-4" />
                    )}
                    <span>AI Generate More Drills</span>
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
