// src/CategoryPage.js
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import Navbar from './NavBar';

export default function CategoryPage() {
  const { category } = useParams();
  const [files, setFiles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios
      .get(`http://localhost:8000/api/categories/${encodeURIComponent(category)}/queries/`)
      .then((res) => {
        setFiles(Array.isArray(res.data.files) ? res.data.files : []);
        setLoading(false);
      })
      .catch((err) => {
        console.error("❌ Error loading files:", err);
        setError("Unable to load Hive query list.");
        setLoading(false);
      });
  }, [category]);

  const filteredFiles = files.filter((f) =>
    f.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Navbar />
      <div className="max-w-6xl mx-auto px-4 py-8">
        <nav className="text-sm text-gray-600 mb-6 space-x-1">
          <Link to="/" className="hover:underline text-blue-600">🏠 Home</Link>
          <span>/</span>
          <span className="text-black">{decodeURIComponent(category).replace(/_/g, ' ')}</span>
        </nav>

        <h1 className="text-2xl font-bold mb-2 text-gray-800">
          📂 {decodeURIComponent(category).replace(/_/g, ' ')}
        </h1>
        <p className="text-gray-600 mb-6">
          Select a Hive query file below to preview and analyze the output.
        </p>

        {loading && <p className="text-blue-500">⏳ Loading query files...</p>}
        {error && <p className="text-red-500 font-medium">{error}</p>}

        {!loading && files.length > 0 && (
          <div className="mb-6">
            <input
              type="text"
              placeholder="🔍 Search query files..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full sm:w-96 px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
          </div>
        )}

        {!loading && files.length === 0 && !error && (
          <p className="italic text-gray-500">⚠️ No Hive query `.txt` files found in this folder.</p>
        )}

        {!loading && filteredFiles.length > 0 && (
          <ul className="space-y-3">
            {filteredFiles.map((file, idx) => (
              <li key={idx}>
                <Link
                  to={`/category/${encodeURIComponent(category)}/${file}`}
                  className="block p-4 bg-white border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition"
                >
                  <span className="font-semibold text-blue-700">
                    📄 {file.replace(/_/g, ' ')}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        )}

        {!loading && files.length > 0 && filteredFiles.length === 0 && (
          <p className="italic text-gray-500">🔍 No queries match your search.</p>
        )}
      </div>
    </>
  );
}
