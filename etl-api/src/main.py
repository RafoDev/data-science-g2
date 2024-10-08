from prefect import flow
from tasks.tasks_utils import task_init_table
from tasks.task_extract import task_extract_csv

BASELINE_TASKS = False
DATA_PATH = "./resources/user.csv"

@flow(name="ETL APIPERU", log_prints=True)
def main_flow():

  if BASELINE_TASKS:
    task_init_table()

  initial_user_data = task_extract_csv(DATA_PATH)
  print(initial_user_data)
  
if __name__ == "__main__":
  main_flow()