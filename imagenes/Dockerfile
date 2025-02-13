#imagen base
FROM ubuntu

#instalar python
RUN apt update
RUN apt install python3 python3-dev -y

COPY index.html .

#levantar un servidor web en el puerto 5000
CMD python3 -m http.server 5000

EXPOSE 5000