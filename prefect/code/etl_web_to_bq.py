import pandas as pd
import pyarrow
from prefect import flow, task
from prefect_gcp import GcpCredentials


@task(retries=3)
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read taxi data from web into pandas DataFrame"""
    df = pd.read_parquet(dataset_url)
    return df


@task()
def write_bq(df: pd.DataFrame, color: str) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")

    df.to_gbq(
        destination_table= f"taxi_trips.{color}",
        project_id="taxi-rides-ny-375905",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )


@flow()
def etl_web_to_bq() -> None:
    """The main ETL function"""
    for color in ['yellow', 'green']:
        for year in [2020, 2021, 2022]:  
            for month in range(1, 13):
                dataset_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{color}_tripdata_{year}-{month:02}.parquet"
                df = fetch(dataset_url)
                write_bq(df, color)

if __name__ == "__main__":
    etl_web_to_bq()