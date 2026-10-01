import React, { useState, useEffect } from 'react';
import {
  X,
  Volume2,
  Sparkles,
  CheckCircle2,
  Loader2,
  Award,
  RotateCcw,
  Headphones,
  Music,
  ArrowRight,
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { api } from '../services/api';
import { speakText, soundEffects } from '../services/audio';
import type {
  PronunciationGuideResponse,
  MinimalPairItem,
  ListeningQuizQuestion,
} from '../types';

interface PronunciationModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialLanguage?: string;
}

type TabType = 'minimal_pairs' | 'vowel_groups' | 'pitch_accents' | 'listening_quiz';

export const PronunciationModal: React.FC<PronunciationModalProps> = ({
  isOpen,
  onClose,
  initialLanguage = 'sv',
}) => {
  const [activeTab, setActiveTab] = useState<TabType>('minimal_pairs');
  const [guideData, setGuideData] = useState<PronunciationGuideResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Quiz state
  const [currentQuizIndex, setCurrentQuizIndex] = useState(0);
  const [selectedQuizOption, setSelectedQuizOption] = useState<string | null>(null);
  const [isQuizAnswerSubmitted, setIsQuizAnswerSubmitted] = useState(false);
  const [correctQuizCount, setCorrectQuizCount] = useState(0);
  const [isQuizFinished, setIsQuizFinished] = useState(false);

  useEffect(() => {
    if (!isOpen) return;

    const fetchGuide = async () => {
      try {
        setIsLoading(true);
        const data = await api.getPronunciationGuide(initialLanguage);
        setGuideData(data);
      } catch (err) {
        console.error('Failed to load pronunciation guide:', err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchGuide();
  }, [isOpen, initialLanguage]);

  if (!isOpen) return null;

  const handlePlayAudio = (text: string, lang: string = 'sv') => {
    speakText(text, lang);
  };

  const handleStartQuiz = () => {
    soundEffects.playClickSound();
    setCurrentQuizIndex(0);
    setSelectedQuizOption(null);
    setIsQuizAnswerSubmitted(false);
    setCorrectQuizCount(0);
    setIsQuizFinished(false);
    setActiveTab('listening_quiz');

    // Auto-play first question sound
    if (guideData?.listening_quiz[0]) {
      setTimeout(() => {
        speakText(guideData.listening_quiz[0].audio_text, 'sv');
      }, 300);
    }
  };

  const handleSelectQuizOption = (option: string) => {
    if (isQuizAnswerSubmitted) return;
    soundEffects.playClickSound();
    setSelectedQuizOption(option);
  };

  const handleSubmitQuizAnswer = () => {
    if (!selectedQuizOption || !currentQuizQuestion || isQuizAnswerSubmitted) return;

    const isCorrect =
      selectedQuizOption.trim().toLowerCase() === currentQuizQuestion.correct_answer.trim().toLowerCase();

    if (isCorrect) {
      soundEffects.playCorrectSound();
      setCorrectQuizCount((prev) => prev + 1);
    } else {
      soundEffects.playIncorrectSound();
    }

    setIsQuizAnswerSubmitted(true);
  };

  const handleNextQuizQuestion = () => {
    soundEffects.playClickSound();
    const quizList = guideData?.listening_quiz || [];
    if (currentQuizIndex + 1 < quizList.length) {
      const nextIdx = currentQuizIndex + 1;
      setCurrentQuizIndex(nextIdx);
      setSelectedQuizOption(null);
      setIsQuizAnswerSubmitted(false);
      // Auto-pronounce next target
      setTimeout(() => {
        speakText(quizList[nextIdx].audio_text, 'sv');
      }, 250);
    } else {
      soundEffects.playVictorySound();
      try {
        confetti({
          particleCount: 70,
          spread: 60,
          origin: { y: 0.6 },
        });
      } catch {
        // Fallback
      }
      setIsQuizFinished(true);
    }
  };

  const currentQuizQuestion: ListeningQuizQuestion | undefined = guideData?.listening_quiz[currentQuizIndex];
  const quizListLength = guideData?.listening_quiz.length || 0;

  return (
    <div className="fixed inset-0 bg-stone-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-5 font-sans">
      <div className="bg-[#FAF7F2] border border-[#E5DDD0] rounded-3xl max-w-4xl w-full max-h-[92vh] flex flex-col shadow-[0_16px_48px_rgba(45,35,25,0.15)] overflow-hidden">
        
        {/* Header Bar */}
        <div className="p-4 bg-[#FFFFFF] border-b border-[#E5DDD0] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-[#2B5876] text-white flex items-center justify-center shadow-[0_2px_0_#1A374A] border border-[#1A374A]">
              <Headphones className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold font-display text-[#24221F] text-lg flex items-center gap-2">
                <span>Uttalsstudio & Fonetiklabb</span>
                <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#EEF5F9] text-[#2B5876] border border-[#D5E5EE]">
                  Svenska (sv)
                </span>
              </h3>
              <p className="text-xs text-[#5C564E] font-editorial italic">
                Vokallängder, hårda/mjuka konsonantskiften och melodiska tonaccenter
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              soundEffects.playClickSound();
              onClose();
            }}
            className="p-2 hover:bg-[#F5EFEB] rounded-xl text-[#8F877B] hover:text-[#24221F] transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Navigation Tabs Bar */}
        <div className="px-4 py-2 bg-[#F5EFEB] border-b border-[#E5DDD0] flex items-center gap-2 overflow-x-auto">
          <button
            onClick={() => {
              soundEffects.playClickSound();
              setActiveTab('minimal_pairs');
            }}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 whitespace-nowrap ${
              activeTab === 'minimal_pairs'
                ? 'bg-[#24221F] text-[#FAF7F2] shadow-sm'
                : 'bg-[#FFFFFF] text-[#5C564E] hover:bg-[#FAF7F2] border border-[#DDD4C6]'
            }`}
          >
            <span>1. Vokallängd & Minimala Par</span>
          </button>

          <button
            onClick={() => {
              soundEffects.playClickSound();
              setActiveTab('vowel_groups');
            }}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 whitespace-nowrap ${
              activeTab === 'vowel_groups'
                ? 'bg-[#24221F] text-[#FAF7F2] shadow-sm'
                : 'bg-[#FFFFFF] text-[#5C564E] hover:bg-[#FAF7F2] border border-[#DDD4C6]'
            }`}
          >
            <span>2. Hårda vs. Mjuka Vokaler</span>
          </button>

          <button
            onClick={() => {
              soundEffects.playClickSound();
              setActiveTab('pitch_accents');
            }}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 whitespace-nowrap ${
              activeTab === 'pitch_accents'
                ? 'bg-[#24221F] text-[#FAF7F2] shadow-sm'
                : 'bg-[#FFFFFF] text-[#5C564E] hover:bg-[#FAF7F2] border border-[#DDD4C6]'
            }`}
          >
            <Music className="w-3.5 h-3.5 text-[#C9862C]" />
            <span>3. Tonaccent 1 & 2</span>
          </button>

          <button
            onClick={handleStartQuiz}
            className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 whitespace-nowrap ${
              activeTab === 'listening_quiz'
                ? 'bg-[#2D5A3F] text-white shadow-sm'
                : 'bg-[#FFFFFF] text-[#2D5A3F] hover:bg-[#FAF7F2] border border-[#DDD4C6]'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5 text-[#2D5A3F]" />
            <span>4. Interaktivt Hörtest</span>
          </button>
        </div>

        {/* Modal Main Body */}
        <div className="flex-1 overflow-y-auto p-6 bg-[#FFFFFF]">
          {isLoading || !guideData ? (
            <div className="h-64 flex flex-col items-center justify-center space-y-3 text-[#8F877B]">
              <Loader2 className="w-8 h-8 animate-spin text-[#2B5876]" />
              <span className="font-editorial italic">Hämtar fonetiska ljudmodeller...</span>
            </div>
          ) : activeTab === 'minimal_pairs' ? (
            /* =======================================================================
               TAB 1: VOWEL LENGTH & MINIMAL PAIRS
               ======================================================================= */
            <div className="space-y-6 max-w-3xl mx-auto">
              <div>
                <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase block mb-1">
                  Grundläggande uttalsregel
                </span>
                <h2 className="text-2xl font-bold font-display text-[#24221F]">
                  {guideData.vowel_length_rule.title}
                </h2>
                <p className="text-xs sm:text-sm text-[#5C564E] font-sans mt-1 leading-relaxed">
                  {guideData.vowel_length_rule.description}
                </p>
              </div>

              {/* Formula Badge */}
              <div className="p-4 bg-[#F5EFEB] border border-[#DDD4C6] rounded-2xl flex items-center gap-3.5 shadow-[0_2px_0_#DDD4C6]">
                <div className="p-2.5 bg-[#FFFFFF] rounded-xl text-[#2B5876] border border-[#DDD4C6]">
                  <Sparkles className="w-4 h-4 text-[#C9862C]" />
                </div>
                <div>
                  <div className="text-[10px] font-mono-tag uppercase text-[#8F877B]">
                    Gyllene Vokalregeln
                  </div>
                  <div className="text-xs sm:text-sm font-mono font-bold text-[#24221F] mt-0.5">
                    {guideData.vowel_length_rule.formula}
                  </div>
                </div>
              </div>

              {/* Minimal Pairs Cards */}
              <div className="space-y-3">
                <h4 className="text-xs font-mono-tag uppercase text-[#8F877B] flex items-center gap-1.5">
                  <Volume2 className="w-3.5 h-3.5 text-[#2B5876]" />
                  <span>Jämför minimala par i realtid (Klicka för att lyssna):</span>
                </h4>

                <div className="grid grid-cols-1 gap-3">
                  {guideData.vowel_length_rule.minimal_pairs.map((pair: MinimalPairItem) => (
                    <div
                      key={pair.pair_id}
                      className="p-4 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl shadow-sm hover:border-[#24221F] transition space-y-2.5"
                    >
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        
                        {/* Long Vowel Box */}
                        <div className="p-3 bg-[#FFFFFF] rounded-xl border border-[#DDD4C6] flex items-center justify-between">
                          <div>
                            <div className="flex items-baseline gap-2">
                              <span className="text-lg font-bold font-display text-[#24221F]">
                                {pair.long_word}
                              </span>
                              <span className="text-xs font-mono-tag text-[#2B5876]">
                                {pair.long_ipa}
                              </span>
                              <span className="text-[10px] px-1.5 py-0.5 rounded bg-[#EEF5F9] text-[#2B5876] font-mono-tag">
                                Lång
                              </span>
                            </div>
                            <div className="text-xs text-[#5C564E] font-editorial italic mt-0.5">
                              {pair.long_translation}
                            </div>
                          </div>

                          <button
                            onClick={() => handlePlayAudio(pair.long_audio_text)}
                            title={`Lyssna på "${pair.long_word}"`}
                            className="p-2 bg-[#FAF7F2] hover:bg-[#EBF3ED] text-[#2D5A3F] border border-[#DDD4C6] rounded-xl transition shadow-sm"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>

                        {/* Short Vowel Box */}
                        <div className="p-3 bg-[#FFFFFF] rounded-xl border border-[#DDD4C6] flex items-center justify-between">
                          <div>
                            <div className="flex items-baseline gap-2">
                              <span className="text-lg font-bold font-display text-[#24221F]">
                                {pair.short_word}
                              </span>
                              <span className="text-xs font-mono-tag text-[#8A321E]">
                                {pair.short_ipa}
                              </span>
                              <span className="text-[10px] px-1.5 py-0.5 rounded bg-[#FAECE8] text-[#8A321E] font-mono-tag">
                                Kort
                              </span>
                            </div>
                            <div className="text-xs text-[#5C564E] font-editorial italic mt-0.5">
                              {pair.short_translation}
                            </div>
                          </div>

                          <button
                            onClick={() => handlePlayAudio(pair.short_audio_text)}
                            title={`Lyssna på "${pair.short_word}"`}
                            className="p-2 bg-[#FAF7F2] hover:bg-[#FAECE8] text-[#8A321E] border border-[#DDD4C6] rounded-xl transition shadow-sm"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>

                      </div>

                      <p className="text-xs text-[#8F877B] font-editorial italic pl-1">
                        💡 {pair.explanation}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ) : activeTab === 'vowel_groups' ? (
            /* =======================================================================
               TAB 2: HARD VS SOFT VOWELS (K, G, SK SOFTENING)
               ======================================================================= */
            <div className="space-y-6 max-w-3xl mx-auto">
              <div>
                <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase block mb-1">
                  Konsonant- & Vokalsamspel
                </span>
                <h2 className="text-2xl font-bold font-display text-[#24221F]">
                  Hårda och Mjuka Vokaler i Svenskan
                </h2>
                <p className="text-xs sm:text-sm text-[#5C564E] font-sans mt-1 leading-relaxed">
                  Vokalen som följer bokstäverna <strong>K, G och SK</strong> avgör om ljudet förblir hårt eller mjuknar till tj-, j- eller sje-ljud.
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                {/* Hard Vowels Card */}
                <div className="bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl p-5 space-y-4 shadow-sm">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="px-2 py-0.5 rounded bg-[#24221F] text-[#FAF7F2] font-mono-tag text-xs">
                        HÅRDA VOKALER
                      </span>
                    </div>
                    <div className="text-2xl font-bold font-display text-[#24221F] tracking-wide mt-1">
                      {guideData.vowel_groups.hard_vowels.vowels.join(' • ')}
                    </div>
                    <p className="text-xs text-[#5C564E] leading-relaxed mt-1.5">
                      {guideData.vowel_groups.hard_vowels.rule}
                    </p>
                  </div>

                  <div className="space-y-2 pt-2 border-t border-[#EDE7DD]">
                    <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase">Exempel:</span>
                    {guideData.vowel_groups.hard_vowels.examples.map((ex, i) => (
                      <div
                        key={i}
                        className="flex items-center justify-between p-2.5 bg-[#FFFFFF] border border-[#DDD4C6] rounded-xl text-xs"
                      >
                        <div>
                          <strong className="text-[#24221F] font-display text-sm">{ex.word}</strong>
                          <span className="text-[#8F877B] font-mono-tag ml-2">{ex.pronunciation}</span>
                          <span className="text-[#5C564E] block text-[11px] font-editorial italic">{ex.translation}</span>
                        </div>
                        <button
                          onClick={() => handlePlayAudio(ex.word)}
                          className="p-1.5 text-[#2B5876] hover:bg-[#F5EFEB] rounded-lg transition"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Soft Vowels Card */}
                <div className="bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl p-5 space-y-4 shadow-sm">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <span className="px-2 py-0.5 rounded bg-[#C9862C] text-white font-mono-tag text-xs">
                        MJUKA VOKALER
                      </span>
                    </div>
                    <div className="text-2xl font-bold font-display text-[#24221F] tracking-wide mt-1">
                      {guideData.vowel_groups.soft_vowels.vowels.join(' • ')}
                    </div>
                    <p className="text-xs text-[#5C564E] leading-relaxed mt-1.5">
                      {guideData.vowel_groups.soft_vowels.rule}
                    </p>
                  </div>

                  <div className="space-y-2 pt-2 border-t border-[#EDE7DD]">
                    <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase">Exempel:</span>
                    {guideData.vowel_groups.soft_vowels.examples.map((ex, i) => (
                      <div
                        key={i}
                        className="flex items-center justify-between p-2.5 bg-[#FFFFFF] border border-[#DDD4C6] rounded-xl text-xs"
                      >
                        <div>
                          <strong className="text-[#24221F] font-display text-sm">{ex.word}</strong>
                          <span className="text-[#995E15] font-mono-tag ml-2">{ex.pronunciation}</span>
                          <span className="text-[#5C564E] block text-[11px] font-editorial italic">{ex.translation}</span>
                        </div>
                        <button
                          onClick={() => handlePlayAudio(ex.word)}
                          className="p-1.5 text-[#2B5876] hover:bg-[#F5EFEB] rounded-lg transition"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    ))}
                  </div>
                </div>

              </div>
            </div>
          ) : activeTab === 'pitch_accents' ? (
            /* =======================================================================
               TAB 3: PITCH ACCENTS (MELODI: ACCENT 1 VS ACCENT 2)
               ======================================================================= */
            <div className="space-y-6 max-w-3xl mx-auto">
              <div>
                <span className="text-[10px] font-mono-tag text-[#8F877B] uppercase block mb-1">
                  Svensk språkmelodi
                </span>
                <h2 className="text-2xl font-bold font-display text-[#24221F]">
                  {guideData.pitch_accents.title}
                </h2>
                <p className="text-xs sm:text-sm text-[#5C564E] font-sans mt-1 leading-relaxed">
                  {guideData.pitch_accents.description}
                </p>
              </div>

              <div className="space-y-3">
                {guideData.pitch_accents.pairs.map((p, idx) => (
                  <div
                    key={idx}
                    className="p-5 bg-[#FAF7F2] border border-[#DDD4C6] rounded-2xl shadow-sm space-y-3"
                  >
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      
                      {/* Accent 1 Card */}
                      <div className="p-3.5 bg-[#FFFFFF] border border-[#DDD4C6] rounded-xl flex items-center justify-between">
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="text-lg font-bold font-display text-[#24221F]">
                              {p.word_1}
                            </span>
                            <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#EEF5F9] text-[#2B5876]">
                              {p.accent_1}
                            </span>
                          </div>
                          <p className="text-xs text-[#5C564E] font-editorial italic mt-1">
                            {p.meaning_1}
                          </p>
                        </div>
                        <button
                          onClick={() => handlePlayAudio(p.audio_text_1)}
                          className="p-2 bg-[#FAF7F2] hover:bg-[#EEF5F9] text-[#2B5876] border border-[#DDD4C6] rounded-xl transition shadow-sm"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>

                      {/* Accent 2 Card */}
                      <div className="p-3.5 bg-[#FFFFFF] border border-[#DDD4C6] rounded-xl flex items-center justify-between">
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="text-lg font-bold font-display text-[#24221F]">
                              {p.word_2}
                            </span>
                            <span className="text-[10px] font-mono-tag px-2 py-0.5 rounded bg-[#FDF6EA] text-[#995E15]">
                              {p.accent_2}
                            </span>
                          </div>
                          <p className="text-xs text-[#5C564E] font-editorial italic mt-1">
                            {p.meaning_2}
                          </p>
                        </div>
                        <button
                          onClick={() => handlePlayAudio(p.audio_text_2)}
                          className="p-2 bg-[#FAF7F2] hover:bg-[#FDF6EA] text-[#995E15] border border-[#DDD4C6] rounded-xl transition shadow-sm"
                        >
                          <Volume2 className="w-4 h-4" />
                        </button>
                      </div>

                    </div>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            /* =======================================================================
               TAB 4: INTERACTIVE LISTENING QUIZ (HÖRFÖRSTÅELSE)
               ======================================================================= */
            <div className="max-w-xl mx-auto space-y-6">
              {isQuizFinished ? (
                /* Celebration Card */
                <div className="text-center py-8 space-y-6 animate-in zoom-in-95">
                  <div className="w-18 h-18 mx-auto rounded-3xl bg-[#EBF3ED] border-2 border-[#2D5A3F] flex items-center justify-center text-[#2D5A3F] shadow-[0_4px_0_#2D5A3F]">
                    <Award className="w-9 h-9" />
                  </div>

                  <div className="space-y-1.5">
                    <h2 className="text-2xl font-bold font-display text-[#24221F]">Hörtestet är slutfört!</h2>
                    <p className="text-xs text-[#5C564E] font-editorial italic">
                      Du fick {correctQuizCount} av {quizListLength} rätt på ljudigenkänningen.
                    </p>
                  </div>

                  <div className="flex justify-center gap-3 pt-2">
                    <button
                      onClick={handleStartQuiz}
                      className="py-3.5 px-6 btn-craft btn-stamp-forest flex items-center justify-center gap-2 text-xs font-bold"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>Gör testet igen</span>
                    </button>
                  </div>
                </div>
              ) : currentQuizQuestion ? (
                /* Active Question */
                <div className="space-y-5 animate-in fade-in">
                  
                  {/* Progress */}
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-mono-tag font-bold text-[#2B5876]">
                      Ljudfråga {currentQuizIndex + 1} av {quizListLength}
                    </span>
                    <span className="text-[#8F877B] font-mono-tag">
                      Poäng: {correctQuizCount} rätt
                    </span>
                  </div>

                  <div className="bg-[#FAF7F2] border border-[#DDD4C6] p-6 rounded-3xl space-y-5 shadow-[0_2px_0_#EADFCF]">
                    <div>
                      <span className="text-[10px] font-mono-tag uppercase text-[#8F877B] block mb-1">
                        Hörövning
                      </span>
                      <h3 className="text-base sm:text-lg font-bold font-display text-[#24221F]">
                        {currentQuizQuestion.prompt}
                      </h3>
                    </div>

                    {/* Audio Player Trigger */}
                    <div className="flex justify-center py-2">
                      <button
                        onClick={() => handlePlayAudio(currentQuizQuestion.audio_text)}
                        className="px-6 py-3.5 bg-[#FFFFFF] hover:bg-[#F5EFEB] text-[#2B5876] border-2 border-[#DDD4C6] rounded-2xl flex items-center gap-2.5 btn-craft shadow-[0_3px_0_#DDD4C6] transition"
                      >
                        <Volume2 className="w-6 h-6 stroke-[2.2]" />
                        <span className="text-sm font-bold">Spela upp ljudprovet</span>
                      </button>
                    </div>

                    {/* Options */}
                    <div className="space-y-2.5 pt-2">
                      {currentQuizQuestion.options.map((opt, idx) => {
                        const isSelected = selectedQuizOption === opt;
                        const isCorrect =
                          opt.trim().toLowerCase() === currentQuizQuestion.correct_answer.trim().toLowerCase();

                        let btnStyle =
                          'bg-[#FFFFFF] border-[#DDD4C6] text-[#24221F] hover:bg-[#FAF7F2] hover:border-[#24221F] shadow-[0_2px_0_#DDD4C6]';
                        if (isQuizAnswerSubmitted) {
                          if (isCorrect) {
                            btnStyle =
                              'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] font-bold shadow-[0_2px_0_#2D5A3F]';
                          } else if (isSelected) {
                            btnStyle =
                              'bg-[#FAECE8] border-[#B34B32] text-[#8A321E] font-bold shadow-[0_2px_0_#B34B32]';
                          }
                        } else if (isSelected) {
                          btnStyle =
                            'bg-[#EBF3ED] border-[#2D5A3F] text-[#2D5A3F] font-bold shadow-[0_2px_0_#2D5A3F]';
                        }

                        return (
                          <button
                            key={idx}
                            onClick={() => handleSelectQuizOption(opt)}
                            disabled={isQuizAnswerSubmitted}
                            className={`w-full text-left p-3.5 rounded-2xl border transition flex items-center justify-between text-xs sm:text-sm ${btnStyle}`}
                          >
                            <span>{opt}</span>
                            {isQuizAnswerSubmitted && isCorrect && (
                              <CheckCircle2 className="w-4 h-4 text-[#2D5A3F]" />
                            )}
                          </button>
                        );
                      })}
                    </div>

                    {/* Explanation */}
                    {isQuizAnswerSubmitted && (
                      <div className="p-4 bg-[#FFFFFF] rounded-2xl border border-[#DDD4C6] space-y-1 animate-in fade-in">
                        <div className="text-xs font-bold text-[#2D5A3F] flex items-center gap-1.5 font-mono-tag">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          <span>Fonetisk förklaring:</span>
                        </div>
                        <p className="text-xs text-[#5C564E] leading-relaxed font-sans">
                          {currentQuizQuestion.explanation}
                        </p>
                      </div>
                    )}

                    {/* Action Button */}
                    {!isQuizAnswerSubmitted ? (
                      <button
                        onClick={handleSubmitQuizAnswer}
                        disabled={!selectedQuizOption}
                        className="w-full py-3.5 btn-craft btn-stamp-forest disabled:opacity-50 text-xs font-bold"
                      >
                        Kontrollera svar
                      </button>
                    ) : (
                      <button
                        onClick={handleNextQuizQuestion}
                        className="w-full py-3.5 btn-craft btn-stamp-dark flex items-center justify-center gap-2 text-xs font-bold"
                      >
                        <span>
                          {currentQuizIndex + 1 < quizListLength ? 'Nästa ljudfråga' : 'Slutför hörtest'}
                        </span>
                        <ArrowRight className="w-4 h-4" />
                      </button>
                    )}
                  </div>
                </div>
              ) : null}
            </div>
          )}
        </div>

      </div>
    </div>
  );
};
