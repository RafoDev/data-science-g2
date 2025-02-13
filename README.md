# Comandos de Docker

- Para instalar una imágen

```bash
docker pull nginx
```

- Para crear un contenedor

```bash
docker run -d -p 80:80 --name mi-nginx nginx
```

- Para parar un contenedor

```bash
docker stop mi-nginx
```

- Para acceder al contenedor

```bash
docker exec -it mi-nginx //bin//sh
```

- Para borrar un contenedor

```bash
docker rm mi-nginx
```

- Para crear un volumen

```bash
docker run -d --rm -p 80:80 -v C:/Users/ASUS/tecsup-codigo/data-science-g2/html:/usr/share/nginx/html --name nginx-codigo nginx:alpine
```

- Para crear una imagen personalizada

```bash
docker build -t python-web .
```

- Para levantar un docker-compose

```bash
docker compose up -d
```
