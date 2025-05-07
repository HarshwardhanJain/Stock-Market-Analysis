// src/NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <header className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <Link to="/" className="text-xl font-bold text-green-700 hover:text-green-800 transition">
          📈 Stock Analyzer
        </Link>
        <nav className="space-x-6 text-sm font-medium">
          <Link to="/" className="text-gray-700 hover:text-green-700 transition">Home</Link>
          <Link to="/about" className="text-gray-700 hover:text-blue-700 transition">About</Link>
          <Link to="/contact" className="text-gray-700 hover:text-red-600 transition">Contact</Link>
        </nav>
      </div>
    </header>
  );
}
