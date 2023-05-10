import React from "react";
import "./aboutPage.css";
import SideBar from "../components/sideBar.js";
import Footer from "../components/footer.js";
import image from "../images/graphics/STH - LOGO.png";

function AboutPage() {
  return (
    <div style={{ width: "87%", float: "right" }}>
      <div className="parent-container">
        <div className="page-container">
          <SideBar />
          <Footer />
          <div className="about-page">
            {/* <h1 className="custom-font">Welcome to SWITCHtoHEALTHY </h1> */}
            <img src={image} style={{ maxWidth: "100%", height: "auto" }} />
            <br></br>
            <br></br>
            <br></br>
            <p className="about-font">
              With a duration of 36 months, SWITCHtoHEALTHY project aims to
              generate a dietary behaviour change by demonstrating and
              reinforcing the role of the family in promoting a sustainable
              change towards enhancing the adherence to the Mediterranean
              dietary pattern of the family members (adults, adolescents, and
              children).
            </p>
            <p className="about-font">
              This will be done by making available to families a combination of
              hands-on educational material and digital tools and complementing
              the dietary and lifestyle recommendations with easy-to-eat
              healthier snacking products.
            </p>
            <p className="about-font">
              In this approach, whereas digital interactive tools
              (SWITCHtoHEALTHY App) will be used by the parents to support them
              in preparing weekly healthier dietary plans for the main meals for
              them and their children, the educational material will be used to
              support families in acquiring healthier habits and to educate
              children and adolescents.
            </p>
            <p className="about-font">
              Finally, healthy, and nutritious plant-based snacks will be
              introduced in the children dietary plans to complement it and to
              substitute less healthier options in-between meals.
            </p>
            <p className="about-font">
              SWITCHtoHEALTHY will result in increasing the adherence to
              Mediterranean Diet (MD) by taking an intra-familiar systemic
              approach taking the family context into account and assess mutual
              influence of children/adolescents-parents and their roles in
              healthy eating and lifestyle; developing innovative solutions
              (plant -based snacks) based on proximity of ingredients,
              sustainability andand healthy consumption to support agri-food
              producers (especially SMEs) in finding new business opportunities;
              job creation opportunities and diversification in traditional
              Mediterranean food sector; supporting food companies in getting
              through the barriers to market uptake and achieving a sustainable
              competitive advantage by designing innovative consumer-oriented
              BMs; raising awareness of the healthy benefits derived from a high
              adherence to a MD, increasing knowledge on local Med products thus
              contributing to improve healthy food choices among families;
              synergising cross-sectorial policy coherence across agriculture,
              health, education, environment, trade, etc. from local to national
              and international level and discussing with all actors of society.
            </p>
            <p className="about-font">
              SWITCHtoHEALTHY involves 18 prestigious organizations – public and
              private – from 8 countries of both shores of Mediterranean Sea
              (Italy, Egypt, Spain, Greece, Lebanon, Morocco, Tunisia and
              Turkey). More information can be found in the project website:
              <a href="http://switchtohealthy.eu/">
                http://switchtohealthy.eu/
              </a>
              .
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AboutPage;
