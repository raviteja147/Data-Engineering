# Prefect
Prefect is a modern workflow orchestration tool for coordinating all of your data tools. Orchestrate and observe your dataflow using Prefect. We will use Prefect to 
load data from web API into Postgres and GCP's Google Cloud Storage and BigQuery. 

## Prefect architecture

![prefect_arch](https://user-images.githubusercontent.com/41874704/233724632-317c8276-1950-4f11-927a-e8a66aece100.png)


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

This is how the prefect UI looks like

![prefect_UI](https://user-images.githubusercontent.com/41874704/233724758-74406e13-104b-4614-a702-05f3c9a300f6.png)


## Register the block types that come with prefect-gcp

`prefect block register -m prefect_gcp`

## Create Prefect GCP blocks

Create a *GCP Credentials* block in the UI.

Create a GCS Bucket block in UI 

## Create flow code

Write your Python functions and add `@flow` and `@task` decorators. 

Note: all code should be run from the top level of your folder to keep file paths consistent.

## Create deployments
A deployment in prefect is a server-side concept that encapsulates a flow allowing it to be scheduled and trigerred via API.
we can have multiple deployments for the same flow.

### Deploying using CLI:
This will create a yaml file contains metadata about the flow code and schedule the flow based on cron 
```bash
prefect deployment build <filepath>:<entry point flow name> -n "<deployemnt name>" --cron "****" -a
```

This will send yaml file to prefect API and you can see the deployment in prefect UI deployment page once we run it, it will add to the workflow queues(default).
workflow queues are agents which are very light weight python process and lives in ur execution env.

```bash
prefect deployment apply <yaml file name>
```
Run the deployment
```bash
prefect deployment run <deployment name> -p "months=[1,2,3,4,5]"
```

## Alternative: create a Docker Image and use a DockerContainer infrastructure block

Bake your flow code into a Docker image, create a DockerContainer, and your flow code in a Docker container.
Run the below code line by line
```bash
docker image build -t <image name>
docker image push  <image name>
docker_deploy.py
prefect agent start -q "default"
prefect deployment run <deployment name> -p "months=[1,2,3,4,5]"
```
