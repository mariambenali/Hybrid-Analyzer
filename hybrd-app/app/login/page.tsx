"use client";

import React, { useState } from "react";

export default function Page() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [isSignup, setIsSignup] = useState(false);

  // LOGIN
  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = { username, password };

    console.log(data)

    try {

      const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      console.log(result)

      if (!response.ok) {
        alert(result.detail || "Login failed");
        return;
      }

      localStorage.setItem("token", result.token);
      window.location.href = "/dashboard";

    } catch (error) {
      alert("Erreur réseau");
    }
  };

  // SIGNUP
  const handleSignup = async (e) => {
    e.preventDefault();

    const data = { username, password, email };

    try {
      const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (!response.ok) {
        alert(result.detail || "Signup failed");
        return;
      }

      alert("Compte créé avec succès ! Vous pouvez vous connecter.");
      setIsSignup(false); // revenir au login

    } catch (error) {
      alert("Erreur réseau");
    }
  };

  return (
    <div className="bg-[url('/images/11.jpg')] bg-cover bg-center flex items-center justify-center min-h-screen">
      <form
        onSubmit={isSignup ? handleSignup : handleSubmit}
        className="bg-black/90 shadow-2xl font-poppins p-8 rounded-xl w-full max-w-sm space-y-4"
      >
        <h2 className="text-center text-xl font-bold">
          {isSignup ? "Create Account" : "Login"}
        </h2>

       
        <div>
          <h4>Username</h4>
          <input
            className="bg-black text-white px-4 py-1 w-full rounded"
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

       
        {isSignup && (
          <div>
            <h4>Email</h4>
            <input
              className="bg-black text-white px-4 py-1 w-full rounded"
              type="email"
              placeholder="Enter email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
        )}

        
        <div>
          <h4>Password</h4>
          <input
            className="bg-black text-white px-4 py-1 w-full rounded"
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {/* MAIN SUBMIT BUTTON */}
        <button
          type="submit"
          className="bg-gray-700 hover:bg-slate-500 w-full py-1 rounded text-white"
        >
          {isSignup ? "Signup" : "Login"}
        </button>

        <div className="text-center">
          <h4>________________OR________________</h4>
        </div>

        {/* SWITCH LOGIN ↔ SIGNUP */}
        <button
          type="button"
          className="bg-red-900 hover:bg-red-950 w-full py-1 rounded text-white"
          onClick={() => setIsSignup(!isSignup)}
        >
          {isSignup ? "Back to Login" : "Create new account"}
        </button>
      </form>
    </div>
  );
}
