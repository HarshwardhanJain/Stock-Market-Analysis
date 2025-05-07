import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

export default function CategoryPage() {
  const { category } = useParams();
  const [files, setFiles] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/categories/${category}/queries/`)
      .then(res => setFiles(res.data.files))
      .catch(() => setFiles([]));
  }, [category]);

  return (
    <div className="container">
      <h1>📂 {decodeURIComponent(category)}</h1>
      <p style={{ fontSize: '1rem', color: '#555' }}>
        Select a Hive query file below to preview and analyze the output.
      </p>

      <ul>
        {files.map((file, i) => (
          <li key={i} style={{
            marginBottom: '1rem',
            border: '1px solid #ddd',
            borderRadius: '6px',
            padding: '1rem',
            backgroundColor: '#fff',
            boxShadow: '0 1px 3px rgba(0,0,0,0.05)'
          }}>
            <Link to={`/category/${encodeURIComponent(category)}/${file}`}>
              📄 {file}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
