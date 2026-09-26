import React, { useState, useEffect } from 'react';
import { X, Target, Send, Volume2, Sparkles, CheckCircle2, ArrowRight, Loader2, Award, Zap, AlertTriangle } from 'lucide-react';
import { api } from '../services/api';
import { speakText, soundEffects } from '../services/audio';
import type { PlacementQuestionItem, PlacementEvaluationResponse } from '../types';

interface PlacementTestModalProps {
  courseId: string;
  courseTitle: string;
  onClose: () => void;
  onCustomPathGenerated: () => void;
}

interface DialogueTurn {
  sender: 'AI' | 'User';
  text: string;
}

export const PlacementTestModal: React.FC<PlacementTestModalProps> = ({
  courseId,
  courseTitle,
  onClose,
  onCustomPathGenerated,
}) => {
  const [questions, setQuestions] = useState<PlacementQuestionItem[]>([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [dialogue, setDialogue] = useState<DialogueTurn[]>([]);
  const [userInput, setUserInput] = useState('');
  const [isLoadingQuestions, setIsLoadingQuestions] = useState(true);
  const [isEvaluating, setIsEvaluating] = useState(false);
  const [assessmentResult, setAssessmentResult] = useState<PlacementEvaluationResponse | null>(null);

  // Load diagnostic questions
  useEffect(() => {
    const loadQuestions = async () => {
      try {
        setIsLoadingQuestions(true);
        const data = await api.getPlacementQuestions(courseId);
        setQuestions(data);
        if (data.length > 0) {
          setDialogue([{ sender: 'AI', text: data[0].prompt }]);
          speakText(data[0].prompt, courseId.startsWith('sv') ? 'sv' : 'en');
        }
      } catch (err) {
        console.error('Failed to load placement questions:', err);
      } finally {
        setIsLoadingQuestions(false);
      }
    };
    loadQuestions();
  }, [courseId]);

  const handleSendAnswer = async () => {
    if (!userInput.trim() || isEvaluating) return;

    soundEffects.playClickSound();

    const userTurn: DialogueTurn = { sender: 'User', text: userInput.trim() };
    const updatedDialogue = [...dialogue, userTurn];
    setDialogue(updatedDialogue);
    setUserInput('');

    const nextIndex = currentQuestionIndex + 1;

    if (nextIndex < questions.length) {
      // Move to next probe question
      setCurrentQuestionIndex(nextIndex);
      const nextQ = questions[nextIndex];
      const aiTurn: DialogueTurn = { sender: 'AI', text: nextQ.prompt };
      setDialogue([...updatedDialogue, aiTurn]);
      speakText(nextQ.prompt, courseId.startsWith('sv') ? 'sv' : 'en');
    } else {
      // Diagnostic complete! Send to AI for evaluation and path generation
      setIsEvaluating(true);
      try {
        const result = await api.evaluatePlacementTest(updatedDialogue, courseId);
        soundEffects.playVictorySound();
        setAssessmentResult(result);
      } catch (err) {
        console.error('Failed to evaluate placement:', err);
      } finally {
        setIsEvaluating(false);
      }
    }
  };

  const handleApplyCustomPath = () => {
    soundEffects.playClickSound();
    onCustomPathGenerated();
    onClose();
  };

  const currentQ = questions[currentQuestionIndex];
  const progressPercent = questions.length > 0 ? ((currentQuestionIndex + 1) / questions.length) * 100 : 0;

  return (
    <div className="fixed inset-0 bg-slate-950/85 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-3xl max-w-2xl w-full flex flex-col shadow-2xl overflow-hidden max-h-[90vh] animate-in zoom-in-95">
        
        {/* Header */}
        <div className="p-4 bg-slate-800/90 border-b border-slate-700 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-500 to-rose-500 flex items-center justify-center text-white shadow">
              <Target className="w-6 h-6" />
            </div>
            <div>
              <h3 className="font-black text-white text-base">AI Placement & Diagnostic Test</h3>
              <p className="text-xs text-amber-400 font-semibold">
                {courseTitle} — Determine CEFR Level & Target Grammar Weaknesses
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 hover:bg-slate-700 rounded-xl text-slate-400 hover:text-white transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Loading questions state */}
        {isLoadingQuestions ? (
          <div className="p-12 flex flex-col items-center justify-center space-y-4">
            <Loader2 className="w-10 h-10 text-amber-400 animate-spin" />
            <div className="text-white font-bold text-sm">Preparing Diagnostic Test...</div>
            <p className="text-xs text-slate-400">Loading CEFR calibration questions</p>
          </div>
        ) : assessmentResult ? (
          <div className="p-6 overflow-y-auto space-y-6">
            <div className="text-center space-y-2">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 bg-amber-400/20 border border-amber-400 text-amber-300 font-black text-sm rounded-full">
                <Award className="w-4 h-4" />
                <span>CEFR Level: {assessmentResult.cefr_level}</span>
              </div>
              <h2 className="text-2xl font-black text-white">{assessmentResult.level_title}</h2>
              <p className="text-sm text-slate-400 max-w-md mx-auto">{assessmentResult.message}</p>
            </div>

            {/* Strengths & Weaknesses Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {/* Strengths */}
              <div className="bg-slate-800/80 border border-emerald-500/30 p-4 rounded-2xl space-y-2">
                <div className="flex items-center gap-2 text-emerald-400 font-bold text-xs uppercase tracking-wider">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Demonstrated Strengths:</span>
                </div>
                <ul className="space-y-1 text-xs text-slate-300">
                  {assessmentResult.strengths.map((s, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-emerald-400 font-bold">•</span>
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Weaknesses Detected */}
              <div className="bg-slate-800/80 border border-rose-500/30 p-4 rounded-2xl space-y-2">
                <div className="flex items-center gap-2 text-rose-400 font-bold text-xs uppercase tracking-wider">
                  <AlertTriangle className="w-4 h-4" />
                  <span>Targeted Grammar Gaps:</span>
                </div>
                <ul className="space-y-1 text-xs text-slate-300">
                  {assessmentResult.weaknesses.map((w, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-rose-400 font-bold">•</span>
                      <span>{w}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Personalized Units Generated Banner */}
            <div className="p-4 bg-indigo-950/60 border border-indigo-500/40 rounded-2xl flex items-center justify-between">
              <div>
                <div className="text-xs font-bold text-indigo-300 uppercase">Adaptive Path Ready</div>
                <div className="text-sm font-bold text-white mt-0.5">
                  Generated {assessmentResult.units_generated_count} tailored units targeting your gaps
                </div>
              </div>
              <div className="p-2.5 bg-indigo-600/40 rounded-xl text-indigo-300">
                <Zap className="w-5 h-5" />
              </div>
            </div>

            {/* Action Button */}
            <button
              onClick={handleApplyCustomPath}
              className="w-full py-4 btn-3d bg-emerald-500 hover:bg-emerald-400 shadow-[0_4px_0_#047857] text-white font-black rounded-2xl flex items-center justify-center gap-2 text-base"
            >
              <span>Apply My Personalized Learning Path</span>
              <ArrowRight className="w-5 h-5" />
            </button>
          </div>
        ) : (
          /* Active Conversational Test View */
          <>
            {/* Progress indicator */}
            <div className="px-4 pt-3 pb-1 flex items-center gap-3">
              <div className="flex-1 h-2 bg-slate-800 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-amber-500 to-rose-500 transition-all duration-300"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
              <span className="text-xs font-bold text-slate-400">
                Question {currentQuestionIndex + 1} of {questions.length || 3}
              </span>
            </div>

            {/* Chat Flow */}
            <div className="flex-1 overflow-y-auto p-4 space-y-3 min-h-[300px]">
              {dialogue.map((turn, idx) => (
                <div
                  key={idx}
                  className={`flex flex-col ${turn.sender === 'User' ? 'items-end' : 'items-start'}`}
                >
                  <div
                    className={`max-w-[85%] rounded-2xl p-3.5 text-sm ${
                      turn.sender === 'User'
                        ? 'bg-emerald-600 text-white rounded-br-none shadow-[0_3px_0_#047857]'
                        : 'bg-slate-800 border border-slate-700 text-slate-200 rounded-bl-none'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-3 mb-1">
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
                        {turn.sender === 'AI' ? 'TrioBot Examiner' : 'You'}
                      </span>
                      {turn.sender === 'AI' && (
                        <button
                          onClick={() => speakText(turn.text, courseId.startsWith('sv') ? 'sv' : 'en')}
                          className="text-slate-400 hover:text-white"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      )}
                    </div>
                    <div>{turn.text}</div>
                  </div>
                </div>
              ))}

              {isEvaluating && (
                <div className="flex items-center gap-2 text-amber-400 text-xs italic p-2 bg-amber-400/10 rounded-xl border border-amber-400/20">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Analyzing grammar patterns, CEFR score, and building your custom path...</span>
                </div>
              )}
            </div>

            {/* Hint & Input Area */}
            {currentQ && !isEvaluating && (
              <div className="p-4 bg-slate-800/90 border-t border-slate-700 space-y-2">
                <div className="text-xs text-slate-400 flex items-center gap-1.5">
                  <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                  <span>Hint: {currentQ.english_hint}</span>
                </div>

                <div className="flex gap-2">
                  <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSendAnswer()}
                    placeholder="Type your response in Swedish / English..."
                    className="flex-1 bg-slate-900 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-amber-500"
                  />
                  <button
                    onClick={handleSendAnswer}
                    disabled={!userInput.trim() || isEvaluating}
                    className="px-4 py-2.5 bg-gradient-to-r from-amber-500 to-rose-500 hover:from-amber-400 hover:to-rose-400 disabled:opacity-40 text-white rounded-xl font-bold transition flex items-center gap-1"
                  >
                    <Send className="w-4 h-4" />
                  </button>
                </div>
              </div>
            )}
          </>
        )}

      </div>
    </div>
  );
};
