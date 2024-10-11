# ETL

El reto consiste en proponer e implementar un ETL utilizando Prefect.

El alumno será el responsable de elegir el método de extracción de datos, así como la fuente de los mismos.

En caso se decida utilizar una API como fuente de datos, se recomienda utilizar [APIs públicas](https://github.com/public-apis/public-apis).  

Es necesario que el alumno detalle cual es la propuesta en el archivo `README.md` del repositorio.

Por ejemplo, una posible propuesta (en Markdown) podría ser:

```markdown
# ETL de RUCs utilizando ApiPeruDev

Implementación de un ETL para RUCs de empresas. Los datos de: el número de ruc y sus ventas anuales se extraen de un archivo `datos_empresas.csv`. Luego estos datos son complementados con la informacion de razon social y domicilio fiscal de la empresa. Estos nuevos datos son obtenidos a través de ApiPeruDev.
Finalmente los datos se guardan en una bd.
```

> **Recomendación:** Utilizar de base el proyecto ETL - ApiPeruDev que desarrollamos en clase.

## Objetivos
 
* Uso de Prefect para orquestar flujos y tareas.
* Extracción de datos ya sea utilizando Web Scraping o alguna API.
* Carga de datos a una bd.
