import React, { useState, useEffect } from 'react';
import type { UserStats, Course, Unit, LessonDetail, LessonCompleteResponse } from './types';
import { api } from './services/api';
import { Header } from './components/Header';
import { LessonMap } from './components/LessonMap';
import { ExerciseSession } from './components/ExerciseSession';
import { LessonCompleteModal } from './components/LessonCompleteModal';
import { AITutorModal } from './components/AITutorModal';
import { GenerateLessonModal } from './components/GenerateLessonModal';
import { PlacementTestModal } from './components/PlacementTestModal';
import { Loader2, AlertCircle, RefreshCw } from 'lucide-react';

export const App: React.FC = () => {
  const [user, setUser] = useState<UserStats | null>(null);
  const [courses, setCourses] = useState<Course[]>([]);
  const [activeCourseId, setActiveCourseId] = useState<string>('sv-from-en');
  const [units, setUnits] = useState<Unit[]>([]);
  
  const [activeLesson, setActiveLesson] = useState<LessonDetail | null>(null);
  const [completeSummary, setCompleteSummary] = useState<LessonCompleteResponse | null>(null);
  const [isAITutorOpen, setIsAITutorOpen] = useState(false);
  const [isGenerateModalOpen, setIsGenerateModalOpen] = useState(false);
  const [isPlacementModalOpen, setIsPlacementModalOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadInitialData = async () => {
    try {
      setLoading(true);
      setError(null);

      const [userData, coursesData] = await Promise.all([
        api.getUser(),
        api.getCourses(),
      ]);

      setUser(userData);
      setCourses(coursesData);

      const targetCourseId = userData.active_course_id || coursesData[0]?.id || 'sv-from-en';
      setActiveCourseId(targetCourseId);

      const unitsData = await api.getUnits(targetCourseId);
      setUnits(unitsData);
    } catch (err: unknown) {
      console.error('Failed to load initial data:', err);
      setError('Could not connect to TrioLang backend. Please ensure the Python API server is running.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadInitialData();
  }, []);

  const handleSelectCourse = async (newCourseId: string) => {
    try {
      setActiveCourseId(newCourseId);
      const updatedUser = await api.switchCourse(newCourseId);
      setUser(updatedUser);
      const unitsData = await api.getUnits(newCourseId);
      setUnits(unitsData);
    } catch (err) {
      console.error('Failed to switch course:', err);
    }
  };

  const handleLessonGenerated = async () => {
    try {
      const unitsData = await api.getUnits(activeCourseId);
      setUnits(unitsData);
    } catch (err) {
      console.error('Failed to reload units after generation:', err);
    }
  };

  const handleRefillHearts = async () => {
    try {
      const updatedUser = await api.refillHearts();
      setUser(updatedUser);
    } catch (err) {
      console.error('Failed to refill hearts:', err);
    }
  };

  const handleStartLesson = async (lessonId: number) => {
    try {
      const lessonDetail = await api.getLessonDetail(lessonId);
      setActiveLesson(lessonDetail);
    } catch (err) {
      console.error('Failed to start lesson:', err);
    }
  };

  const handleLessonCompleted = (summary: LessonCompleteResponse) => {
    setCompleteSummary(summary);
  };

  const handleCloseCompletion = async () => {
    setCompleteSummary(null);
    setActiveLesson(null);
    await loadInitialData();
  };

  const activeCourse = courses.find((c) => c.id === activeCourseId) || courses[0];

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center p-4">
        <Loader2 className="w-12 h-12 text-emerald-400 animate-spin mb-4" />
        <h2 className="text-xl font-black text-white">Välkommen till TrioLang</h2>
        <p className="text-slate-400 text-sm mt-1">Connecting to Python FastAPI backend...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center p-4 text-center">
        <div className="bg-slate-800 border border-slate-700 p-8 rounded-3xl max-w-md w-full space-y-4">
          <AlertCircle className="w-12 h-12 text-rose-400 mx-auto" />
          <h2 className="text-xl font-black text-white">Connection Error</h2>
          <p className="text-sm text-slate-400">{error}</p>
          <button
            onClick={loadInitialData}
            className="w-full py-3 bg-emerald-500 hover:bg-emerald-400 font-black text-white rounded-xl flex items-center justify-center gap-2 btn-3d shadow-[0_3px_0_#047857]"
          >
            <RefreshCw className="w-4 h-4" />
            <span>Try Again</span>
          </button>
        </div>
      </div>
    );
  }

  if (activeLesson) {
    return (
      <ExerciseSession
        lesson={activeLesson}
        hearts={user?.hearts ?? 5}
        onQuit={() => setActiveLesson(null)}
        onComplete={handleLessonCompleted}
        onHeartsUpdate={(newHearts) => {
          if (user) {
            setUser({ ...user, hearts: newHearts });
          }
        }}
      />
    );
  }

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex flex-col">
      <Header
        user={user}
        courses={courses}
        currentCourseId={activeCourseId}
        onSelectCourse={handleSelectCourse}
        onOpenAITutor={() => setIsAITutorOpen(true)}
        onOpenPlacementTest={() => setIsPlacementModalOpen(true)}
        onRefillHearts={handleRefillHearts}
      />

      <main className="flex-1">
        <LessonMap
          units={units}
          activeCourseTitle={
            activeCourse
              ? `${activeCourse.native_title} (${activeCourse.title})`
              : 'Swedish (Svenska)'
          }
          onStartLesson={handleStartLesson}
          onOpenGenerateModal={() => setIsGenerateModalOpen(true)}
        />
      </main>

      {isPlacementModalOpen && (
        <PlacementTestModal
          courseId={activeCourseId}
          courseTitle={activeCourse?.native_title || 'Swedish'}
          onClose={() => setIsPlacementModalOpen(false)}
          onCustomPathGenerated={async () => {
            const unitsData = await api.getUnits(activeCourseId);
            setUnits(unitsData);
          }}
        />
      )}

      {isGenerateModalOpen && (
        <GenerateLessonModal
          courseId={activeCourseId}
          courseTitle={activeCourse?.native_title || 'Swedish'}
          onClose={() => setIsGenerateModalOpen(false)}
          onLessonGenerated={handleLessonGenerated}
        />
      )}

      {completeSummary && (
        <LessonCompleteModal
          summary={completeSummary}
          onFinish={handleCloseCompletion}
        />
      )}

      {isAITutorOpen && (
        <AITutorModal
          targetLanguage={activeCourse?.target_language || 'sv'}
          onClose={() => setIsAITutorOpen(false)}
        />
      )}
    </div>
  );
};

export default App;
