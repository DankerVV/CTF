Carlos Uriel Salcido Aviña.  
217560751.  

Esta tarea es un tanto complicada, debido a la naturaleza de Airflow. Comenzamos por crear un directorio para usar el Airflow. Aquí utilizo la terminal de Wrap
![Alt text](image.png)


Con esto podemos ver un archivo .yml que nos muestra información relacionada
![Alt text](image-2.png)


Ahora se ejecuta el siguiente comando para crear un usuario Airflow con password a irflow
![Alt text](image-1.png)


Ahora introducimos el siguiente comando, no puse toda lo que muestra porque es bastante. Se corren todos los servicios especificados en el archivo 'compose' local
![Alt text](image-3.png)


Si escribimos 'docker ps' podremos ver todos los servicios corriendo
![Alt text](image-4.png)


Si nos dirigimos al localhost:8080, veremos esta pagina.  
![Alt text](image-5.png)


Como mencioné, el usuario y contraseña son 'airflow'. Nos logeamos y llegamos a esta pagina.  
![Alt text](image-6.png)


Para interactuar con los containers, podemos tomar su ID y así, por ejemplo, saber su versión, usando 'docker exec'.
![Alt text](image-7.png)


