# Ejercicio | Análisis de Textos

## ¿Qué es análisis de textos?

El análisis de texto, también conocido como minería de datos, se refiere al proceso de extraer información significativa de datos textuales.

## Objetivos

Convertir el texto a minúsculas y luego buscar la frecuencia de cada palabra, asi como de una palabra en específico.

## Conocimientos necesarios

1. Listas
2. Strings 
3. Clases y objetos
4. Conjuntos y Diccionarios

## Tareas

Consideremos un escenario de la vida real en el que se analizan los comentarios de los clientes sobre un producto. Tiene un gran conjunto de datos de opiniones de clientes en forma de cadenas y desea extraer información útil de ellas mediante las tres tareas identificadas:

- **Tarea 1: String en minúsculas**: desea preprocesar los comentarios de los clientes convirtiendo todo el texto a minúsculas. Este paso ayuda a estandarizar el texto. Poner el texto en minúsculas le permite centrarse en el contenido en lugar de en las letras específicas.
- **Tarea 2: Frecuencia de todas las palabras en una cadena determinada:**: Frecuencia de todas las palabras en una cadena determinada: después de convertir el texto a minúsculas, desea determinar la frecuencia de cada palabra en los comentarios de los clientes. Esta información te ayudará a identificar qué palabras se utilizan con más frecuencia, indicando los aspectos o temas clave que los clientes mencionan en sus reseñas. Al analizar la frecuencia de las palabras, puede obtener información sobre los problemas más comunes planteados por los clientes. 
- **Tarea 3: Frecuencia de una palabra específica**:  Frecuencia de una palabra específica: además de analizar las frecuencias generales de las palabras, desea realizar un seguimiento específico de la frecuencia de una palabra en particular que sea relevante para su análisis. Por ejemplo, podría interesarle monitorear la frecuencia con la que aparece la palabra "confiable" en las reseñas de los clientes para medir la opinión de los clientes sobre la confiabilidad del producto. Al centrarse en la frecuencia de una palabra específica, puede obtener una comprensión más profunda de las opiniones o preferencias de los clientes relacionadas con ese aspecto en particular. 

## Extra | Manejo de Archivos

El analizador recibe un nombre archivo y procesa el contenido del mismo. Adicionalmente, tiene un método que permite escribir la frecuencia de palabras en otro archivo.  