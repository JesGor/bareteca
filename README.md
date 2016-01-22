#Bareteca
Jesús Prieto López

Repositorio con la aplicación de las prácticas de la asignatura DAI de la UGR en 2015-16.

Este repositorio está creado en concreto para la práctica 7 que se trata de desplegar la aplicación en un PAAS.

Se indicarán a continuación los pasos seguidos para su despliegue en Heroku por medio de integración continua con Snap-CI y Travis.


#Integración Continua

Antes de realizar la integración continua necesitamos:

- El fichero requirements.txt, en el que se indica información de las dependencias (he utilizado el comando pip freezepara conocer estas).

- El fichero de tests

##Travis

Accedemos a la página web de Travis (podemos acceder con al cuenta de github). Ya en nuestro perfil nos aparecen directamente los repositorios de Github en los que contribuimos.

Tan solo tenemos que activar nuestro repositorio.

![Repositorio activado a través de Travis](cap1)

Definimos el archivo de configuración de la integración continua,  un archivo que se debe llamar *.travis.yml*, en el que indicamos el lenguaje, la versión, como instalar dependencias y ejecutar los tests (se pueden añadir más cosas).

```yml
language: python
python:
 - "3.4"
# command to install dependencies
install:
 - pip install -r requierements.txt
# command to run tests
script:
 - python manage.py test
```

Una vez creado lo subimos al directorio raíz de nuestro repositorio. A continuación accedemos a las propiedades del repositorio y dentro del menú Webhooks & services pulsamos sobre Travis CI y seguidamente pulsamos en el botón superior que indica Test service.

![Activando servicio de integración continua con Travis en github](cap2)

Desde la web de Travis podremos ver el proceso de integración y las operaciones pertinentes. Si todo ha ido correctamente deberíamos obtener un resultado parecido al siguiente:

![Resultado de la integración continua en Travis](cap3)