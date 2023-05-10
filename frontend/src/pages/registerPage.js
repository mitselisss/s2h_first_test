import React, { useEffect, useState } from "react";
import logo from "../images/logo/logo2.png";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import { Alert } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const navigate = useNavigate();
  const [userId, setUserId] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios
        .post("http://127.0.0.1:8000/register", {
          username,
          password,
          password2,
        })
        .then((res) => {
          if (res.status === 200) {
            const userId = res.data.id;
            setUserId(userId);
            localStorage.setItem("userId", userId); // Save the user ID to local storage
            navigate("/rUserProfile", {
              state: {
                infoMessage: `Hi ${res.data.username}. Your are one step before you create your account. Now help us with some more imforamtions about your profile.`,
              },
            });
          }
        });
    } catch (error) {
      console.log(error.response.data);
      setErrorMessage(error.response.data.error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}
        <img src={logo} className="Login-logo" alt="logo" />
        <h1 className="custom-font">Hi! Welcome</h1>
        <p className="custom-font">Let's create an account</p>

        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <input
              type="text"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder="Enter your username"
              className="line-field"
            />
          </div>
          <div className="input-container">
            <input
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Enter your password"
              className="line-field"
            />
          </div>
          <div className="input-container">
            <input
              type="password"
              value={password2}
              onChange={(event) => setPassword2(event.target.value)}
              placeholder="Confirm your password"
              className="line-field"
            />
          </div>

          <div className="button-container">
            <input type="submit" value="Sign Up" className="button" />
          </div>

          <p className="custom-font">Already have an account?</p>
          <Link to="/" className="button-container">
            Sign In
          </Link>
        </form>
      </header>
    </div>
  );
}

export default LoginPage;
