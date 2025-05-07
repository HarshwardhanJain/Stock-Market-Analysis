// src/About.js
import React from 'react';
import Navbar from './NavBar';

export default function About() {
  return (
    <>
      <Navbar />
      <div className="max-w-5xl mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">📘 About This Project</h1>
        <p className="text-gray-700 mb-4">
          This project is developed as part of the Big Data Lab (CSL311) course at The NorthCap University. It focuses on
          performing scalable analysis of stock market data using the Hadoop ecosystem.
        </p>
        <ul className="list-disc pl-6 text-gray-700 mb-4">
          <li>Apache Hadoop and Hive are used to handle and analyze large datasets.</li>
          <li>StockPrices.csv (50MB, 851,265 records) and StockCompanies.csv (40KB, 509 records) were processed.</li>
          <li>HiveQL queries enable insights into trends, sector performance, and volatility.</li>
          <li>The frontend (this dashboard) was built with React and Tailwind CSS.</li>
        </ul>
        <p className="text-gray-700">
          This work was submitted on <strong>7th May 2025</strong> by Harshwardhan Jain, Raghav Sharma, and Mehul Miglani
          under the guidance of Ms. Aarti Kukreja, Assistant Professor, CSE Department.
        </p>
      </div>
    </>
  );
}
