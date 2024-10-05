from prefect import flow
from tasks.tasks_utils import task_init_table

BASELINE_TASKS = True

@flow(name="ETL APIPERU")
def main_flow():

  if BASELINE_TASKS:
    task_init_table()
  
if __name__ == "__main__":
  main_flow()