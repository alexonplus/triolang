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
          ? 'bg-emerald-950/95 border-emerald-500 text-emerald-100'
          : 'bg-rose-950/95 border-rose-500 text-rose-100'
      }`}
    >
      <div className="max-w-2xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        
        <div className="flex items-start gap-4">
          <div className="mt-0.5">
            {isCorrect ? (
              <CheckCircle2 className="w-9 h-9 text-emerald-400 stroke-[2.5]" />
            ) : (
              <XCircle className="w-9 h-9 text-rose-400 stroke-[2.5]" />
            )}
          </div>

          <div>
            <h3 className="text-xl font-black">
              {isCorrect ? 'Snyggt jobbat! (Nicely done!)' : 'Incorrect solution'}
            </h3>
            
            {!isCorrect && (
              <div className="text-sm mt-1 font-semibold text-rose-200">
                Correct answer: <span className="underline font-bold text-white">{result.correct_answer}</span>
              </div>
            )}

            {result.explanation && (
              <div className="flex items-center gap-1.5 text-xs text-slate-300 mt-2 bg-black/30 px-3 py-1.5 rounded-lg">
                <Lightbulb className="w-4 h-4 text-amber-300 shrink-0" />
                <span>{result.explanation}</span>
              </div>
            )}
          </div>
        </div>

        <button
          onClick={onContinue}
          className={`px-8 py-3.5 rounded-2xl font-black text-white flex items-center gap-2 btn-3d shadow-lg w-full sm:w-auto justify-center ${
            isCorrect
              ? 'bg-emerald-500 hover:bg-emerald-400 shadow-[0_4px_0_#047857]'
              : 'bg-rose-500 hover:bg-rose-400 shadow-[0_4px_0_#be123c]'
          }`}
        >
          <span>Continue</span>
          <ArrowRight className="w-5 h-5 stroke-[2.5]" />
        </button>

      </div>
    </div>
  );
};
