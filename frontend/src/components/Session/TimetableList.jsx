{/*import { useState, useEffect } from 'react';
import axios from 'axios';

function TimetableList() {
  const [timetables, setTimetables] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/timetables/')
      .then(response => {
        console.log('Response data:', response.data);
        setTimetables(response.data);
      })
      .catch(error => {
        console.error('Error fetching timetables:', error);
      });
  }, []);

  return (
    <div className="container mx-auto py-8">
      <h2 className="text-2xl font-bold mb-4">Timetables</h2>
      <div className="overflow-x-auto">
        <table className="table-auto w-full">
          <thead>
            <tr>
              <th className="px-4 py-2">Department</th>
              <th className="px-4 py-2">Level</th>
              <th className="px-4 py-2">Class Group</th>
              <th className="px-4 py-2">Lecture Hall</th>
              <th className="px-4 py-2">Day</th>
              <th className="px-4 py-2">Time</th>
              <th className="px-4 py-2">Lecturer</th>
              <th className="px-4 py-2">Session Type</th>
            </tr>
          </thead>
          <tbody>
            {timetables.map(timetable => (
              <tr key={timetable.id} className="bg-gray-100">
                <td className="px-4 py-2">{timetable.department.name}</td>
                <td className="px-4 py-2">{timetable.level.level_type}</td>
                <td className="px-4 py-2">{timetable.class_group.group_name}</td>
                <td className="px-4 py-2">{timetable.lecture_hall.name}</td>
                <td className="px-4 py-2">{timetable.day}</td>
                <td className="px-4 py-2">{timetable.time_start} - {timetable.time_end}</td>
                <td className="px-4 py-2">{timetable.lecturer.name}</td>
                <td className="px-4 py-2">{timetable.session_type}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default TimetableList;*/}


import { useState, useEffect } from 'react';


function TimetableList() {
  const [timetables, setTimetables] = useState([]);

  useEffect(() => {
    // Construct URL with filters
    const url = new URL('http://127.0.0.1:8000/api/timetables/', window.location.origin);
    //const params = new URLSearchParams();
    //if (departmentId) {
    //  params.append('department', departmentId);
    //}
    //if (levelId) {
     // params.append('level', levelId);
  //  }
   // url.search = params.toString();
   

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setTimetables(data);
        console.log('Timetables:', data); // Log the entire timetable object array
      });
  },[]) //[departmentId, levelId]);



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
              {timetables.filter((timetable) => timetable.session_type === sessionType).map(
                (timetable) => (
                  <tr key={timetable.id} className="border-b border-gray-200 hover:bg-gray-100">
                    <td className="px-4 py-2">{timetable.day}</td>
                    <td className="px-4 py-2">{timetable.time_start} - {timetable.time_end}</td>
                    <td className="px-4 py-2">{console.log('Class Group:', timetable.class_group)}{timetable.class_group.name}</td>
                    <td className="px-4 py-2">{timetable.lecture_hall.name}</td>
                    <td className="px-4 py-2">{timetable.lecturer.name}</td>
                  </tr>
                )
              )}
            </tbody>
          </table>
        </div>
      ))}
    </div>
  );
}

export default TimetableList;

