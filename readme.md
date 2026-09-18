# Manual de instalacion de la instalacion web 

## Decisiones de proyecto

|elemento|version|decision|justificacion|
|--------|--------|---------|-----------|
|servidor web|apache|2|sencillo de usar, popular|
|base de datos|MySQL|8|Eperiencia previa, popular|
|lenguaje servidor|Phython|3|uso extendido, muy interesante para asir|
|Framework|Flask|3|sencillo de usar, pensado especificamente para web (formularios, sesiones)|
|control de versiones|git|2|Muy extendido|
|documentacion|markdown|-|Muy utilizado con github|

## Proceso de instalacion

1. Actualizar sistema 
`sudo apt update
`sudo apt upgrade`
2. instalar git
`sudo apt install git`
3. instaalr VSCode + plugins:
    - Markdown all in one
4. Instalar apache 2
`sudo apt install apache 2`
5. cambair permisos capeta /var/www/html
``` bash
sudo chown -R $USER $USER:$USER /var/www/html
sudo chown -R u=rwX,go=rX /var/www/html
```
6. Instalar mysql server
``` bash 
sudo apt install mysql-server
```

1. Configuracion Mysql
``` mysql
create database incidencias;
sudo apt install mysql-server
create user 'incidencias'@'localhost' identified by 'incidencias';
grant all privileges on incidencias.* to 'incidencias'@'localhost';
flush privileges;
-- Crear Tabla
-- Insertar datos
```

## Configuracion de Git/giuthub

1. Crear repositorio local, añadir archivos y commit
``` bash
git init
git add .
git commit -m "comentario"
```
2. Crear cuenat github, crear repositerio en github
3. Conectar repositorio local con remoto
``` bash 
git remote add origin https://github.com/gabrielramiloal-ctrl/incidencias.ies.teis.git
git branch -M main
git push -u origin main
