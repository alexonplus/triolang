export interface UserStats {
  id: number;
  username: string;
  hearts: number;
  gems: number;
  total_xp: number;
  streak_days: number;
  active_course_id: string;
}

export interface Course {
  id: string;
  title: string;
  native_title: string;
  flag_emoji: string;
  target_language: string;
  source_language: string;
  description: string;
  units_count: number;
  completed_lessons_count: number;
}

export interface LessonSummary {
  id: number;
  unit_id: number;
  order_index: number;
  title: string;
  swedish_title: string;
  xp_reward: number;
  is_completed: boolean;
  is_locked: boolean;
}

export interface Unit {
  id: number;
  course_id: string;
  order_index: number;
  title: string;
  swedish_title: string;
  description: string;
  icon_name: string;
  theme_color: string;
  lessons: LessonSummary[];
}

export type ExerciseType = 'multiple_choice' | 'word_bank' | 'pair_match' | 'listen_transcribe';

export interface Exercise {
  id: number;
  lesson_id: number;
  order_index: number;
  exercise_type: ExerciseType;
  prompt_text: string;
  target_audio_text?: string;
  target_language: string;
  correct_answer: string;
  options?: string[];
  word_bank?: string[];
  pairs?: Record<string, string>;
  explanation?: string;
}

export interface LessonDetail extends LessonSummary {
  exercises: Exercise[];
}

export interface AnswerSubmitResponse {
  is_correct: boolean;
  correct_answer: string;
  explanation?: string;
  xp_earned: number;
  hearts_remaining: number;
  gems_earned: number;
}

export interface LessonCompleteResponse {
  lesson_id: number;
  xp_gained: number;
  new_total_xp: number;
  new_streak: number;
  gems_awarded: number;
  message: string;
}

export interface AITutorResponse {
  reply: string;
  suggested_followups: string[];
  swedish_vocabulary: Array<{ word: string; translation: string }>;
}

export interface GenerateLessonResponse {
  success: boolean;
  unit_id: number;
  lesson_id: number;
  title: string;
  swedish_title: string;
  exercise_count: number;
  source: string;
}

export interface PlacementQuestionItem {
  order_index: number;
  prompt: string;
  english_hint: string;
  grammar_target: string;
}

export interface PlacementDialogueTurn {
  sender: 'AI' | 'User';
  text: string;
}

export interface PlacementEvaluationResponse {
  cefr_level: string;
  level_title: string;
  strengths: string[];
  weaknesses: string[];
  message: string;
  units_generated_count: number;
}

export interface GrammarExample {
  swedish: string;
  english: string;
  target_highlight?: string;
}

export interface GrammarExerciseItem {
  id: number;
  type: string;
  prompt: string;
  options?: string[];
  correct_answer: string;
  explanation?: string;
}

export interface GrammarTopicSummary {
  id: string;
  language: string;
  level: string;
  title: string;
  swedish_title: string;
  summary: string;
  formula: string;
}

export interface GrammarTopicDetail extends GrammarTopicSummary {
  rule_explanation: string;
  examples: GrammarExample[];
  common_pitfalls: string[];
  exercises_count: number;
}

export interface GrammarPracticeDrillsResponse {
  topic_id: string;
  topic_title: string;
  level: string;
  exercises: GrammarExerciseItem[];
}

export interface TenseExample {
  swedish: string;
  english: string;
  target_highlight?: string;
}

export interface TenseExerciseItem {
  id: number;
  type: string;
  prompt: string;
  options?: string[];
  correct_answer: string;
  explanation?: string;
}

export interface TenseSummary {
  id: string;
  language: string;
  time_aspect: string; // 'past' | 'present' | 'future'
  title: string;
  swedish_title: string;
  level: string;
  summary: string;
  formula: string;
  signal_words: string[];
  timeline_description: string;
  mastery_percentage: number;
  attempts_count: number;
}

export interface TenseDetail extends TenseSummary {
  examples: TenseExample[];
  common_pitfalls: string[];
  exercises_count: number;
}

export interface TenseDrillsResponse {
  tense_id: string;
  tense_title: string;
  language: string;
  time_aspect: string;
  exercises: TenseExerciseItem[];
}

export interface TenseDrillSubmitResponse {
  is_correct: boolean;
  correct_answer: string;
  explanation?: string;
  xp_earned: number;
  new_mastery_percentage: number;
  ai_memory_feedback?: string;
}

export interface AIMemoryProfileResponse {
  username: string;
  overall_accuracy: number;
  detected_strengths: string[];
  detected_weaknesses: string[];
  recommended_focus_tenses: string[];
  total_mistakes_logged: number;
  ai_coaching_note: string;
}

export interface DialogueScenarioSummary {
  id: string;
  language: string;
  title: string;
  swedish_title: string;
  level: string;
  category: string;
  persona_name: string;
  avatar_emoji: string;
  scenario_context: string;
  suggested_chips: string[];
  target_grammar: string;
}

export interface GrammarCorrectionFeedback {
  has_errors: boolean;
  original_text: string;
  corrected_text?: string;
  grammar_rule_explanation?: string;
  improved_native_alternative?: string;
  highlighted_issues: string[];
}

export interface DialogueTurnMessage {
  sender: 'AI' | 'User';
  text: string;
  translation?: string;
  correction_feedback?: GrammarCorrectionFeedback;
  timestamp?: string;
}

export interface DialogueStartResponse {
  scenario_id: string;
  persona_name: string;
  avatar_emoji: string;
  scenario_title: string;
  initial_message: DialogueTurnMessage;
  suggested_chips: string[];
}

export interface DialogueTurnResponse {
  ai_reply: DialogueTurnMessage;
  correction_feedback?: GrammarCorrectionFeedback;
  suggested_next_chips: string[];
}

export interface MinimalPairItem {
  pair_id: string;
  long_word: string;
  long_ipa: string;
  long_translation: string;
  long_audio_text: string;
  short_word: string;
  short_ipa: string;
  short_translation: string;
  short_audio_text: string;
  explanation: string;
}

export interface VowelLengthRule {
  title: string;
  description: string;
  formula: string;
  minimal_pairs: MinimalPairItem[];
}

export interface VowelExample {
  word: string;
  pronunciation: string;
  translation: string;
}

export interface VowelGroupItem {
  title: string;
  vowels: string[];
  rule: string;
  examples: VowelExample[];
}

export interface VowelGroups {
  hard_vowels: VowelGroupItem;
  soft_vowels: VowelGroupItem;
}

export interface PitchAccentPair {
  word_1: string;
  accent_1: string;
  meaning_1: string;
  audio_text_1: string;
  word_2: string;
  accent_2: string;
  meaning_2: string;
  audio_text_2: string;
}

export interface PitchAccents {
  title: string;
  description: string;
  pairs: PitchAccentPair[];
}

export interface ListeningQuizQuestion {
  id: number;
  prompt: string;
  target_word: string;
  audio_text: string;
  options: string[];
  correct_answer: string;
  explanation: string;
}

export interface PronunciationGuideResponse {
  language: string;
  vowel_length_rule: VowelLengthRule;
  vowel_groups: VowelGroups;
  pitch_accents: PitchAccents;
  listening_quiz: ListeningQuizQuestion[];
}




