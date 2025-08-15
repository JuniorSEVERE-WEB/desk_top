
import { useState } from "react";
import './login.css'
export function LoginForm() {
  const [showPassword, setShowPassword] = useState(false);

  function togglePasswordVisibility() {
    setShowPassword(!showPassword);
  }
  return (
    <>
      <div>
        <input placeholder="Email" className="login-input" />
      </div>
      <div>
        <input
          placeholder="Password"
          type={showPassword ? "text" : "password"}
          className="login-input"
        />
      </div>

      <button className="login-button">Login</button>
      <button className="login-button">Sign up</button>
      <button className="login-button" onClick={togglePasswordVisibility}>
        {showPassword ? "Hide" : "Show"} Password
      </button>
    </>
  );
}
