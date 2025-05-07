import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

export default function QueryViewer() {
  const { category, filename } = useParams();
  const [queryText, setQueryText] = useState('');
  const [outputType, setOutputType] = useState(null); // 'csv' or 'txt'
  const [outputData, setOutputData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Load Hive Query
    axios
      .get(`http://localhost:8000/api/categories/${category}/queries/${filename}/`)
      .then((res) => {
        setQueryText(res.data.content || 'No query found.');
      })
      .catch(() => {
        setQueryText('❌ Failed to load Hive query.');
      });

    // Load Output (CSV or TXT fallback)
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
        setLoading(false); // still show query even if output fails
      });
  }, [category, filename]);

  return (
    <div className="container" style={{ padding: '2rem' }}>
      <Link to={`/category/${category}`} style={{ display: 'inline-block', marginBottom: '1rem' }}>
        ⬅ Back to {decodeURIComponent(category).replace(/_/g, ' ')}
      </Link>

      <h1 style={{ wordBreak: 'break-word' }}>
        📄 {filename.replace(/_/g, ' ')}
      </h1>

      <section>
        <h2>📘 Hive Query Script</h2>
        <pre style={{ background: '#f8f8f8', padding: '1rem', borderRadius: '5px', overflowX: 'auto' }}>
          {queryText}
        </pre>
      </section>

      <section style={{ marginTop: '2rem' }}>
        <h2>📊 Output</h2>

        {loading && <p>Loading output...</p>}

        {!loading && outputType === 'csv' && (
          <div style={{ overflowX: 'auto', marginTop: '1rem' }}>
            <table border="1" cellPadding="6" style={{ borderCollapse: 'collapse', width: '100%' }}>
              <thead style={{ backgroundColor: '#eee' }}>
                <tr>
                  {outputData.columns.map((col, idx) => (
                    <th key={idx}>{col}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {outputData.rows.map((row, idx) => (
                  <tr key={idx}>
                    {outputData.columns.map((col, j) => (
                      <td key={j}>{row[col]}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {!loading && outputType === 'txt' && (
          <pre style={{ background: '#f4f4f4', padding: '1rem', borderRadius: '5px' }}>
            {outputData}
          </pre>
        )}

        {!loading && !outputType && (
          <p style={{ fontStyle: 'italic', color: 'gray' }}>
            ⚠️ No output file available for this query yet.
          </p>
        )}
      </section>
    </div>
  );
}
