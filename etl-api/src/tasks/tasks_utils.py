from prefect import task
from config import config
from mysql import connector

@task(name="Inicializar la tabla de usuario")
def task_init_table():
  with connector.connect(**config.MYSQL_CONFIG) as db:
    with db.cursor() as cursor:
      pass # procs 