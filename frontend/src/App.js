import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginPage from "./pages/loginPage";
import RegisterPage from "./pages/registerPage";
import HomePage from "./pages/homePage";
import UserProfilePage from "./pages/userProfilePage";
import PasswordResetPage from "./pages/passwordResetPage";
import RegisterUserProfilePage from "./pages/RegisterUserProfilePage";
import AboutPage from "./pages/aboutPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/forgotPassword" element={<PasswordResetPage />} />
        <Route exact path="/home" element={<HomePage />} />
        <Route path="/rUserProfile" element={<RegisterUserProfilePage />} />
        <Route path="/userProfile" element={<UserProfilePage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
    </Router>
  );
}

export default App;
