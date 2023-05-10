import React, { useState, useEffect } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { Alert } from "react-bootstrap";
import axios from "axios";
import jwt_decode from "jwt-decode";
import SideBar from "../components/sideBar";
import Footer from "../components/footer.js";
import image from "../images/homePage/qjNLom2.jpg";
import backgroundImage from "../images/homePage/mfc.jpg";
import concept1 from "../images/graphics/SWITCHtoHEALTHY-Concept_01.png";
import concept2 from "../images/graphics/SWITCHtoHEALTHY-Concept_02.png";
import concept3 from "../images/graphics/SWITCHtoHEALTHY-Concept_03.png";
import concept4 from "../images/graphics/SWITCHtoHEALTHY-Concept_04.png";
import "bootstrap/dist/css/bootstrap.css";
import "./homePage.css";
import "../components/sideBar.css";
import "../components/calendar.css";

function HomePage() {
  const [meals, setMeals] = useState([]);
  const [selectedDay, setSelectedDay] = useState("Monday");
  // const [isVisible, setIsVisible] = useState(null);
  // const [Visibility, setVisibility] = useState(null);
  // const [selectedMealDishes, setSelectedMealDishes] = useState([]);
  const [selectedDish, setSelectedDish] = useState(null);
  const location = useLocation();
  const navigate = useNavigate();
  const [week, setWeek] = useState(1);
  const [successMessage, setSuccessMessage] = useState("");
  const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  const [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwt_decode(localStorage.getItem("authTokens"))
      : null
  );

  useEffect(() => {
    if (user == null) {
      navigate("/");
    } else {
      if (location.state && location.state.successMessage) {
        setSuccessMessage(location.state.successMessage);
        setTimeout(() => {
          setSuccessMessage("");
        }, 10000); // Hide the success message after 10 seconds
      }
      if (user) {
        axios
          .get(`http://127.0.0.1:8000/${user.user_id}/NPs`)
          .then((response) => {
            setMeals(response.data);
          })
          .catch((error) => console.log(error));
      }
    }
  }, []);

  const handleNextWeek = () => {
    setWeek(week + 1);
  };

  const handlePreviousWeek = () => {
    setWeek(week - 1);
  };

  const days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];

  const dayMap = {
    Monday: [0, 1],
    Tuesday: [1, 2],
    Wednesday: [2, 3],
    Thursday: [3, 4],
    Friday: [4, 5],
    Saturday: [5, 6],
    Sunday: [6, 7],
  };

  const handleDishClick = (dish) => {
    setSelectedDish(dish);
  };

  const selectedMeals = meals.slice(...dayMap[selectedDay]);
  //console.log(selectedMeals);

  return (
    <div className="parent-container">
      <div className="page-container">
        {/* <SideBar /> */}
        <SideBar />
        <Footer />

        <div style={{ width: "87%", float: "right" }}>
          {/* <WeeklyCalendar /> */}
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            {successMessage && (
              <Alert variant="success">{successMessage}</Alert>
            )}
          </div>

          <div className="calendar">
            {/* <div className="controls">
              <button onClick={handlePreviousWeek} disabled={week === 1}>
                <label className="custom-font">Previous Week</label>
              </button>
              <h1 className="custom-font">Week {week}</h1>
              <button onClick={handleNextWeek}>
                {" "}
                <label className="custom-font">Next Week</label>
              </button>
            </div> */}
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
          {/* <div>
            {isVisible && (
              <div className="popup">
                <UserProfilePage />
              </div>
            )}
          </div> */}
          {/* <div
            style={{
              backgroundImage: `url(${backgroundImage})`,
              backgroundSize: "cover", // This will resize the image to cover the entire element
              backgroundRepeat: "no-repeat", // This will prevent the image from repeating
              backgroundPosition: "center", // This will position the image at the center of the element
            }}
          > */}
          <div></div>
          <div className="meal-grid">
            <div className="meal-grid-left">
              {selectedMeals.map((mealSet, index) => (
                <p key={index}>
                  {mealSet.map((meal) => (
                    <p key={meal.id}>
                      <p className="meal-type-font">{meal.type}</p>
                      {meal.dish_1 && (
                        <p
                          onClick={() => handleDishClick(meal.dish_1)}
                          className="custom-font"
                        >
                          {meal.dish_1.name_en}

                          <span style={{ float: "right" }}>
                            kcal:{meal.dish_1.kcal} | protein:
                            {meal.dish_1.protein} | fat:{meal.dish_1.fat} |
                            carbs:{meal.dish_1.carbohydrates}
                          </span>
                        </p>
                      )}
                      {meal.dish_2 && (
                        <p
                          onClick={() => handleDishClick(meal.dish_2)}
                          className="custom-font"
                        >
                          {meal.dish_2.name_en}

                          <span style={{ float: "right" }}>
                            kcal:{meal.dish_2.kcal} | protein:
                            {meal.dish_2.protein} | fat:{meal.dish_2.fat} |
                            carbs:{meal.dish_2.carbohydrates}
                          </span>
                        </p>
                      )}
                      {meal.dish_3 && (
                        <p
                          onClick={() => handleDishClick(meal.dish_3)}
                          className="custom-font"
                        >
                          {meal.dish_3.name_en}

                          <span style={{ float: "right" }}>
                            kcal:{meal.dish_3.kcal} | protein:
                            {meal.dish_3.protein} | fat:{meal.dish_3.fat} |
                            carbs:{meal.dish_3.carbohydrates}
                          </span>
                        </p>
                      )}
                      {meal.dish_4 && (
                        <p
                          onClick={() => handleDishClick(meal.dish_4)}
                          className="custom-font"
                        >
                          {meal.dish_4.name_en}

                          <span style={{ float: "right" }}>
                            kcal:{meal.dish_4.kcal} | protein:
                            {meal.dish_4.protein} | fat:{meal.dish_4.fat} |
                            carbs:{meal.dish_4.carbohydrates}
                          </span>
                        </p>
                      )}
                      {meal.dish_5 && (
                        <p
                          onClick={() => handleDishClick(meal.dish_5)}
                          className="custom-font"
                        >
                          {meal.dish_5.name_en}

                          <span style={{ float: "right" }}>
                            kcal:{meal.dish_5.kcal} | protein:
                            {meal.dish_5.protein} | fat:{meal.dish_5.fat} |
                            carbs:{meal.dish_5.carbohydrates}
                          </span>
                        </p>
                      )}
                    </p>
                  ))}
                </p>
              ))}
            </div>
            <div className="meal-grid-right">
              {selectedDish && (
                <>
                  <p className="dish-name-font">{selectedDish.name_en}</p>
                  <br></br>
                  <div>
                    <p className="custom-font2">Ingredients for an adult: </p>
                    <p className="custom-font">
                      {selectedDish.ingredients_adult_en}
                    </p>
                  </div>
                  <br></br>
                  <div>
                    <p className="custom-font2">Ingredients for an child: </p>
                    <p className="custom-font">
                      {selectedDish.ingredients_child_en}
                    </p>
                  </div>
                  <br></br>
                  <div>
                    <p className="custom-font2">Recipe:</p>
                    <p className="custom-font">{selectedDish.recipe_en}</p>
                  </div>
                  <br></br>
                  <div>
                    <p className="custom-font2">Tip:</p>
                    <p className="custom-font">{selectedDish.tip_en}</p>
                  </div>
                </>
              )}
            </div>
          </div>
          {/* </div> */}
          <br></br>
          <div className="camvas">
            <img src={image} style={{ maxWidth: "100%", height: "auto" }} />
          </div>
          <br></br>
          <br></br>
          <div className="concept-grid">
            <div>
              <img
                src={concept1}
                style={{ maxWidth: "100%", height: "auto" }}
              ></img>
            </div>
            <div>
              <img
                src={concept2}
                style={{ maxWidth: "100%", height: "auto" }}
              ></img>
            </div>
            <div>
              <img
                src={concept3}
                style={{ maxWidth: "100%", height: "auto" }}
              ></img>
            </div>
            <div>
              <img
                src={concept4}
                style={{ maxWidth: "100%", height: "auto" }}
              ></img>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
