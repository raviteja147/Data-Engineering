# Data-Engineering-Bootcamp
## Problem

This project involves taking data from the New York daily taxi trips official [website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), using Airflow as a data orchestration tool to load it into Google Cloud Storage, transforming the raw data into analytically ready data using dbt and Apache Spark, and ultimately loading it into BigQuery. Google Dataproc is used to run spark jobs, and Prefect is used as an alternative to Airflow for data orchestration.
