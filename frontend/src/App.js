import React from 'react';
import { Link } from 'react-router-dom';

const categories = [
  {
    name: '1_Volume_Based_Queries',
    description: 'Analyze trading volumes by sector and subindustry.',
  },
  {
    name: '2_CLOSE_Price_&_Percent_Change_Queries',
    description: 'Track stock closing prices and price shifts.',
  },
  {
    name: '3_GAIN_Gainers_&_Losers',
    description: 'Identify top gainers and losers by daily percentage.',
  },
  {
    name: '4_VOLAT_Volatility_and_Range',
    description: 'Evaluate volatility and price fluctuations.',
  },
  {
    name: '5_META_Company_Metadata',
    description: 'Explore metadata like sector and headquarters.',
  },
];

export default function App() {
  return (
    <div className="container">
      <h1>📊 Stock Market Analysis Dashboard</h1>
      <p style={{ fontSize: '1.1rem', color: '#555' }}>
        Explore large-scale stock datasets using Hive queries categorized by analytics type.
        Select a category to begin.
      </p>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '1.5rem',
        marginTop: '2rem'
      }}>
        {categories.map((cat, i) => (
          <Link to={`/category/${encodeURIComponent(cat.name)}`} key={i}>
            <div style={{
              border: '1px solid #d0d7de',
              borderRadius: '8px',
              padding: '1.2rem',
              background: '#ffffff',
              boxShadow: '0 2px 6px rgba(0,0,0,0.04)',
              transition: '0.2s',
              wordBreak: 'break-word',
            }}>
              <h3 style={{
                margin: '0 0 0.5rem 0',
                fontSize: '1.1rem',
                wordBreak: 'break-word',
                color: '#2e7d32'
              }}>
                {cat.name.replace(/_/g, ' ')}
              </h3>
              <p style={{ color: '#555', fontSize: '0.95rem' }}>{cat.description}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
