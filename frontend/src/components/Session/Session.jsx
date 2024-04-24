/* eslint-disable react/prop-types */
import  { useState, useEffect } from 'react';
import axios from 'axios';

const Session = () => {
  const [regularTimetables, setRegularTimetables] = useState([]);
  const [eveningTimetables, setEveningTimetables] = useState([]);
  const [weekendTimetables, setWeekendTimetables] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/timetables/')
      .then(response => {
        // Separate timetables based on session types
        const regular = [];
        const evening = [];
        const weekend = [];

        response.data.forEach(timetable => {
          switch (timetable.session_type) {
            case 'Regular':
              regular.push(timetable);
              break;
            case 'Evening':
              evening.push(timetable);
              break;
            case 'Weekend':
              weekend.push(timetable);
              break;
            default:
              break;
          }
        });

        // Set state for each session type
        setRegularTimetables(regular);
        setEveningTimetables(evening);
        setWeekendTimetables(weekend);
      })
      .catch(error => {
        console.error('Error fetching timetables:', error);
      });
  }, []);

  return (
    <>
      <div className="session lg:w-10/12 lg:mx-auto divide-y divide-blue-200">
        {/* Regular Session */}
        <div className="bg-blue-200 w-60 p-1">
          <h1 className="uppercase font-bold lg:text-2xl md:text-xl">Regular</h1>
        </div>
        {regularTimetables.map((timetable, index) => (
          <Timetable key={index} timetable={timetable} />
        ))}

        {/* Evening Session */}
        <div className="bg-blue-200 w-60 p-1 mt-10">
          <h1 className="uppercase font-bold lg:text-2xl md:text-xl">Evening</h1>
        </div>
        {eveningTimetables.map((timetable, index) => (
          <Timetable key={index} timetable={timetable} />
        ))}

        {/* Weekend Session */}
        <div className="bg-blue-200 w-60 p-1 mt-10">
          <h1 className="uppercase font-bold lg:text-2xl md:text-xl">Weekend</h1>
        </div>
        {weekendTimetables.map((timetable, index) => (
          <Timetable key={index} timetable={timetable} />
        ))}
      </div>
    </>
  );
};

const Timetable = ({ timetable }) => {
  return (
    <div className="bg-slate-50 flex items-center lg:gap-16 md:gap-5">
      <div className="w-1/5 rounded-md">
        <p className="uppercase text-blue-900 py-5 px-2 md:text-lg lg:text-xl">{timetable.day}</p>
      </div>
      <div className="w-2/5 py-4 px-1 bg-slate-50">
        <p className="uppercase lg:text-xl">
          {timetable.course.name} <br />{" "}
          <span className="font-bold">{timetable.course.course_code}</span>
          <br />
          <span className="font-bold -mt-4 text-blue-400">{timetable.lecture_hall.name}</span>
        </p>
      </div>
      <div className="w-1/5 py-9 px-2 bg-slate-50">
        <p className="uppercase lg:text-xl">{timetable.lecturer.name}</p>
      </div>
      <div className="w-1/5 py-9 px-2 bg-slate-50">
        <p className="uppercase lg:text-xl">
          {timetable.time_start} <br /> {timetable.time_end}
        </p>
      </div>
    </div>
  );
};

export default Session;
