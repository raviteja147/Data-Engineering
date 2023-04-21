## Prefect
Prefect is a modern workflow orchestration tool for coordinating all of your data tools. Orchestrate and observe your dataflow using Prefect. We will use Prefect to 
load data from web API into Postgres and GCP's Google Cloud Storage and BigQuery. 



# Setup

## Install packages

In a conda environment, install all package dependencies with 

```bash
pip install -r requirements.txt
```
## Start the Prefect Orion server locally

Create another window and activate your conda environment. Start the Orion API server locally with 

```bash
prefect orion start
```
and then use the below address to access prefect UI
```bash
http://127.0.0.1:4200/
```


## Register the block types that come with prefect-gcp

`prefect block register -m prefect_gcp`

## Create Prefect GCP blocks

Create a *GCP Credentials* block in the UI.

Create a GCS Bucket block in UI 

## Create flow code

Write your Python functions and add `@flow` and `@task` decorators. 

Note: all code should be run from the top level of your folder to keep file paths consistent.

## Create deployments

Create and apply your deployments.

## Run a deployment or create a schedule

Run a deployment ad hoc from the CLI or UI.

Or create a schedule from the UI or when you create your deployment.

## Start an agent

Make sure your agent set up to poll the work queue you created when you made your deployment (*default* if you didn't specify a work queue).

## Later: create a Docker Image and use a DockerContainer infrastructure block

Bake your flow code into a Docker image, create a DockerContainer, and your flow code in a Docker container.
