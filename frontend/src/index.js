import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from './App';
import CategoryPage from './CategoryPage';
import QueryViewer from './QueryViewer';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/category/:category" element={<CategoryPage />} />
        <Route path="/category/:category/:filename" element={<QueryViewer />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
