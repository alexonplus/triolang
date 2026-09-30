import React, { useState } from 'react';
import { Volume2, RefreshCw, Quote, BookOpen } from 'lucide-react';
import { speakText, soundEffects } from '../services/audio';

export interface IdiomItem {
  id: string;
  language: 'sv' | 'en';
  phrase: string;
  literal: string;
  meaning: string;
  context: string;
  tag: string;
}

const DAILY_IDIOMS: IdiomItem[] = [
  {
    id: 'sv-1',
    language: 'sv',
    phrase: 'Glida in på en räkmacka',
    literal: 'To slide in on a shrimp sandwich',
    meaning: 'Att nå framgång enkelt och utan egen ansträngning (To achieve effortless success).',
    context: 'Mycket vanligt svenskt uttryck om någon som får fördelar gratis eller har tur i karriären.',
    tag: 'Klassiskt idiom',
  },
  {
    id: 'sv-2',
    language: 'sv',
    phrase: 'Finns det hjärterum så finns det stjärterum',
    literal: 'If there is room in the heart, there is room for the buttocks',
    meaning: 'Är man välkomnande och vänlig så finns det alltid plats för en till (There is always room for one more).',
    context: 'Sägs ofta när man tränger ihop sig runt middagsbordet eller i fikasoffan.',
    tag: 'Ordspråk & Gästfrihet',
  },
  {
    id: 'sv-3',
    language: 'sv',
    phrase: 'Det är ingen ko på isen (så länge rumpan är på land)',
    literal: 'There is no cow on the ice (as long as its backside is on land)',
    meaning: 'Det är ingen fara eller brådska, situationen är under kontroll (No reason to panic).',
    context: 'Används för att lugna ner kollegor eller vänner när problem uppstår.',
    tag: 'Vardagsuttryck',
  },
  {
    id: 'sv-4',
    language: 'sv',
    phrase: 'Att ana ugglor i mossen',
    literal: 'To suspect owls in the bog (originally wolves in Danish)',
    meaning: 'Att ana oråd eller misstänka att något lurt är på gång (To smell a rat).',
    context: 'Historiskt språkuttryck som används när något verkar misstänkt.',
    tag: 'Folkligt idiom',
  },
  {
    id: 'sv-5',
    language: 'sv',
    phrase: 'Att ha skägget i brevlådan',
    literal: 'To have one’s beard caught in the letterbox',
    meaning: 'Att bli ertappad på bar gärning eller hamna i en knivig sits (To be caught red-handed).',
    context: 'Roligt bildligt uttryck när någon försatt sig i en pinsam situation.',
    tag: 'Humor & Bildspråk',
  },
  {
    id: 'sv-6',
    language: 'sv',
    phrase: 'Smaken är som baken – delad',
    literal: 'Taste is like the buttocks – divided',
    meaning: 'Alla tycker olika och har olika preferenser (To each their own / tastes differ).',
    context: 'Sägs med glimten i ögat när man diskuterar mat, musik eller design.',
    tag: 'Kultursanning',
  },
  {
    id: 'en-1',
    language: 'en',
    phrase: 'Bite the bullet',
    literal: 'Att bita i kulan',
    meaning: 'Att ta tag i en obehaglig eller svår uppgift med mod (Face a tough situation bravely).',
    context: 'Originated from soldiers biting lead bullets during battlefield surgery.',
    tag: 'Classic Idiom',
  },
  {
    id: 'en-2',
    language: 'en',
    phrase: 'Every cloud has a silver lining',
    literal: 'Varje moln har en silverkant',
    meaning: 'Även i motgång finns det alltid något positivt att finna (Optimism in adversity).',
    context: 'Common comforting phrase encouraging optimism in tough times.',
    tag: 'Proverb & Wisdom',
  },
];

interface DailyWisdomCardProps {
  language?: string;
}

export const DailyWisdomCard: React.FC<DailyWisdomCardProps> = ({ language = 'sv' }) => {
  const targetLang = language.startsWith('en') ? 'en' : 'sv';
  const filteredIdioms = DAILY_IDIOMS.filter((i) => i.language === targetLang);
  const [currentIndex, setCurrentIndex] = useState(0);

  const currentIdiom = filteredIdioms[currentIndex % filteredIdioms.length] || DAILY_IDIOMS[0];

  const handleNext = () => {
    soundEffects.playClickSound();
    setCurrentIndex((prev) => (prev + 1) % filteredIdioms.length);
  };

  const handlePlayAudio = () => {
    speakText(currentIdiom.phrase, currentIdiom.language);
  };

  return (
    <div className="bg-[#FFFFFF] border border-[#DDD4C6] rounded-2xl p-5 mb-8 shadow-[0_2px_0_#EADFCF] relative overflow-hidden transition-all">
      {/* Decorative Stamp Tag */}
      <div className="flex items-center justify-between gap-2 mb-3">
        <div className="flex items-center gap-2">
          <div className="w-7 h-7 rounded-lg bg-[#FAF7F2] border border-[#DDD4C6] flex items-center justify-center text-[#C9862C]">
            <Quote className="w-3.5 h-3.5" />
          </div>
          <div>
            <span className="text-[10px] font-mono-tag uppercase text-[#8F877B] block leading-none">
              Dagens Visdomsord & Idiom
            </span>
            <span className="text-xs font-bold text-[#24221F] font-display">
              {currentIdiom.tag}
            </span>
          </div>
        </div>

        <div className="flex items-center gap-1.5">
          <button
            onClick={handlePlayAudio}
            title="Lyssna på uttal"
            className="p-1.5 bg-[#FAF7F2] hover:bg-[#F5EFEB] border border-[#DDD4C6] rounded-xl text-[#2B5876] transition shadow-sm"
          >
            <Volume2 className="w-4 h-4" />
          </button>
          <button
            onClick={handleNext}
            title="Visa nästa ordspråk"
            className="flex items-center gap-1 px-2.5 py-1.5 bg-[#FAF7F2] hover:bg-[#F5EFEB] border border-[#DDD4C6] rounded-xl text-[#5C564E] text-xs font-bold transition shadow-sm"
          >
            <RefreshCw className="w-3 h-3 text-[#8F877B]" />
            <span>Nästa</span>
          </button>
        </div>
      </div>

      {/* Main Phrase Quote */}
      <div className="space-y-1.5 pt-1">
        <h3 className="text-lg sm:text-xl font-bold font-display text-[#24221F] tracking-tight flex items-baseline gap-2">
          <span>&quot;{currentIdiom.phrase}&quot;</span>
        </h3>
        
        <div className="text-xs text-[#8F877B] font-editorial italic">
          Bokstavligt: &quot;{currentIdiom.literal}&quot;
        </div>

        <p className="text-xs sm:text-sm text-[#5C564E] font-sans leading-relaxed pt-1">
          {currentIdiom.meaning}
        </p>

        <div className="text-[11px] text-[#8F877B] pt-2 border-t border-[#EDE7DD] flex items-center gap-1.5 font-editorial">
          <BookOpen className="w-3.5 h-3.5 text-[#C9862C] shrink-0" />
          <span>{currentIdiom.context}</span>
        </div>
      </div>
    </div>
  );
};
