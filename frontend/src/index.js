// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css';

import App from './App';
import CategoryPage from './CategoryPage';
import QueryViewer from './QueryViewer';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/category/:category" element={<CategoryPage />} />
        <Route path="/category/:category/:filename" element={<QueryViewer />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
