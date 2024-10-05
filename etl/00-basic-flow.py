from prefect import task, flow

#                           FLUJO
#       T1                  T2                 T3
# [OBTENER DATOS] -> [PROCESAR DATOS] -> [MOSTRAR DATOS]

@task(name="Obtener datos")
def get_data():
  return [1,2,3]

@task(name="Procesar Datos")
def proccess_data(data):
  return data * 2

@task(name="Mostrar datos")
def show_results(data):
  print("Data procesada ", data)

@flow(name="Flujo básico", log_prints=True)
def main_flow():
  data = get_data()
  results = proccess_data(data)
  show_results(results)

if __name__ == "__main__":
  main_flow()