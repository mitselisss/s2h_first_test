import React, { useState } from "react";
import logo from "../images/logo/logo2.png";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import { Alert } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.css";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();
  // const [userId, setUserId] = useState(null);
  // const [authTokens, setAuthTokens] = useState(null);
  // const [user, setUser] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      axios
        .post("http://127.0.0.1:8000/token/", {
          username,
          password,
        })
        .then((res) => {
          // console.log(res.data.success);
          // && res.data.success
          if (res.status === 200) {
            // setAuthTokens(res.data);
            // setUser(jwt_decode(res.data.access));
            // console.log(res.data);
            // console.log(jwt_decode(res.data.access));
            localStorage.setItem("authTokens", JSON.stringify(res.data));
            // const userId = res.data.id;
            // setUserId(userId);
            // localStorage.setItem("userId", userId); // Save the user ID to local storage
            navigate("/home", {
              state: {
                successMessage: `Welcome back !!! Eating healthy food fills your body with energy and nutrients !!!`,
              },
            });
          }
        });
    } catch (error) {
      setErrorMessage("No active account found with the given credentials");
    }
  };

  return (
    <div classname="App">
      <header className="App-header">
        {errorMessage && <Alert variant="danger">{errorMessage}</Alert>}
        <img src={logo} className="Login-logo" alt="logo" />

        <form onSubmit={handleSubmit}>
          <div>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder="Enter your username"
              className="line-field"
            />
          </div>

          <div>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Enter your password"
              className="line-field"
            />
          </div>

          <div className="App-forgot">
            <a href="./forgotPassword" className="custom-font">
              Forgot Password?
            </a>
          </div>

          <div className="button-container">
            <input type="submit" value="Log In" className="button" />
          </div>

          <p className="custom-font">Don't have an account?</p>
          <Link to="/register" className="button-container">
            Sign Up
          </Link>
        </form>
      </header>
    </div>
  );
}

export default LoginPage;
