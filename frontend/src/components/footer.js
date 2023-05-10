import React from "react";
import "./footer.css";
import eu from "../images/footer/europe.png";
import prima from "../images/footer/prima-logo.jpg";

const Footer = () => {
  return (
    <footer>
      <div className="images-container">
        <img src={eu} className="Footer-eu" alt="foot" />
        <div className="text-container">
          {"Co-funded by the European Union"}
        </div>
      </div>
      <div className="images-container">
        <img src={prima} className="Footer-pr" alt="foot" />
        <div className="text-container">
          {
            "This project is part of the PRIMA programme supported by the European Union"
          }
        </div>
      </div>
    </footer>
  );
};

export default Footer;
