import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export default function QueryViewer() {
  const { category, filename } = useParams();
  const [queryText, setQueryText] = useState('');
  const [table, setTable] = useState(null);
  const [csvError, setCsvError] = useState(false);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/categories/${category}/queries/${filename}/`)
      .then(res => setQueryText(res.data.content))
      .catch(() => setQueryText('Error loading query file.'));

    axios.get(`http://localhost:8000/api/categories/${category}/output/${filename}/`)
      .then(res => {
        setTable(res.data);
        setCsvError(false);
      })
      .catch(() => {
        setTable(null);
        setCsvError(true);
      });
  }, [category, filename]);

  return (
    <div className="container">
      <h1>📄 {filename}</h1>

      <section>
        <h2>📘 Hive Query Preview</h2>
        <pre>{queryText}</pre>
      </section>

      <section style={{ marginTop: '2rem' }}>
        <h2>📊 Output (CSV Result)</h2>

        {csvError && (
          <p style={{ color: 'gray', fontStyle: 'italic' }}>
            ⚠️ No CSV found. Please add <code>{filename.replace('.txt', '.csv')}</code> inside
            <code> output/</code> folder under <strong>{category}</strong>.
          </p>
        )}

        {table && (
          <div style={{ overflowX: 'auto', marginTop: '1rem' }}>
            <table border="1" cellPadding="6" style={{ borderCollapse: 'collapse', width: '100%' }}>
              <thead style={{ backgroundColor: '#eee' }}>
                <tr>
                  {table.columns.map((col, i) => (
                    <th key={i}>{col}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {table.rows.map((row, i) => (
                  <tr key={i}>
                    {table.columns.map((col, j) => (
                      <td key={j}>{row[col]}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </div>
  );
}
