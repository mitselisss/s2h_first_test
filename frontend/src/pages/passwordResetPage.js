import React from "react";
import logo from "../images/logo/logo2.png";
import { useState } from "react";
import { Link } from "react-router-dom";

function PasswordResetPage() {
  const [email, setEmail] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleInputChange = (event) => {
    setEmail(event.target.value);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (!email) {
      setErrorMessage("Please enter your email");
    } else {
      // send password reset link
      setErrorMessage("");
    }
  };

  return (
    <div classname="App">
      <header className="App-header">
        <form>
          <img src={logo} className="Forgot-logo" alt="logo" />
          <div className="password-reset-page">
            <h1 className="custom-font">Oh no, I forgot!</h1>
            <p className="custom-font">
              Enter your email and we'll send you a link to set a new password
            </p>
            {errorMessage && <p className="error-message">{errorMessage}</p>}
            <form onSubmit={handleFormSubmit}>
              <input
                type="email"
                name="uname"
                required
                value={email}
                onChange={handleInputChange}
                placeholder="Enter your Email"
                className="line-field"
              />
              <Link to="/" className="button-container">
                <div className="button-container">
                  <input type="submit" value="Reset Password" class="button" />
                </div>
              </Link>

              <h2 className="custom-font">Don't have an account?</h2>
            </form>
          </div>
        </form>
        <Link to="/register" className="button-container">
          Sign Up
        </Link>
      </header>
    </div>
  );
}

export default PasswordResetPage;
