from prefect import flow

@flow(name="ETL Productos")
def main_flow():
  pass

if __name__ == "__main__":
  main_flow()