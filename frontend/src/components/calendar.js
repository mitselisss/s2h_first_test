import React, { useState } from "react";
import "./calendar.css";

const days = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday",
];

function WeeklyCalendar() {
  const [week, setWeek] = useState(1);

  const handleNextWeek = () => {
    setWeek(week + 1);
  };

  const handlePreviousWeek = () => {
    setWeek(week - 1);
  };

  const [selectedDay, setSelectedDay] = useState(null);

  return (
    <div className="calendar">
      <div className="controls">
        <button onClick={handlePreviousWeek} disabled={week === 1}>
          <label className="custom-font">Previous Week</label>
        </button>
        <h1 className="custom-font">Week {week}</h1>
        <button onClick={handleNextWeek}>
          {" "}
          <label className="custom-font">Next Week</label>
        </button>
      </div>
      <div className="days">
        {days.map((day) => (
          <div
            className={`day ${selectedDay === day ? "selected" : ""}`}
            key={day}
            onClick={() => setSelectedDay(day)}
          >
            <h1 className="custom-font">{day}</h1>
          </div>
        ))}
      </div>
    </div>
  );
}

export default WeeklyCalendar;
