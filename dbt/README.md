### Goal: Transforming the raw data into Analytical Views developing a dbt project using BigQuery


What is dbt? 
dbt stands for data build tool. It's a transformation tool: it allows us to transform process raw data in our Data Warehouse to transformed data which can be later used by Business Intelligence tools and any other data consumers.

dbt also allows us to introduce good software engineering practices by defining a deployment workflow:
- Develop models
- Test and document models
- ploy models with version control and CI/CD.

In this project, I have done all the above three steps mentioned.

#### How are we going to use dbt?
Using the raw data present in BigQuery, we are going to us these as source tables and create stage tables adn finally loading fact and dimensional tables into BigQuery The flow of the transformation is shown in the below lineage graph.


