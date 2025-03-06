# Pasos para ejecutar el contenedor

1. Para crear la imágen

```shell
docker build -t flask-docker .
```

2. Para levantar el contenedor

```shell
docker run -d -p 8000:8000 --name flask-docker-container flask-docker
```

# Para ejecutar el docker-compose

```shell
docker compose -p flask-docker-compose up -d
```
