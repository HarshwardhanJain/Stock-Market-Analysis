// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css';

import App from './App';
import CategoryPage from './CategoryPage';
import QueryViewer from './QueryViewer';
import About from './About';

const Contact = () => (
  <div className="max-w-5xl mx-auto px-4 py-8">
    <h1 className="text-2xl font-bold text-gray-800 mb-4">📬 Contact</h1>
    <p className="text-gray-600">Contact page coming soon.</p>
  </div>
);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/category/:category" element={<CategoryPage />} />
        <Route path="/category/:category/:filename" element={<QueryViewer />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
