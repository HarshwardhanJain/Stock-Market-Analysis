import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

export default function CategoryPage() {
  const { category } = useParams();
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios
      .get(`http://localhost:8000/api/categories/${encodeURIComponent(category)}/queries/`)
      .then((res) => {
        if (res.data && Array.isArray(res.data.files)) {
          setFiles(res.data.files);
        } else {
          setFiles([]);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error("❌ Error loading files:", err);
        setFiles([]);
        setError("Unable to load Hive query list.");
        setLoading(false);
      });
  }, [category]);

  return (
    <div className="container" style={{ padding: '2rem' }}>
      <h1>📂 {decodeURIComponent(category).replace(/_/g, ' ')}</h1>
      <p style={{ fontSize: '1rem', color: '#555' }}>
        Select a Hive query file below to preview and analyze the output.
      </p>

      {loading && <p>⏳ Loading query files...</p>}

      {error && <p style={{ color: 'red' }}>❌ {error}</p>}

      {!loading && files.length === 0 && !error && (
        <p style={{ fontStyle: 'italic', color: 'gray' }}>
          ⚠️ No Hive query `.txt` files found in this folder.
        </p>
      )}

      {!loading && files.length > 0 && (
        <ul style={{ listStyle: 'none', paddingLeft: 0 }}>
          {files.map((file, idx) => (
            <li
              key={idx}
              style={{
                marginBottom: '1rem',
                padding: '1rem',
                border: '1px solid #ddd',
                borderRadius: '5px',
                backgroundColor: '#f5f5f5',
                wordBreak: 'break-word',
              }}
            >
              <Link
                to={`/category/${encodeURIComponent(category)}/${file}`}
                style={{ textDecoration: 'none', color: '#003366', fontWeight: 'bold' }}
              >
                📄 {file.replace(/_/g, ' ')}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
