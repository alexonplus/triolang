import type {
  UserStats,
  Course,
  Unit,
  LessonDetail,
  AnswerSubmitResponse,
  LessonCompleteResponse,
  AITutorResponse,
  GenerateLessonResponse,
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
};
