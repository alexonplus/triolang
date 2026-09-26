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

