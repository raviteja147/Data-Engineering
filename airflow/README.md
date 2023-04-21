## Airflow

Apache Airflow is a platform to programmatically schedule and mointor workflows as DAGs. With Airflow, we have command line utilities as well as a user interface to visualise pipelines, monitor progress and troubleshoot issues.

Here's the general architecture:

![airflow_arch](https://user-images.githubusercontent.com/41874704/233694088-0cfd7a1c-9a28-46b8-977b-9e0737f6ee51.png)

* `Web Server` - GUI to inspect, trigger and debug behaviour of DAGS. Available at http://localhost:8080.

    The home page of the web server shows us a list of DAGs. The DAGs properties can be seen here (where the source file resides, tags, descriptions, and so on). The DAGs can also easily be paused here, which will then ignore any schedules you may have set. You can see the names of the DAGs, the schedule that they run on (in [CRON](https://crontab.guru/#5_4_8_*_*) format), the owner of the DAG, recent tasks, a timestamp of the last run of the DAG, summary of previous DAGs run, and so on.

    You can also view the DAG as a graph, after going to the DAG detail page. We can also view the code behind the DAG here as well.

* `Scheduler` - Responsible for scheduling jobs.

    This constantly monitors DAGs and taks and running any that are scheduled to run and have had their dependencies met.

* `Worker` - Executes the tasks given by scheduler.
* `MetaData Database` - Backend to Airflow. Used by scheduler and executor and webserver to store data.

    This contains all the metadata related to the execution history of each task and DAG as well as airflow configuration. I believe the default in SQLite, but can easily be configured to PostgreSQL or some other database system. The database is created when we initialise using `airflow-init`. Information in this database includes task history.

* `redis` - Forwards messages from scheduler to worker
* `flower`- Flower app for monitoring the environment. Available at http://localhost:5555.
* `airflow-inti` - Initialises service

If we're running Airflow in Docker, we use something called `CeleryExecutor`

### Workflow
* Using Airflow, we are going to load data from web API to Google Cloud Storage(GCS) and from GCS to BigQuery for both yellow and green taxi trips.

![web_2_bq_dag_graph_view](https://user-images.githubusercontent.com/41874704/233694793-11aa34e3-f345-4927-a610-eb5f3b8219d1.png)

![web_2_bq_dag_tree_view](https://user-images.githubusercontent.com/41874704/233694819-8baeb8ab-065c-4766-b747-ad5b015b8e17.png)

 #### Execution
 
  1. Build the image (only first-time, or when there's any change in the `Dockerfile`, takes ~15 mins for the first-time):
     ```shell
     docker-compose build
     ```
   
     or (for legacy versions)
   
     ```shell
     docker build .
     ```

 2. Initialize the Airflow scheduler, DB, and other config
    ```shell
    docker-compose up airflow-init
    ```

 3. Kick up the all the services from the container:
    ```shell
    docker-compose up
    ```

 4. In another terminal, run `docker-compose ps` to see which containers are up & running (there should be 7, matching with the services in your docker-compose file).

 5. Login to Airflow web UI on `localhost:8080` with default creds: `airflow/airflow`

 6. Run your DAG on the Web Console.

 7. On finishing your run or to shut down the container/s:
    ```shell
    docker-compose down
    ```

    To stop and delete containers, delete volumes with database data, and download images, run:
    ```
    docker-compose down --volumes --rmi all
    ```

    or
    ```
    docker-compose down --volumes --remove-orphans
    ```
    
