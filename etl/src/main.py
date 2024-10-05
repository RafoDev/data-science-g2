from prefect import flow
from tasks.task_extract_products import task_extract_products
from tasks.task_load_products import task_load_products

@flow(name="ETL Productos")
def main_flow():
  products = task_extract_products("teclado")
  task_load_products(products)

if __name__ == "__main__":
  main_flow()