import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

export default function CategoryPage() {
  const { category } = useParams();
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/api/categories/${category}/queries/`)
      .then(res => {
        setFiles(res.data.files);
        setLoading(false);
      })
      .catch(() => {
        setFiles([]);
        setLoading(false);
      });
  }, [category]);

  return (
    <div className="container">
      <h1>📂 {decodeURIComponent(category).replace(/_/g, ' ')}</h1>
      <p style={{ fontSize: '1rem', color: '#555', marginBottom: '2rem' }}>
        Select a Hive query file below to preview and analyze the output.
      </p>

      {loading && <p>Loading queries...</p>}

      {!loading && files.length === 0 && (
        <p style={{ fontStyle: 'italic', color: 'gray' }}>No Hive queries found in this category.</p>
      )}

      {!loading && files.length > 0 && (
        <ul>
          {files.map((file, i) => (
            <li
              key={i}
              style={{
                marginBottom: '1rem',
                border: '1px solid #d0d7de',
                borderRadius: '6px',
                padding: '1rem',
                backgroundColor: '#fff',
                boxShadow: '0 1px 3px rgba(0,0,0,0.05)',
                wordBreak: 'break-word',
              }}
            >
              <Link to={`/category/${encodeURIComponent(category)}/${file}`}>
                📄 {file.replace(/_/g, ' ')}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
