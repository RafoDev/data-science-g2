# Ejercicio con Requests y MySQL

Se propondrán endpoins, elija uno de ellos y utilice la data que devuelve el endpoint para llenar una tabla de MySQL.

## Endpoints Propuestos

1. [PokéApi](#pokeapi)
2. [jsonplaceholder](#jsonplaceholder)
3. [RestCountries](#restcountries)

---

### [PokéApi](https://pokeapi.co/docs/v2#pokemon)

Para obtener un pokemon mediante su `id`:

```python
id = 1
url = f"https://pokeapi.co/api/v2/pokemon/{id}"
```
Para obtener un pokemon mediante su `nombre`:

```python
nombre = "bulbasaur"
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
```

Obtendrá TODOS los datos del pokemon en formato JSON.

```json
{
    "abilities": [
        {
            "ability": {
                "name": "overgrow",
                "url": "https://pokeapi.co/api/v2/ability/65/"
            },
            "is_hidden": false,
            "slot": 1
        },
        {
            "ability": {
                "name": "chlorophyll",
                "url": "https://pokeapi.co/api/v2/ability/34/"
            },
    .
    .
    .
```

> **Nota:** Basta con unos pocos campos (name, height, weight, base_experience)

Para obtener una `cantidad` de pokemones:

```python
cantidad = 3
url = f"https://pokeapi.co/api/v2/pokemon?limit={cantidad}"
```
Obtendrá:
```json
{
    "count": 1302,
    "next": "https://pokeapi.co/api/v2/pokemon?offset=3&limit=3",
    "previous": null,
    "results": [
        {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
        },
        {
            "name": "ivysaur",
            "url": "https://pokeapi.co/api/v2/pokemon/2/"
        },
        {
            "name": "venusaur",
            "url": "https://pokeapi.co/api/v2/pokemon/3/"
        }
    ]
}
```
> **Nota:** Al utilizar este endpoint, obtendrá un arreglo de `urls` de pokemones, será necesario recorrer la lista `results` y hacer un request por cada `url` para obtener los datos.

---

### [jsonplaceholder](https://jsonplaceholder.typicode.com/)


Para obtener todos los usuarios (10).
```python
url = f"https://jsonplaceholder.typicode.com/users"
```

Para obtener un usuario mediante su `id`:

```python
id = 1
url = f"https://jsonplaceholder.typicode.com/users/{id}"
```

La respuesta será:
```json
{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}
```
---

### [RestCountries](https://restcountries.com/#rest-countries)

Para obtener información sobre todos los países:

```python
url = f"https://restcountries.com/v3.1/all"
```

Para obtener resultados filtrados por campos:

```python
url = f"https://restcountries.com/v3.1/all?fields=name,flags,capital,languajes"
```

La lista oficial de campos se puede revisar en el siguiente [link](https://gitlab.com/restcountries/restcountries/-/blob/master/FIELDS.md).