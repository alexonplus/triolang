import React, { useState, useEffect } from 'react';
import { X, Heart } from 'lucide-react';
import type { LessonDetail, Exercise, AnswerSubmitResponse, LessonCompleteResponse } from '../types';
import { WordBankExercise } from './WordBankExercise';
import { MultipleChoiceExercise } from './MultipleChoiceExercise';
import { PairMatchExercise } from './PairMatchExercise';
import { AudioExercise } from './AudioExercise';
import { ResultDrawer } from './ResultDrawer';
import { api } from '../services/api';
import { soundEffects } from '../services/audio';

interface ExerciseSessionProps {
  lesson: LessonDetail;
  hearts: number;
  onQuit: () => void;
  onComplete: (summary: LessonCompleteResponse) => void;
  onHeartsUpdate: (newHearts: number) => void;
}

export const ExerciseSession: React.FC<ExerciseSessionProps> = ({
  lesson,
  hearts,
  onQuit,
  onComplete,
  onHeartsUpdate,
}) => {
  const exercises = lesson.exercises || [];
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [selectedWords, setSelectedWords] = useState<string[]>([]);
  const [availableWords, setAvailableWords] = useState<Array<{ id: number; word: string; isUsed: boolean }>>([]);
  const [isPairMatchDone, setIsPairMatchDone] = useState(false);
  const [isChecking, setIsChecking] = useState(false);
  const [result, setResult] = useState<AnswerSubmitResponse | null>(null);
  const [correctAnswersCount, setCorrectAnswersCount] = useState(0);

  const currentExercise: Exercise | undefined = exercises[currentIndex];
  const progressPercent = exercises.length > 0 ? (currentIndex / exercises.length) * 100 : 0;

  useEffect(() => {
    if (!currentExercise) return;

    setSelectedOption(null);
    setSelectedWords([]);
    setIsPairMatchDone(false);
    setResult(null);

    if (currentExercise.word_bank) {
      setAvailableWords(
        currentExercise.word_bank.map((word, id) => ({
          id,
          word,
          isUsed: false,
        }))
      );
    }
  }, [currentIndex, currentExercise]);

  const handleToggleWord = (word: string, id: number) => {
    setSelectedWords((prev) => [...prev, word]);
    setAvailableWords((prev) =>
      prev.map((item) => (item.id === id ? { ...item, isUsed: true } : item))
    );
  };

  const handleRemoveWord = (index: number) => {
    const wordToRemove = selectedWords[index];
    const newSelected = selectedWords.filter((_, idx) => idx !== index);
    setSelectedWords(newSelected);

    const matched = availableWords.find((item) => item.word === wordToRemove && item.isUsed);
    if (matched) {
      setAvailableWords((prev) =>
        prev.map((item) => (item.id === matched.id ? { ...item, isUsed: false } : item))
      );
    }
  };

  const canCheck = () => {
    if (!currentExercise || result !== null || isChecking) return false;
    if (currentExercise.exercise_type === 'multiple_choice' || currentExercise.exercise_type === 'listen_transcribe') {
      return selectedOption !== null;
    }
    if (currentExercise.exercise_type === 'word_bank') {
      return selectedWords.length > 0;
    }
    if (currentExercise.exercise_type === 'pair_match') {
      return isPairMatchDone;
    }
    return false;
  };

  const handleCheckAnswer = async () => {
    if (!currentExercise || !canCheck()) return;

    let answerStr = '';
    if (currentExercise.exercise_type === 'multiple_choice' || currentExercise.exercise_type === 'listen_transcribe') {
      answerStr = selectedOption || '';
    } else if (currentExercise.exercise_type === 'word_bank') {
      answerStr = selectedWords.join(' ');
    } else if (currentExercise.exercise_type === 'pair_match') {
      answerStr = 'pairs_completed';
    }

    setIsChecking(true);
    try {
      const res = await api.submitAnswer(currentExercise.id, answerStr);
      setResult(res);
      onHeartsUpdate(res.hearts_remaining);

      if (res.is_correct) {
        soundEffects.playCorrectSound();
        setCorrectAnswersCount((prev) => prev + 1);
      } else {
        soundEffects.playIncorrectSound();
      }
    } catch (err) {
      console.error('Failed to submit answer:', err);
    } finally {
      setIsChecking(false);
    }
  };

  const handleContinue = async () => {
    if (currentIndex + 1 < exercises.length) {
      setCurrentIndex((prev) => prev + 1);
    } else {
      const accuracy = Math.round(((correctAnswersCount + (result?.is_correct ? 1 : 0)) / exercises.length) * 100);
      try {
        const completeSummary = await api.completeLesson(lesson.id, accuracy);
        onComplete(completeSummary);
      } catch (err) {
        console.error('Failed to complete lesson:', err);
      }
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex flex-col justify-between pb-32">
      
      <div className="max-w-4xl mx-auto w-full px-4 pt-6 flex items-center gap-4">
        <button
          onClick={onQuit}
          className="p-2 text-slate-400 hover:text-white rounded-xl hover:bg-slate-800 transition"
        >
          <X className="w-6 h-6" />
        </button>

        <div className="flex-1 h-3.5 bg-slate-800 rounded-full overflow-hidden border border-slate-700/60">
          <div
            className="h-full bg-emerald-500 rounded-full transition-all duration-300"
            style={{ width: `${progressPercent}%` }}
          />
        </div>

        <div className="flex items-center gap-1.5 font-black text-rose-400">
          <Heart className="w-6 h-6 fill-rose-500" />
          <span>{hearts}</span>
        </div>
      </div>

      <main className="max-w-3xl mx-auto w-full px-4 py-8 flex-1 flex flex-col justify-center">
        {currentExercise && (
          <>
            {currentExercise.exercise_type === 'word_bank' && (
              <WordBankExercise
                exercise={currentExercise}
                selectedWords={selectedWords}
                onToggleWord={handleToggleWord}
                onRemoveWord={handleRemoveWord}
                availableWords={availableWords}
              />
            )}

            {currentExercise.exercise_type === 'multiple_choice' && (
              <MultipleChoiceExercise
                exercise={currentExercise}
                selectedOption={selectedOption}
                onSelectOption={setSelectedOption}
              />
            )}

            {currentExercise.exercise_type === 'listen_transcribe' && (
              <AudioExercise
                exercise={currentExercise}
                selectedOption={selectedOption}
                onSelectOption={setSelectedOption}
              />
            )}

            {currentExercise.exercise_type === 'pair_match' && (
              <PairMatchExercise
                exercise={currentExercise}
                onAllMatched={() => {
                  setIsPairMatchDone(true);
                }}
              />
            )}
          </>
        )}
      </main>

      {!result && (
        <div className="fixed bottom-0 left-0 right-0 p-4 bg-slate-900/90 border-t border-slate-800 backdrop-blur-md">
          <div className="max-w-2xl mx-auto flex justify-end">
            <button
              onClick={handleCheckAnswer}
              disabled={!canCheck()}
              className={`w-full sm:w-auto px-10 py-3.5 rounded-2xl font-black text-white text-base btn-3d transition ${
                canCheck()
                  ? 'bg-emerald-500 hover:bg-emerald-400 shadow-[0_4px_0_#047857]'
                  : 'bg-slate-800 text-slate-600 cursor-not-allowed opacity-60 shadow-none'
              }`}
            >
              Check Answer
            </button>
          </div>
        </div>
      )}

      <ResultDrawer result={result} onContinue={handleContinue} />

    </div>
  );
};
