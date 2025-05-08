# 📊 Stock Market Analysis using Hive and Hadoop

This project demonstrates how **Apache Hive** can be used over **Hadoop HDFS** to analyze large-scale stock market data and present the insights on a modern **React + Tailwind CSS** dashboard.

---

## 🛠 Tools & Technologies

- **Apache Hadoop (v3.3.x)** – for distributed storage via HDFS  
- **Apache Hive (v3.1.x)** – SQL-like query engine on Hadoop  
- **Django + REST Framework** – backend to serve Hive query outputs  
- **ReactJS + Tailwind CSS** – interactive frontend dashboard  
- **HiveQL** – for performing analytical queries  
- **HDFS** – for storing large CSV-based datasets  
- **Manual Hive View** – for exporting Hive query results

---

## 📁 Dataset Description

### StockPrices.csv

- **Fields:** `stock_id`, `date`, `open_price`, `close_price`, `high_price`, `low_price`, `volume`  
- **Size:** 50 MB  
- **Records:** 851,265  

### StockCompanies.csv

- **Fields:** `stock_id`, `company_name`, `sector`, `industry`  
- **Size:** 40 KB  
- **Records:** 509  

These datasets are linked via the `stock_id` field and stored in HDFS.

---

## 🔧 Setup Instructions

### 1. Upload Data to HDFS

```bash
hadoop fs -mkdir /user/hive/warehouse/stock_data
hadoop fs -put StockPrices.csv /user/hive/warehouse/stock_data/
hadoop fs -put StockCompanies.csv /user/hive/warehouse/stock_data/
```

### 2. Create Hive Tables

```sql
CREATE TABLE stock_prices (
  stock_id STRING,
  date STRING,
  open_price FLOAT,
  close_price FLOAT,
  high_price FLOAT,
  low_price FLOAT,
  volume INT
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/hive/warehouse/stock_data/StockPrices.csv'
INTO TABLE stock_prices;

CREATE TABLE stock_companies (
  stock_id STRING,
  company_name STRING,
  sector STRING,
  industry STRING
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/hive/warehouse/stock_data/StockCompanies.csv'
INTO TABLE stock_companies;
```

### 3. Run the Backend (Django)

```bash
cd backend
python manage.py runserver
```

- Make sure Hive query `.txt` files, their output `.csv` files, and optional visualization scripts/images are organized under:

```txt
project_data/
  ├── 1_Volumne_Based_Queries/
  │    ├── VOL_query_sector_daily_volume.txt
  │    ├── output/
  │    │   └── VOL_query_sector_daily_volume.csv
  │    └── visualization/
  │         ├── VOL_query_sector_daily_volume.py
  │         └── VOL_query_sector_daily_volume.png
  ├── 2_CLOSE_Price_&_Percent_Change_Queries/
  │    ├── CLOSE_query_percent_change.txt
  │    └── output/
  │         └── CLOSE_query_percent_change.csv
  └── ...
```

These folders and files are read by the Django backend to serve query details and results to the frontend.

### 4. Run the Frontend (React)

```bash
cd frontend
npm install
npm start
```

App will be available at:  
[http://localhost:3000](http://localhost:3000)

---

## 🧭 Navigation Structure

- **Home Page:** Browse by query category  
- **Category Page:** View all Hive `.txt` queries under selected category  
- **Query Viewer Page:** See raw Hive query + output CSV or TXT preview  

---

## ✨ Features

- Hive query previews with syntax highlighting  
- Render CSV and TXT output directly in browser  
- Search/filter queries  
- Mobile-friendly Tailwind UI  
- Breadcrumb navigation  
- Fully modular React components  

---

## 🚀 Future Enhancements

- Add export/download result feature  
- Enable user login and saved query states  
- Implement ML analysis using Spark MLlib  
- Add Hive partitioning for faster queries  
- Dockerize the backend + frontend  

---

## 📂 Project Folder Structure

```txt
Stock Market Analysis/
├── backend/                        # Django backend
│   ├── api/                        # API views to serve query/output/plots
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── __pycache__/            # [ignored in .gitignore]
│   ├── stocksite/                  # Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── __pycache__/            # [ignored in .gitignore]
│   ├── manage.py
│   ├── requirements.txt            # Python dependencies
│   └── project_data/               # Hive queries, outputs, and visualizations
│       ├── 1_Volumne_Based_Queries/
│       ├── 2_CLOSE_Price_&_Percent_Change_Queries/
│       ├── 3_GAIN_Gainers_&_Losers/
│       ├── 4_VOLAT_Volatility_and_Range/
│       └── 5_META_Company_Metadata/
│           ├── *.txt
│           ├── output/
│           └── visualization/
│
├── frontend/                       # React + Tailwind frontend
│   ├── public/
│   ├── src/
│   │   └── components/
│   ├── package.json
│   └── node_modules/              # [ignored in .gitignore]
│
├── datasets/                       # Raw input datasets
│   ├── StockPrices.csv
│   └── Stockcompanies.csv
│
├── documentation/                 # Docs, reports, and references
│   ├── Hadoop_and_Hive_code_explanation.docx    # [ignored in .gitignore]
│   ├── Stock_Market_Analysis_Report.docx        # [ignored in .gitignore]
│   ├── Final Project PPT.pdf
│   ├── PPT Slides/
│   │   └── 12.png
│   └── Website Screenshots/
│       └── Average-Closing-Price-by-Sector-Over-Time.png
│
├── .gitignore                     # Git ignore file (see below ⚠️)
├── README.md
```

---

## ⚠️ `.gitignore` Rules

Ensure you **do not commit large files or unnecessary build/bytecode directories**. Your `.gitignore` includes:

```txt
Hadoop_and_Hive_code_explanation.docx
Stock_Market_Analysis_Report.docx

backend/api/__pycache__
backend/stocksite/__pycache__

frontend/node_modules
```

---

## 📄 License & Acknowledgement

This project was developed as part of the **Big Data Lab (CSL311)** course at  
**The NorthCap University, Gurugram**.

**Prepared by:**

- Harshwardhan Jain – 22CSU392  
- Raghav Sharma – 22CSU229  
- Mehul Miglani – 22CSU323  

**Faculty Guide:**  
Aarti Kukreja
