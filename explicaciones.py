Lo que se ejecuta,
 El main- en este caso es la Api.py ,Dockerfile y requirementes.txt tienen que estar en la misma carpeta.

 RUN pip install -r requirements.txt
 Instalará las librerias que tenga dentro.


 Haciendo en la consola pipfreze me saca listado de todas las librerias para saber lo que 
 tengo instalado y con eso creamos un archivo .txt requirements donde voy a poner las librerias
 que va a necesita ,mi programa.

 COPY . /app:   Es la carpeta de docker donde voy a trabjar

 WORKDIR /app : Es el directorio de la carpeta de trabajo.