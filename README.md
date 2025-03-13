# Módulo 9: Proyecto Final

## Implementación y Despliegue de Modelos de ML/DP

El trabajo final consistirá en desarrollar un modelo de machine learning y/o Deep Learning para resolver un problema comercial específico, y llevarlo desde su fase de planteamiento en un notebook hasta su implementación como una API funcional que pueda ser consumida por otras aplicaciones.

## Estructura del Proyecto

### Propuesta Inicial

El estudiante deberá presentar una propuesta que incluya:

- Descripción del problema comercial seleccionado, puede ser uno de los siguientes o proponer uno nuevo:
  - Predicción de abandono de clientes (churn prediction)
  - Segmentación de clientes para estrategias de marketing
  - Optimización de precios dinámicos
  - Análisis de sentimiento de reseñas
  - Predicción de demanda y gestión de inventario
  - Detección de fraude
  - Recomendación de productos
  - Pronóstico de ventas
  - Optimización de rutas de entrega
  - Análisis de comportamiento del cliente
- Conjunto de datos a utilizar (fuente, características, etc)

## Desarrollo del Modelo

### Formulación de Modelos

- Limpieza y preprocesamiento de datos
- Análisis estadístico descriptivo
- Visualización de relaciones entre variables
- Selección de algoritmos apropiados para el problema
- Definición de variables predictoras y objetivo
- Implementación de modelos base (fine tunning opcional)

## Despliegue del Modelo

#### Serialización del Modelo

- Exportación del modelo entrenado
- Documentación de versiones y dependencias

#### Desarrollo de Paquete Python

- Creación de estructura de paquete con setup.py
- Implementación de funciones para pre-procesamiento y predicción
- Documentación del código y funcionalidades

#### Desarrollo de API

- Implementación usando Flask o FastAPI
- Endpoints para predicción
- Validación de entradas y manejo de errores
- Pruebas de funcionamiento y rendimiento

#### Dockerización

- Creación de Dockerfile
- Configuración de entorno y dependencias
- Pruebas de contenerización
- Instrucciones de despliegue

## Entregables:

Repositorio de GitHub con:

1. Notebook del modelo: Completamente documentado y con la propuesta inicial al comienzo. Debe incluir el modelo y el dataset (cuando sea aplicable).
2. Paquete del modelo: Implementación del modelo como un paquete de Python instalable.
3. API dockerizada: Implementación del modelo como un servicio web dentro de un contenedor Docker.

### Fecha de entrega: 26-03-2025
