import type {
  UserStats,
  Course,
  Unit,
  LessonDetail,
  AnswerSubmitResponse,
  LessonCompleteResponse,
  AITutorResponse,
  GenerateLessonResponse,
  PlacementQuestionItem,
  PlacementDialogueTurn,
  PlacementEvaluationResponse,
  GrammarTopicSummary,
  GrammarTopicDetail,
  GrammarPracticeDrillsResponse,
} from '../types';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

async function fetchJson<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const url = `${API_BASE_URL}${endpoint}`;
  try {
    const res = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options?.headers,
      },
    });

    if (!res.ok) {
      const errorBody = await res.text();
      throw new Error(`API Error ${res.status}: ${errorBody || res.statusText}`);
    }

    return (await res.json()) as T;
  } catch (err) {
    console.error(`Fetch failed for ${endpoint}:`, err);
    throw err;
  }
}

export const api = {
  getUser: () => fetchJson<UserStats>('/user'),
  
  switchCourse: (courseId: string) =>
    fetchJson<UserStats>('/user/active-course', {
      method: 'POST',
      body: JSON.stringify({ course_id: courseId }),
    }),

  refillHearts: () =>
    fetchJson<UserStats>('/user/refill-hearts', {
      method: 'POST',
    }),

  getCourses: () => fetchJson<Course[]>('/courses'),

  getUnits: (courseId: string) =>
    fetchJson<Unit[]>(`/courses/${courseId}/units`),

  getLessonDetail: (lessonId: number) =>
    fetchJson<LessonDetail>(`/lessons/${lessonId}`),

  submitAnswer: (exerciseId: number, userAnswer: string) =>
    fetchJson<AnswerSubmitResponse>('/exercises/submit', {
      method: 'POST',
      body: JSON.stringify({ exercise_id: exerciseId, user_answer: userAnswer }),
    }),

  completeLesson: (lessonId: number, accuracyPercentage: number = 100) =>
    fetchJson<LessonCompleteResponse>('/lessons/complete', {
      method: 'POST',
      body: JSON.stringify({
        lesson_id: lessonId,
        accuracy_percentage: accuracyPercentage,
      }),
    }),

  askAITutor: (query: string, targetLanguage: string = 'sv', context?: string) =>
    fetchJson<AITutorResponse>('/ai/tutor', {
      method: 'POST',
      body: JSON.stringify({
        query,
        target_language: targetLanguage,
        context,
      }),
    }),

  generateAILesson: (topic: string, courseId: string = 'sv-from-en') =>
    fetchJson<GenerateLessonResponse>('/ai/generate-lesson', {
      method: 'POST',
      body: JSON.stringify({
        topic,
        course_id: courseId,
      }),
    }),

  getPlacementQuestions: (courseId: string = 'sv-from-en') =>
    fetchJson<PlacementQuestionItem[]>(`/ai/placement-questions?course_id=${encodeURIComponent(courseId)}`),

  evaluatePlacementTest: (dialogue: PlacementDialogueTurn[], courseId: string = 'sv-from-en') =>
    fetchJson<PlacementEvaluationResponse>('/ai/diagnostic-evaluate', {
      method: 'POST',
      body: JSON.stringify({
        dialogue,
        course_id: courseId,
      }),
    }),

  getGrammarTopics: (language?: string, level?: string) => {
    const params = new URLSearchParams();
    if (language) params.append('language', language);
    if (level) params.append('level', level);
    const query = params.toString() ? `?${params.toString()}` : '';
    return fetchJson<GrammarTopicSummary[]>(`/grammar/topics${query}`);
  },

  getGrammarTopicDetail: (topicId: string) =>
    fetchJson<GrammarTopicDetail>(`/grammar/topics/${encodeURIComponent(topicId)}`),

  getGrammarPracticeDrills: (topicId: string) =>
    fetchJson<GrammarPracticeDrillsResponse>(`/grammar/topics/${encodeURIComponent(topicId)}/drills`),

  generateGrammarAIDrills: (topicId: string, customPrompt?: string) =>
    fetchJson<GrammarPracticeDrillsResponse>(`/grammar/topics/${encodeURIComponent(topicId)}/generate-drills`, {
      method: 'POST',
      body: JSON.stringify({ custom_prompt: customPrompt }),
    }),
};
