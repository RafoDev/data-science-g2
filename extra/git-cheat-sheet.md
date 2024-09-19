# Git Cheat Sheet

## Configuración

Para configurar el nombre y el email que estarán ligados a tus commits.

```bash
git config --global user.name 'tu nombre'
git config --global user.email 'email@gmail.com'
```

Para listar la configuración.

```bash
git config --list
```

## Repositorio local

Crear un repositorio de git en el directorio actual.
```bash
git init
```

Para clonar un repositorio remoto.

```bash
git clone <url>
```

Para listar el estado de los archivos.

```bash
git status
```

Agregar los archivos nuevos o que hayan sufrido cambios.

```bash
# Para archivos desde la carpeta actual
git add .

# Para TODOS los archivos
git add --all

# Para un archivo
git add <archivo>
```

Crear el commit con los archivos agregados.

```bash
git commit -m '<mensaje>'
```

Para modificar el último commit.

```bash
git commit --amend -m '<mensaje>'
```

Deshacer los cambios en el working directory.

```bash
git restore '<archivo>'
```

Regresar un archivo del stagging al working directory.
```bash
git reset '<archivo>'
```

## Mostrar los commits

```bash
git log
git log --oneline
git log --oneline --graph --all
```

## Ramas

Crear una nueva rama.

```bash
git branch <rama>
```

Mostrar las ramas.
```bash
git branch
```

Para moverse a otra rama.

```bash
git checkout <rama>
```

Para renombrar la rama actual.

```bash
git branch -m <rama>
```

Para borrar una rama.

```bash
git branch -d <rama>
```

Para mezclar dos ramas. Los cambios de la rama especificada se aplican a la actual.

```bash
git merge <rama>
```

## Repositorio remoto

Para vincular un repositorio remoto a nuestro repositorio local.

```bash
git remote add origin <url>
```

Cambiar la url del respositorio remoto.

```bash
git remote set-url origin <url>
```
Para mostrar el repositorio remoto vinculado.

```bash
git remote -v
```

Subir los commits al repositorio remoto. Con `-u` especificamos que `<rama>` es la rama principal.

```bash
git push -u origin <rama>
```

Subir los commits al repositorio remoto dede la rama principal.

```bash
git push
```

Descargar los commits del repositorio remoto y actualizar la rama.

```bash
git pull
git pull origin <rama>
```
