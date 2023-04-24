# Data-Engineering-Bootcamp
## Problem

This project involves extracting data using Python script from the New York daily taxi trips official [website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), using `Airflow` as a data orchestration tool to load it into `Google Cloud Storage`, and then transforming the raw data into analytically ready data using `dbt` and `Apache Spark`, and ultimately loading it into `BigQuery`. `Google Dataproc` is used to run spark jobs, and `Prefect` is used as an alternative to Airflow for data orchestration.

## Project details and implementation
This project makes use of Google Cloud Platform, particularly Cloud Storage, Dataproc and BigQuery.

Cloud infrastructure is mostly managed with Terraform, except for Airflow and dbt instances.

Data ingestion is carried out by an Airflow DAG. The DAG downloads new data hourly and ingests it to a Cloud Storage bucket which behaves as the Data Lake for the project. The dataset is in JSON format; the DAG transforms it in order to get rid of any payload objects and parquetizes the data before uploading it. The DAG also creates an external table in BigQuery for querying the parquet files.

The Data Warehouse is defined with dbt. It creates a table with all the info in the parquet files. The table is partitioned by day and clustered on actor ID's.

dbt is also used for creating the transformations needed for the visualizations. A view is created in a staging phase containing only the PushEvents (a Push Event contains one or more commits), and a final table containing the commit count per user is materialized in the deployment phase.

The visualization dashboard is a simple Google Data Studio report.

## Architecture diagram

![project_overview](https://user-images.githubusercontent.com/41874704/233907980-bfe1fc26-d5d8-4402-b8f1-01abc4065fa3.png)

## Technologies
* *Google Cloud Platform (GCP)*: Cloud-based auto-scaling platform by Google
  * *Google Cloud Storage (GCS)*: Data Lake
  * *BigQuery*: Data Warehouse
* *Terraform*: Infrastructure-as-Code (IaC)
* *Docker*: Containerization
* *SQL*: Data Analysis & Exploration
* *Airflow*: Pipeline Orchestration
* *DBT*: Data Transformation
* *Spark*: Distributed Processing
