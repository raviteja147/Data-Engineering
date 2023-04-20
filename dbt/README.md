### Goal: Transforming the raw data into more Analytical ready data by using dbt and BigQuery


What is dbt? 
- dbt stands for data build tool. It's a transformation tool: it allows us to transform process raw data in our Data Warehouse to transformed data which can be later used by Business Intelligence tools and any other data consume>>>>>>> main

dbt also allows us to introduce good software engineering practices by defining a deployment workflow:
- Develop models
- Test and document models
- ploy models with version control and CI/CD.

In this project, I have done all the above three steps mentioned.

#### How are we going to use dbt?
- Using the raw data present in BigQuery, we are going to us these as source tables and create stage tables adn finally loading fact and dimensional tables into BigQuery The flow of the transformation is shown in the below lineage graph.

![dbt_lineag_graph](https://user-images.githubusercontent.com/41874704/233490276-3aa316fd-c298-4ce6-90af-1515e82a872b.png)
