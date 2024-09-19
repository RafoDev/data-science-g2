# Git

<img src='https://i.postimg.cc/nr6CG7BZ/git-stages.jpg' alt='Banner de Git' width='600px' />

## ¿Qué es el control de versiones?

Es un sistema que ayuda a rastrear y gestionar los cambios realizados en un archivo o archivos.

Es utilizado por todo aquel quien necesite hacer un seguimiento de las modificaciones realizadas en el código fuente, el sistema de versiones permite analizar los cambios y revertirlos sin repercusiones si se comete algún error.


## ¿Qué es Git?

Es el sistema de control de versiones más utilizado del mundo.  Presenta una arquitectura distribuida, en lugar de tener un único espacio para todo el historiar de versiones, en Git, la copia de trabajo del código de cada desarrollador es también un repositorio local que puede albergar el historial de los cambios.

## Aspectos básicos de Git

### Commit

Cuando se guarda el trabajo, Git crea un commit. Un commit es una instantánea (snapshot) de todos los archivos del repositorio en un momento determinado. Si un archivo no fue modificado de un commit a otro siguiente, Git utiliza el que fue almacenado anteriormente.

Los commits crean enlaces a otros commits, formando un grafo de la historia de desarrollo. Es posible revertir el código a un commit anterior, inspeccionar como los archivos cambiaron entre commits y revisar la información como donde y cuando fueron hechos estos cambios.

### Branches (ramas)

Cada desarrollador guarda los cambios en su repositorio local. Como resultado pueden haber muchos cambios sobre un solo commit. Git provee las ramas para aislar los cambos y luego poder mezclarlos.

### Archivos y commits

En Git existen tres estados posibles: 

- Modificado
- Staged
- Commited

Cuando un archivo está modificado los cambios solo existen en el directorio mas no son parte del histórico de desarrollo. El desarrollador tiene que almacenar provisionalmente (staged) los archivos modificados que serán parte del commit. El area de Staging contiene todos los cambios que se incluirán en el siguiente commit.