import React from 'react';
import { CheckCircle2, XCircle, ArrowRight, Lightbulb } from 'lucide-react';
import type { AnswerSubmitResponse } from '../types';

interface ResultDrawerProps {
  result: AnswerSubmitResponse | null;
  onContinue: () => void;
}

export const ResultDrawer: React.FC<ResultDrawerProps> = ({ result, onContinue }) => {
  if (!result) return null;

  const isCorrect = result.is_correct;

  return (
    <div
      className={`fixed bottom-0 left-0 right-0 p-6 z-50 transition-all transform animate-in slide-in-from-bottom border-t-2 ${
        isCorrect
          ? 'bg-[#EBF3ED] border-[#2D5A3F] text-[#1E3D2B] shadow-[0_-4px_20px_rgba(45,90,63,0.08)]'
          : 'bg-[#FAECE8] border-[#B34B32] text-[#632415] shadow-[0_-4px_20px_rgba(179,75,50,0.08)]'
      }`}
    >
      <div className="max-w-2xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-5">
        
        <div className="flex items-start gap-4">
          <div className="mt-0.5">
            {isCorrect ? (
              <CheckCircle2 className="w-8 h-8 text-[#2D5A3F] stroke-[2.5]" />
            ) : (
              <XCircle className="w-8 h-8 text-[#B34B32] stroke-[2.5]" />
            )}
          </div>

          <div>
            <h3 className="text-xl font-bold font-display">
              {isCorrect ? 'Snyggt jobbat! (Utmärkt svar)' : 'Inte helt rätt den här gången'}
            </h3>
            
            {!isCorrect && (
              <div className="text-sm mt-1 font-semibold text-[#8A321E]">
                Rätt lösning: <span className="font-bold underline text-[#24221F]">{result.correct_answer}</span>
              </div>
            )}

            {result.explanation && (
              <div className="flex items-center gap-2 text-xs text-[#5C564E] mt-2 bg-[#FFFFFF] border border-[#DDD4C6] px-3 py-1.5 rounded-xl shadow-sm">
                <Lightbulb className="w-4 h-4 text-[#C9862C] shrink-0" />
                <span>{result.explanation}</span>
              </div>
            )}
          </div>
        </div>

        <button
          onClick={onContinue}
          className={`px-8 py-3.5 rounded-2xl font-bold text-white flex items-center gap-2 btn-craft w-full sm:w-auto justify-center text-sm shadow-md ${
            isCorrect
              ? 'btn-stamp-forest'
              : 'btn-stamp-terracotta'
          }`}
        >
          <span>Fortsätt</span>
          <ArrowRight className="w-4 h-4 stroke-[2.5]" />
        </button>

      </div>
    </div>
  );
};
