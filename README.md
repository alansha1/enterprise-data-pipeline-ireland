# Enterprise Data Pipeline: Irish Market Intelligence Platform

An end-to-end cloud data engineering project designed to extract, transform, load (ETL), and visualize live datasets from the Central Statistics Office (CSO) Ireland API. This project demonstrates enterprise-level architecture utilizing automated data orchestration and cloud data warehousing.

## 🚀 Architecture Overview
*   **Data Source:** Central Statistics Office (CSO) Ireland / Smart Dublin API
*   **Ingestion & Extraction:** Python (`requests`, `pandas`) 
*   **Cloud Storage (Data Lake):** Amazon S3 (Raw Storage Layer)
*   **Data Warehouse:** Snowflake / Google BigQuery (Staging & Production Layers)
*   **Transformation:** SQL & dbt (Data Build Tool) for modular modeling
*   **Orchestration:** Apache Airflow / AWS Lambda (Scheduled Daily Runs)
*   **Data Visualization:** Power BI (Automated Executing Dashboards)

## 📁 Repository Structure
*   `/scripts/extract.py` - Local and cloud Python API data extraction
*   `/dbt/` - SQL transformation models and schema documentation
*   `/airflow/` - DAG configurations for pipeline automation
*   `/data/` - Git-ignored directory for local debugging raw files

## 🛠️ Current Project Phase
- [x] Repository initialized & architecture blueprint mapped.
- [ ] Phase 1: Local Python extraction script from Irish API endpoints.
- [ ] Phase 2: Cloud storage landing zone integration (AWS S3 / IAM).
- [ ] Phase 3: Snowflake warehouse setup and SQL staging models.
- [ ] Phase 4: Production scheduling via Apache Airflow.
