# Importar el decorador flow de prefect
from prefect import flow

# Importamos las tareas
# from paquete.modulo import funcion
from tasks.task_extract_products import task_extract_products
from tasks.task_load_products import task_load_products_baseline, task_load_products_update

TYPE_TASK = "update"

# Definimos nuesto flujo de trabajo
@flow(name="ETL Productos")
def main_flow():
  search = ["hyperx"]
  for query in search:
    products = task_extract_products(query)
    if TYPE_TASK == "baseline":
      task_load_products_baseline(products)
    elif TYPE_TASK == "update":
      task_load_products_update(products)

# Solo ejecutamos el main_flow si el archivo se llama como archivo principal
if __name__ == "__main__":
  main_flow()