import { useState, useEffect } from 'react';

function TimetableList() {
  const [timetables, setTimetables] = useState([]);

  useEffect(() => {
    // Fetch timetables data from the backend
    fetchTimetables();
  }, []);

  const fetchTimetables = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/timetables/');
      if (!response.ok) {
        throw new Error('Failed to fetch timetables');
      }
      const data = await response.json();
      setTimetables(data);
      console.log('Timetables:', data); // Log the entire timetable object array
    } catch (error) {
      console.error('Error fetching timetables:', error);
    }
  };

  const sessionTypes = [...new Set(timetables.map((timetable) => timetable.session_type))];

  return (
    <div className="w-full overflow-auto rounded-lg shadow-md">
      <h2>Timetables</h2>
      {sessionTypes.map((sessionType) => (
        <div key={sessionType} className="border-b border-gray-200 px-4 py-2">
          <h3>{sessionType} Session</h3>
          <table className="w-full table-auto">
            <thead>
              <tr className="text-left bg-gray-100 font-medium">
                <th className="px-4 py-2">Day</th>
                <th className="px-4 py-2">Time</th>
                <th className="px-4 py-2">Class Group</th>
                <th className="px-4 py-2">Lecture Hall</th>
                <th className="px-4 py-2">Lecturer</th>
              </tr>
            </thead>
            <tbody>
              {timetables
                .filter((timetable) => timetable.session_type === sessionType)
                .map((timetable) => (
                  <tr key={timetable.id} className="border-b border-gray-200 hover:bg-gray-100">
                    <td className="px-4 py-2">{timetable.day}</td>
                    <td className="px-4 py-2">{timetable.time_start} - {timetable.time_end}</td>
                    <td className="px-4 py-2">{timetable.class_group?.group_name}</td>
                    <td className="px-4 py-2">{timetable.lecture_hall?.name}</td>
                    <td className="px-4 py-2">{timetable.lecturer?.name}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      ))}
    </div>
  );
}

export default TimetableList;


