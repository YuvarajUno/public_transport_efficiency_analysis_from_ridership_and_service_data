# 🚍 Public Transport Efficiency Analysis from Ridership and Service Data

## 📌 Project Overview
This project implements an end-to-end **data engineering and analytical pipeline**
to evaluate the efficiency of urban public transportation systems using
**ridership logs, GTFS schedule data, and route-level information**.

The pipeline follows industry-standard data engineering practices:
- Modular data ingestion
- Data cleaning and preprocessing
- Feature engineering
- KPI-based modeling and aggregation
- Analytical evaluation and visualization
- Workflow orchestration using **Apache Airflow**

The results support **evidence-based transport planning and operational improvements**.

---

## 🎯 Research Questions Addressed

### RQ1: Which transport routes experience the highest congestion during peak hours?
- Peak-hour ridership is analyzed across routes and time intervals
- Load factor KPIs are used to identify congestion-prone routes
- Results are summarized in route-level tables and figures

---

### RQ2: How does ridership vary across time?
- Ridership patterns are compared across:
  - Peak vs off-peak hours
  - Weekdays vs weekends
- Temporal aggregation highlights demand fluctuations
- Insights support scheduling and capacity planning decisions

---

### RQ3: How efficient is each route based on operational KPIs?
- Route efficiency is evaluated using:
  - Load factor
  - On-time (punctual) performance
  - Peak utilization rates
- KPIs enable standardized comparison across routes

---

### RQ4: Can integrated ridership and GTFS data identify underutilized routes?
- Ridership data is integrated with GTFS schedules
- Low-utilization routes are detected using KPI thresholds
- Findings support route rescheduling and service optimization

---

### RQ5: What are the practical implications for urban transport planning?
- Data-driven insights enable:
  - Improved timetable design
  - Capacity optimization
  - Reduced congestion
  - Better passenger experience
  - Efficient allocation of transport resources

---
## 🗂 Project Structure
public_transport_efficiency_analysis_from_ridership_service_data/
├── dags/ # Airflow DAGs for pipeline orchestration
│ ├── figures/ # Auto-generated figures (PDF)
│ ├── tables/ # Auto-generated tables (XLSX/CSV)
│ └── project_pipeline_dag.py
├── data/ # Data storage
│ ├── sample/ # Raw input datasets
│ └── intermediate/ # Cleaned and processed data
│ ├── Ridership.csv
│ └── upcoming_city.csv
├── data_ingestion/ # Data ingestion scripts
│ └── load_data.py
├── data_cleaning/ # Data cleaning scripts
│ └── clean_data.py
├── feature_engineering/ # Feature engineering scripts
│ └── features.py
├── modeling/ # KPI modeling and aggregation
│ └── simple_model.py
├── evaluation/ # Output generation scripts
│ ├── figures/ # Generated figures (PDF)
│ ├── tables/ # Generated tables (CSV/XLSX)
│ └── generate_outputs.py
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── main.py # Main execution script


---

## ⚙️ Installation & Requirements

1. Clone the repository:  
```bash
# 🚍 Public Transport Efficiency Analysis from Ridership and Service Data

## 📌 Project Overview
This project implements an end-to-end **data engineering and analytical pipeline**
to evaluate the efficiency of urban public transportation systems using
**ridership logs, GTFS schedule data, and route-level information**.

The pipeline follows industry-standard data engineering practices:
- Modular data ingestion
- Data cleaning and preprocessing
- Feature engineering
- KPI-based modeling and aggregation
- Analytical evaluation and visualization
- Workflow orchestration using **Apache Airflow**

The results support **evidence-based transport planning and operational improvements**.

---

## 🎯 Research Questions Addressed

### RQ1: Which transport routes experience the highest congestion during peak hours?
- Peak-hour ridership is analyzed across routes and time intervals
- Load factor KPIs are used to identify congestion-prone routes
- Results are summarized in route-level tables and figures

---

### RQ2: How does ridership vary across time?
- Ridership patterns are compared across:
  - Peak vs off-peak hours
  - Weekdays vs weekends
- Temporal aggregation highlights demand fluctuations
- Insights support scheduling and capacity planning decisions

---

### RQ3: How efficient is each route based on operational KPIs?
- Route efficiency is evaluated using:
  - Load factor
  - On-time (punctual) performance
  - Peak utilization rates
- KPIs enable standardized comparison across routes

---

### RQ4: Can integrated ridership and GTFS data identify underutilized routes?
- Ridership data is integrated with GTFS schedules
- Low-utilization routes are detected using KPI thresholds
- Findings support route rescheduling and service optimization

---

### RQ5: What are the practical implications for urban transport planning?
- Data-driven insights enable:
  - Improved timetable design
  - Capacity optimization
  - Reduced congestion
  - Better passenger experience
  - Efficient allocation of transport resources

---
## 🗂 Project Structure
public_transport_efficiency_analysis_from_ridership_service_data/
├── dags/ # Airflow DAGs for pipeline orchestration
│ ├── figures/ # Auto-generated figures (PDF)
│ ├── tables/ # Auto-generated tables (XLSX/CSV)
│ └── project_pipeline_dag.py
├── data/ # Data storage
│ ├── sample/ # Raw input datasets
│ └── intermediate/ # Cleaned and processed data
│ ├── Ridership.csv
│ └── upcoming_city.csv
├── data_ingestion/ # Data ingestion scripts
│ └── load_data.py
├── data_cleaning/ # Data cleaning scripts
│ └── clean_data.py
├── feature_engineering/ # Feature engineering scripts
│ └── features.py
├── modeling/ # KPI modeling and aggregation
│ └── simple_model.py
├── evaluation/ # Output generation scripts
│ ├── figures/ # Generated figures (PDF)
│ ├── tables/ # Generated tables (CSV/XLSX)
│ └── generate_outputs.py
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── main.py # Main execution script


---

## ⚙️ Installation & Requirements

1. Clone the repository:  
```bash
git clone https://github.com/YuvarajUno/public_transport_efficiency_analysis_from_ridership_and_service_data.git





