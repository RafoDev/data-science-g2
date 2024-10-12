from prefect import flow
from tasks.tasks_utils import task_init_table, task_get_user_from_db
from tasks.task_extract import task_extract_csv, task_extract_dni
from tasks.utils import validate_dni, handle_invalid_dni
from tasks.task_load import task_load_user

BASELINE_TASKS = False
DATA_PATH = "./resources/user.csv"

@flow(name="ETL APIPERU", log_prints=True)
def main_flow():

  if BASELINE_TASKS:
    task_init_table()

  initial_user_data = task_extract_csv(DATA_PATH)
  for user in initial_user_data:
    dni = user[0]
    celular = user[1]
    
    if validate_dni(dni):
      user_exists = task_get_user_from_db(dni)
      
      if not user_exists:
        api_user_data = task_extract_dni(dni)
        user_data = (dni, *api_user_data, celular)
        task_load_user(user_data)
    else:
      handle_invalid_dni(dni)

if __name__ == "__main__":
  main_flow()