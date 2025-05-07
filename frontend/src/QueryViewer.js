// src/QueryViewer.js
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import Navbar from './NavBar';

export default function QueryViewer() {
  const { category, filename } = useParams();
  const [queryText, setQueryText] = useState('');
  const [outputType, setOutputType] = useState(null);
  const [outputData, setOutputData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/api/categories/${category}/queries/${filename}/`)
      .then((res) => {
        setQueryText(res.data?.content || 'No query found.');
      })
      .catch(() => {
        setQueryText('❌ Failed to load Hive query.');
      });

    axios
      .get(`http://localhost:8000/api/categories/${category}/output/${filename}/`)
      .then((res) => {
        if (res.data.columns && res.data.rows) {
          setOutputType('csv');
          setOutputData(res.data);
        } else if (res.data.txt) {
          setOutputType('txt');
          setOutputData(res.data.txt);
        } else {
          setOutputType(null);
        }
        setLoading(false);
      })
      .catch(() => {
        setOutputType(null);
        setOutputData(null);
        setLoading(false);
      });
  }, [category, filename]);

  return (
    <>
      <Navbar />
      <div className="max-w-6xl mx-auto px-4 py-8">
        <nav className="text-sm text-gray-600 mb-6 space-x-1">
          <Link to="/" className="hover:underline text-blue-600">🏠 Home</Link>
          <span>/</span>
          <Link to={`/category/${category}`} className="hover:underline text-blue-600">
            {decodeURIComponent(category).replace(/_/g, ' ')}
          </Link>
          <span>/</span>
          <span className="text-black font-medium">{filename.replace(/_/g, ' ')}</span>
        </nav>

        <h1 className="text-2xl font-bold text-gray-800 mb-4 break-words">
          📄 {filename.replace(/_/g, ' ')}
        </h1>

        <section className="mb-8">
          <h2 className="text-lg font-semibold mb-2">📘 Hive Query Script</h2>
          <pre className="bg-gray-100 text-sm text-gray-800 rounded-md p-4 overflow-x-auto whitespace-pre-wrap">
            {queryText}
          </pre>
        </section>

        <section>
          <h2 className="text-lg font-semibold mb-2">📊 Output</h2>
          {loading && <p className="text-blue-500">⏳ Loading output...</p>}

          {!loading && outputType === 'csv' && (
            <div className="overflow-x-auto mt-2">
              <table className="min-w-full text-sm border border-gray-300 rounded-md shadow-sm">
                <thead className="bg-blue-100 text-gray-700">
                  <tr>
                    {outputData.columns.map((col, idx) => (
                      <th key={idx} className="px-4 py-2 text-left border border-gray-300">{col}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {outputData.rows.map((row, idx) => (
                    <tr key={idx} className="hover:bg-gray-50">
                      {outputData.columns.map((col, j) => (
                        <td key={j} className="px-4 py-2 border border-gray-300">{row[col]}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {!loading && outputType === 'txt' && (
            <pre className="bg-gray-100 rounded-md p-4 mt-2 text-sm text-gray-800 whitespace-pre-wrap">
              {outputData}
            </pre>
          )}

          {!loading && !outputType && (
            <p className="text-gray-500 italic mt-2">⚠️ No output file available for this query yet.</p>
          )}
        </section>
      </div>
    </>
  );
}
