// src/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-6 py-3 shadow-md mb-6">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold hover:text-blue-400 transition">
          📊 Stock Dashboard
        </Link>
        <div className="space-x-4 text-sm">
          <Link to="/" className="hover:text-blue-400 transition">Home</Link>
        </div>
      </div>
    </nav>
  );
}
