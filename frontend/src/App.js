import React from 'react';
import { Link } from 'react-router-dom';

const categories = [
  {
    name: '1_Volumne_Based_Queries',
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
              border: '1px solid #ddd',
              borderRadius: '8px',
              padding: '1.2rem',
              background: '#fff',
              boxShadow: '0 2px 6px rgba(0,0,0,0.05)',
              transition: '0.2s',
            }}>
              <h3 style={{ margin: '0 0 0.5rem 0' }}>{cat.name}</h3>
              <p style={{ color: '#666', fontSize: '0.95rem' }}>{cat.description}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
