import React, { useState, useEffect } from "react";
import logo from "../images/logo/logo2.png";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";
import { Alert } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "./RegisterUserProfilePage.css";

function RegisterUserProfilePage() {
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState("");
  const [gender, setGender] = useState("");
  const [yearOfBirth, setYearOfBirth] = useState("");
  const [PAL, setPAL] = useState("");
  const [halal, setHalal] = useState(false);
  const [diary, setDiary] = useState(false);
  const [eggs, setEggs] = useState(false);
  const [fish, setFish] = useState(false);
  const location = useLocation();
  const [infoMessage, setInfoMessage] = useState("");

  const navigate = useNavigate();
  const [userId, setUserId] = useState(null);

  useEffect(() => {
    const userId = localStorage.getItem("userId");
    if (userId) {
      setUserId(userId);
    }
    if (location.state && location.state.infoMessage) {
      setInfoMessage(location.state.infoMessage);
    }
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios
        .put("http://127.0.0.1:8000/IdUserProfile/" + userId + "/", {
          height: height,
          weight: weight,
          gender: gender,
          yob: yearOfBirth,
          pal: PAL,
          halal: halal,
          diary: diary,
          eggs: eggs,
          fish: fish,
        })
        .then((res) => {
          // console.log(res.data.success);
          // && res.data.success
          if (res.status === 200) {
            navigate("/home", {
              state: {
                successMessage: `Everything was set up correctly. Nice to have you with us. We hope you enjoy our meal proposals.`,
              },
            });
          }
        });
    } catch (error) {
      console.error("Error saving username and password.", error);
    }
  };

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {infoMessage && <Alert variant="warning">{infoMessage}</Alert>}
      </div>
      <div className="ruser-profile-container">
        <form onSubmit={handleSubmit}>
          <div className="ruser-profile-grid">
            <div>
              <div className="ruser-profile-font">Physical Characteristics</div>
              <br></br>
              <div>
                <label className="ruser-font">Gender:</label>
                <div>
                  <input
                    type="radio"
                    name="gender"
                    value="male"
                    checked={gender === "male"}
                    onChange={(event) => setGender(event.target.value)}
                    className="ruser-font"
                  />
                  Male
                </div>
                <div>
                  <input
                    type="radio"
                    name="gender"
                    value="female"
                    checked={gender === "female"}
                    onChange={(event) => setGender(event.target.value)}
                    className="ruser-font"
                  />
                  Female
                </div>
              </div>
              <br></br>
              <div>
                <label className="ruser-font">Year of Birth</label>
                <input
                  type="number"
                  name="yearOfBirth"
                  value={yearOfBirth}
                  onChange={(event) => setYearOfBirth(event.target.value)}
                  className="line-field"
                />
              </div>
              <div>
                <label className="ruser-font">Height (cm)</label>
                <input
                  type="number"
                  name="height"
                  value={height}
                  onChange={(event) => setHeight(event.target.value)}
                  className="line-field"
                />
              </div>
              <div>
                <label className="ruser-font">Weight (kg)</label>
                <input
                  type="number"
                  name="weight"
                  value={weight}
                  onChange={(event) => setWeight(event.target.value)}
                  className="line-field"
                />
              </div>

              <br></br>
              <div>
                <label className="ruser-profile-font">
                  Physical Activity Level (PAL):
                </label>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Sedentary"
                    checked={PAL === "Sedentary"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="ruser-font"
                  />
                  Sedentary
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Low active"
                    checked={PAL === "Low active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="ruser-font"
                  />
                  Low Active
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Active"
                    checked={PAL === "Active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="ruser-font"
                  />
                  Active
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Very active"
                    checked={PAL === "Very active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="ruser-font"
                  />
                  Very Active
                </div>
              </div>
            </div>
            <div>
              <div>
                <div>
                  <label className="ruser-profile-font">Allergies</label>
                </div>
                <br></br>
                <div className="allergies-section">
                  <div className="checkbox-options">
                    <div>
                      <label>
                        <input
                          type="checkbox"
                          checked={diary}
                          onChange={(event) => setDiary(!diary)}
                        />
                        Diary
                      </label>
                    </div>
                    <div>
                      <label>
                        <input
                          type="checkbox"
                          checked={eggs}
                          onChange={(event) => setEggs(!eggs)}
                        />
                        Eggs
                      </label>
                    </div>
                    <div>
                      <label>
                        <input
                          type="checkbox"
                          checked={fish}
                          onChange={(event) => setFish(!fish)}
                        />
                        Fish
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <br></br>
              <div>
                <label className="ruser-profile-font">Dietary Choices</label>
              </div>
              <br></br>
              <div className="allergies-section">
                <div className="checkbox-options">
                  <label>
                    <input
                      type="checkbox"
                      checked={halal}
                      onChange={(event) => setHalal(!halal)}
                    />
                    Halal
                  </label>
                </div>
              </div>
            </div>
          </div>
          <br></br>
          <br></br>
          <div>
            <button style={{ float: "right" }} type="submit">
              Register
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
export default RegisterUserProfilePage;

{
  /* <div className="UserProfile-container">
      <form onSubmit={handleSubmit}>
        <div className="UserProfile-form-container">
          <div className="UserProfile-personal-info-container">
            <div className="UserProfile-form-group">
              <label className="custom-font">Personal Info</label>
              <label className="custom-font">Username</label>
            </div>
            <div className="UserProfile-form-group">
              <label className="custom-font">Password</label>
              <input
                type="password"
                name="password"
                value={password}
                onChange={handlePasswordChange}
                className="line-field"
              />
            </div>
          </div>
          <div className="grid-container">
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Height (cm)</label>
                <input
                  type="number"
                  name="height"
                  value={height}
                  onChange={(event) => setHeight(event.target.value)}
                  className="line-field"
                />
              </div>
            </div>
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Weight (kg)</label>
                <input
                  type="number"
                  name="weight"
                  value={weight}
                  onChange={(event) => setWeight(event.target.value)}
                  className="line-field"
                />
              </div>
            </div>
          </div>
          <div className="grid-container">
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Gender:</label>
                <div>
                  <input
                    type="radio"
                    name="gender"
                    value="male"
                    checked={gender === "male"}
                    onChange={(event) => setGender(event.target.value)}
                    className="custom-font"
                  />
                  Male
                </div>
                <div>
                  <input
                    type="radio"
                    name="gender"
                    value="female"
                    checked={gender === "female"}
                    onChange={(event) => setGender(event.target.value)}
                    className="custom-font"
                  />
                  Female
                </div>
              </div>
            </div>
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Year of Birth</label>
                <input
                  type="number"
                  name="yearOfBirth"
                  value={yearOfBirth}
                  onChange={(event) => setYearOfBirth(event.target.value)}
                  className="line-field"
                />
              </div>
            </div>
          </div>
          <div className="grid-container">
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">
                  Physical Activity Level (PAL):
                </label>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Sedentary"
                    checked={PAL === "Sedentary"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="custom-font"
                  />
                  Sedentary
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Low active"
                    checked={PAL === "Low active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="custom-font"
                  />
                  Low Active
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Active"
                    checked={PAL === "Active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="custom-font"
                  />
                  Active
                </div>
                <div>
                  <input
                    type="radio"
                    name="PAL"
                    value="Very active"
                    checked={PAL === "Very active"}
                    onChange={(event) => setPAL(event.target.value)}
                    className="custom-font"
                  />
                  Very Active
                </div>
              </div>
            </div>
            <div></div>
          </div>
          <div className="grid-container">
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Allergies</label>

                <div className="allergies-section">
                  <div className="checkbox-options">
                    <label>
                      <input
                        type="checkbox"
                        checked={diary}
                        onChange={(event) => setDiary(!diary)}
                      />
                      Diary
                    </label>
                    <label>
                      <input
                        type="checkbox"
                        checked={eggs}
                        onChange={(event) => setEggs(!eggs)}
                      />
                      Eggs
                    </label>
                    <label>
                      <input
                        type="checkbox"
                        checked={fish}
                        onChange={(event) => setFish(!fish)}
                      />
                      Fish
                    </label>
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div className="UserProfile-form-group">
                <label className="custom-font">Dietary Choices</label>
              </div>
              <div className="allergies-section">
                <div className="checkbox-options">
                  <label>
                    <input
                      type="checkbox"
                      checked={halal}
                      onChange={(event) => setHalal(!halal)}
                    />
                    Halal
                  </label>
                </div>
              </div>
            </div>
          </div>
          <div className="UserProfile-form-group">
            <button type="submit">Update</button>
          </div>
        </div>
      </form>
    </div>
  );
} */
}
