// src/App.js
import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './NavBar';

const categories = [
  {
    name: '1_Volume_Based_Queries',
    description: 'Analyze trading volumes by sector and subindustry.',
    icon: '📈',
    color: 'text-green-700',
  },
  {
    name: '2_CLOSE_Price_&_Percent_Change_Queries',
    description: 'Track stock closing prices and price shifts.',
    icon: '💹',
    color: 'text-blue-700',
  },
  {
    name: '3_GAIN_Gainers_&_Losers',
    description: 'Identify top gainers and losers by daily percentage.',
    icon: '📉',
    color: 'text-red-600',
  },
  {
    name: '4_VOLAT_Volatility_and_Range',
    description: 'Evaluate volatility and price fluctuations.',
    icon: '📊',
    color: 'text-yellow-600',
  },
  {
    name: '5_META_Company_Metadata',
    description: 'Explore metadata like sector and headquarters.',
    icon: '🧠',
    color: 'text-gray-700',
  },
];

export default function App() {
  return (
    <>
      <Navbar />
      <div className="bg-gray-100 min-h-screen py-10 px-4">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">📊 Stock Market Analysis Dashboard</h1>
          <p className="text-gray-600 mb-8 text-lg">
            Explore large-scale stock datasets using Hive queries categorized by analytics type.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {categories.map((cat, i) => (
              <Link to={`/category/${encodeURIComponent(cat.name)}`} key={i}>
                <div className="bg-white border border-gray-300 rounded-lg shadow-sm p-6 hover:shadow-lg transition">
                  <h3 className={`text-xl font-semibold mb-2 ${cat.color}`}>
                    {cat.icon} {cat.name.replace(/_/g, ' ')}
                  </h3>
                  <p className="text-gray-600">{cat.description}</p>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
