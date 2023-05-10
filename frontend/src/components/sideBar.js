import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import logo from "../images/logo/logo2.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDoorOpen } from "@fortawesome/free-solid-svg-icons";
import jwt_decode from "jwt-decode";
import "./sideBar.css";

function SideBar() {
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

  const Logout = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
  };

  return (
    <div className="page-container">
      <div className="main-content">
        <div className="sidebar" style={{ width: "13%" }}>
          <div className="logo-container">
            <img src={logo} style={{ maxWidth: "100%", height: "auto" }} />
          </div>
          <div className="menu-options-container">
            <hr></hr>
            <Link to="/home" className="menu-option">
              <label className="custom-font3">Weekly Plan</label>
            </Link>
            <hr></hr>
            <Link to="/userProfile" className="menu-option">
              <label className="custom-font3">User Profile</label>
            </Link>
            {/* <div>
                  <button onClick={toggleVisibility}>User Profile</button>
                </div> */}
            <hr></hr>
            <Link to="/about" className="menu-option">
              <label className="custom-font3">About</label>
            </Link>
            <hr></hr>
            {/* <Link to="/" className="menu-option">
                  <label className="custom-font3">Other</label>
                </Link>
                <hr></hr> */}
            <Link to="/" className="menu-option">
              <div className="sign-out-button">
                <FontAwesomeIcon
                  icon={faDoorOpen}
                  size="2x"
                  onClick={Logout}
                  // onClick={() => alert("Signing out...")}
                />
              </div>
            </Link>
            <hr></hr>
          </div>
        </div>
      </div>
    </div>
  );
}
export default SideBar;
