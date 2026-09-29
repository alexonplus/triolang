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
      setCurrentQuestionIndex(nextIndex);
      const nextQ = questions[nextIndex];
      const aiTurn: DialogueTurn = { sender: 'AI', text: nextQ.prompt };
      setDialogue([...updatedDialogue, aiTurn]);
      speakText(nextQ.prompt, courseId.startsWith('sv') ? 'sv' : 'en');
    } else {
      setIsEvaluating(true);
      try {
        const evaluation = await api.evaluatePlacementTest(updatedDialogue, courseId);
        setAssessmentResult(evaluation);
        soundEffects.playVictorySound();
      } catch (err) {
        console.error('Diagnostic evaluation error:', err);
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
  const progressPercent = questions.length > 0 ? ((currentQuestionIndex) / questions.length) * 100 : 0;

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl max-w-2xl w-full max-h-[85vh] flex flex-col shadow-[0_16px_48px_rgba(45,35,25,0.15)] overflow-hidden">
        
        {/* Header */}
        <div className="p-4 bg-[#FFFFFF] border-b border-[#E5DDD0] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-[#8A321E] text-white flex items-center justify-center shadow-[0_2px_0_#632415] border border-[#632415]">
              <Target className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-base">Diagnostiskt Nivåtest ({courseTitle})</h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                AI analyserar dina svar och anpassar kursstrukturen
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Area */}
        {isLoadingQuestions ? (
          <div className="p-12 flex flex-col items-center justify-center space-y-3 text-[#8F877B]">
            <Loader2 className="w-8 h-8 animate-spin text-[#8A321E]" />
            <span className="text-xs font-editorial italic">Förbereder diagnostiska frågor...</span>
          </div>
        ) : assessmentResult ? (
          /* Assessment Evaluation Results View */
          <div className="p-6 overflow-y-auto space-y-6 bg-[#FAF7F2]">
            <div className="text-center space-y-1.5">
              <div className="inline-flex items-center gap-2 px-3.5 py-1 bg-[#FDF6EA] border border-[#F3E2C4] text-[#995E15] font-mono-tag text-xs rounded-full">
                <Award className="w-4 h-4" />
                <span>CEFR Nivå: {assessmentResult.cefr_level}</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#24221F]">{assessmentResult.level_title}</h2>
              <p className="text-xs sm:text-sm text-[#5C564E] font-editorial italic max-w-md mx-auto">{assessmentResult.message}</p>
            </div>

            {/* Strengths & Weaknesses Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              {/* Strengths */}
              <div className="bg-[#FFFFFF] border border-[#DDD4C6] p-4 rounded-2xl space-y-1.5 shadow-sm">
                <div className="flex items-center gap-1.5 text-[#2D5A3F] font-bold text-xs font-mono-tag">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Styrkor:</span>
                </div>
                <ul className="space-y-1 text-xs text-[#5C564E]">
                  {assessmentResult.strengths.map((s, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-[#2D5A3F] font-bold">•</span>
                      <span>{s}</span>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Weaknesses Detected */}
              <div className="bg-[#FAECE8] border border-[#F6D3C8] p-4 rounded-2xl space-y-1.5 shadow-sm">
                <div className="flex items-center gap-1.5 text-[#B34B32] font-bold text-xs font-mono-tag">
                  <AlertTriangle className="w-4 h-4" />
                  <span>Fokusområden:</span>
                </div>
                <ul className="space-y-1 text-xs text-[#632415]">
                  {assessmentResult.weaknesses.map((w, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-[#B34B32] font-bold">•</span>
                      <span>{w}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>

            {/* Personalized Units Generated Banner */}
            <div className="p-4 bg-[#FFFFFF] border border-[#DDD4C6] rounded-2xl flex items-center justify-between shadow-sm">
              <div>
                <div className="text-[10px] font-mono-tag text-[#2B5876] uppercase">Anpassad studieplan klar</div>
                <div className="text-xs sm:text-sm font-bold text-[#24221F] mt-0.5">
                  Genererade {assessmentResult.units_generated_count} skräddarsydda kapitel
                </div>
              </div>
              <div className="p-2.5 bg-[#FAF7F2] rounded-xl text-[#2B5876] border border-[#DDD4C6]">
                <Zap className="w-5 h-5 text-[#C9862C]" />
              </div>
            </div>

            {/* Action Button */}
            <button
              onClick={handleApplyCustomPath}
              className="w-full py-3.5 btn-craft btn-stamp-forest flex items-center justify-center gap-2 text-xs sm:text-sm font-bold"
            >
              <span>Tillämpa personlig studieplan</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        ) : (
          /* Active Conversational Test View */
          <>
            {/* Progress indicator */}
            <div className="px-4 pt-3 pb-1 flex items-center gap-3 bg-[#FAF7F2]">
              <div className="flex-1 h-2 bg-[#EBE4D8] rounded-full overflow-hidden border border-[#DDD4C6]">
                <div
                  className="h-full bg-[#8A321E] transition-all duration-300"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
              <span className="text-xs font-mono-tag text-[#8F877B]">
                Fråga {currentQuestionIndex + 1} av {questions.length || 3}
              </span>
            </div>

            {/* Chat Flow */}
            <div className="flex-1 overflow-y-auto p-4 space-y-3 min-h-[300px] bg-[#FAF7F2]">
              {dialogue.map((turn, idx) => (
                <div
                  key={idx}
                  className={`flex flex-col ${turn.sender === 'User' ? 'items-end' : 'items-start'}`}
                >
                  <div
                    className={`max-w-[85%] rounded-2xl p-3.5 text-sm shadow-[0_2px_0_#EADFCF] ${
                      turn.sender === 'User'
                        ? 'bg-[#2D5A3F] text-[#FAF7F2] rounded-br-none border border-[#1E3D2B]'
                        : 'bg-[#FFFFFF] border border-[#DDD4C6] text-[#24221F] rounded-bl-none'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-3 mb-1">
                      <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase">
                        {turn.sender === 'AI' ? 'Examinator' : 'Du'}
                      </span>
                      {turn.sender === 'AI' && (
                        <button
                          onClick={() => speakText(turn.text, courseId.startsWith('sv') ? 'sv' : 'en')}
                          className="text-[#8F877B] hover:text-[#24221F]"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      )}
                    </div>
                    <div className="font-sans">{turn.text}</div>
                  </div>
                </div>
              ))}

              {isEvaluating && (
                <div className="flex items-center gap-2 text-[#995E15] text-xs p-3 bg-[#FDF6EA] rounded-2xl border border-[#F3E2C4] font-editorial italic">
                  <Loader2 className="w-4 h-4 animate-spin text-[#C9862C]" />
                  <span>Analyserar grammatiska mönster och beräknar CEFR-nivå...</span>
                </div>
              )}
            </div>

            {/* Hint & Input Area */}
            {currentQ && !isEvaluating && (
              <div className="p-4 bg-[#FFFFFF] border-t border-[#E5DDD0] space-y-2">
                <div className="text-xs text-[#5C564E] flex items-center gap-1.5 font-editorial italic">
                  <Sparkles className="w-3.5 h-3.5 text-[#C9862C]" />
                  <span>Tips: {currentQ.english_hint}</span>
                </div>

                <div className="flex gap-2">
                  <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSendAnswer()}
                    placeholder="Skriv ditt svar på svenska..."
                    className="flex-1 bg-[#FAF7F2] border border-[#DDD4C6] rounded-xl px-4 py-2.5 text-sm text-[#24221F] placeholder-[#A89E90] focus:outline-none focus:border-[#2D5A3F]"
                  />
                  <button
                    onClick={handleSendAnswer}
                    disabled={!userInput.trim() || isEvaluating}
                    className="px-4 py-2.5 btn-craft btn-stamp-dark disabled:opacity-40 text-white rounded-xl font-bold transition flex items-center gap-1 text-xs"
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
