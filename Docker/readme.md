Carlos Uriel Salcido Aviña.  
217560751.  

El primer paso es la instalación de Docker Desktop, no tiene ningún chiste. Ahora, utilizaremos la terminal para ejecutar algunos comandos. Comenzamos con el comando 'images' para ver las imagenes que tenemos. Como usé Airflow para la actividad anterior, esta ya aparece instalada. Ahora instalo la imagen de node, y tras su instalación, si repetimos en comando 'images', ahora también aparece node, en su última versión, ya que no especificamos ese aspecto.
![Alt text](image.png)


Podemos instalar distintas versiones de una misma imagen con el comando indicado.
![Alt text](image-1.png)


Ahora me moví a la terminal de Warp. Con este comando se pueden elminar imagenes.
![Alt text](image-2.png)


Creamos un contenedor mongo con este comando, se nos devuelve un ID importante. Con este ID, podemos iniciar el contenedor, y verificarlo con el comando 'docker ps', que nos muestra una tabla con los contenedores. Aqui se pueden ver los de Airflow que usé antes.
![Alt text](image-3.png)


Con 'docker stop', seguido del ID, podemos detener contenedores. Aqui dejé solo mongo.
![Alt text](image-4.png)


Para eliminar un docker, se usa 'docker rm ', junto con el nombre o ID del contenedor.
![Alt text](image-5.png)


Es posible especificar el puerto que queremos asignar a un contenedor. Es mejor hacerlo, pues si no, Docker tomará la decisión, y suele tomar malas decisiones.
![Alt text](image-6.png)


El comando 'docker run' encuentra una imagen que necesitemos, y si no la tenemos, la descarga, luego crea un contenedor, y luego lo inicia.
![Alt text](image-7.png)


Ahora podemos crear una aplicación usando JavaScript. Primero creamos un container de nombre 'sofia', donde incluimos sus puertos, nombres, USERNAME y PASSWORD de la base de datos y establecemos que usaremos mongo.
![Alt text](image-8.png)


Utilizamos este codigo de Java Script, el cual, al acceder al puerto 3000 del localhost, muestra todos los animales creados. Para crear animales, hay que añadir '/crear/', nos mostrará el mensaje 'ok'
![Alt text](image-9.png)


No muestra nada porque no hemos creado animales.
![Alt text](image-10.png)


creamos uno.
![Alt text](image-11.png)


Y volvemos al inicio, yo hice dos. Podemos ver ambos chanchitos con su ID y estado 'Feliz'
![Alt text](image-12.png)


Mientras tanto, la terminal muestra esto:
![Alt text](image-13.png)