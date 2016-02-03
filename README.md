#Bareteca
Jesús Prieto López

[![Build Status](https://snap-ci.com/JesGor/bareteca/branch/master/build_image)](https://snap-ci.com/JesGor/bareteca/branch/master)
[![Build Status](https://travis-ci.org/JesGor/bareteca.svg?branch=master)](https://travis-ci.org/JesGor/bareteca)
[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://bareteca.herokuapp.com/)

Repositorio con la aplicación de las prácticas de la asignatura DAI de la UGR en 2015-16.

Este repositorio está creado en concreto para la práctica 7 que se trata de desplegar la aplicación en un PaaS.

Se indicarán a continuación los pasos seguidos para su despliegue en Heroku por medio de integración continua con Snap-CI y Travis.

#Descripción

Este proyecto consiste en una aplicación web creada con **python** y **Django** en la que guardamos información referente a una serie de bares y a sus tapas.

La aplicación web cuenta con un listado de bares junto a una gráfica con los bares más visitados. Dentro de cada bar tenemos información de este, como la localización por medio de un plugin que muestra el mapa y un listado de sus tapas. Cada tapa tiene un nº de votos que podemos ir aumentando al votarlas.

Esta web permite realizar el registro de usuario y la identificación de los mismos, que podrán añadir tapas a la base de datos.

#Despliegue en PaaS - heroku

Para el despligue de la aplicación he utilizado el Paas heroku que me permite trabajar con el repositorio github directamente conectándolo a él.

> Una vez completada la configuración de despliegue en heroku y comprobado que funcionaba, he automatizado el proceso de despliegue junto al proceso de integración continua con Snap CI.

Para el despliegue en heroku necesitamos crear tres archivos:

- [requirements.txt](https://github.com/JesGor/bareteca/blob/master/requirements.txt): Indica información de las dependencias (me he ayudado con el comando `pip freeze` para conocer estas). 

```
Django==1.8.5
djangorestframework==3.3.1
wheel==0.24.0
django-easy-maps==0.9.2
django-registration-redux==1.2
django-toolbelt==0.0.1
django-bootstrap-toolkit==2.15.0
gunicorn==19.3.0
dj-database-url==0.3.0
whitenoise==2.0.6
```

- [Procfile](https://github.com/JesGor/bareteca/blob/master/Procfile): Utilizado para que la plataforma ejecute la aplicación, en este caso web. Tendrá la siguiente línea:

	web: gunicorn bareteca.wsgi --log-file -

- [runtime.txt](https://github.com/JesGor/bareteca/blob/master/runtime.txt): Se utiliza para indicar la versión de python

	python-3.4.0

Aparte hay que añadir algunas dependencias al archivo requirements.txt, como puede ser gunicorn que lo utiliza la plataforma para ejecutar la app y el cinturón de herramientas de django django-toolbelt. 

Para que nos funcionen los estilos de **bootstrap** tenemos que realizar una serie de añadidos en el archivo [settings.py](https://github.com/JesGor/bareteca/blob/master/bareteca/settings.py) y [wsgi.py](https://github.com/JesGor/bareteca/blob/master/bareteca/wsgi.py).

* En el archivo **settings.py** añadir la siguiente línea:
	STATICFILES_STORAGE = whitenoise.django.GzipManifestStaticFilesStorage'

* En el archivo **wsgi.py** modificar y añadir:

	from whitenoise.django import DjangoWhiteNoise
	application = get_wsgi_application()
	application = DjangoWhiteNoise(application)



Es necesario bajarse las herramientas de heroku para desplegar la aplicación.

`$ wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh`

Una vez instalado nos logueamos con nuestra cuenta mediante el comando:

`$ heroku login`

Accedemos ahora al directorio de nuestra aplicación y creamos nuestra aplicación en heroku, la renombramos (pone un nombre aleatorio), y subimos el código fuente.

	$ heroku create
	$ heroku apps:rename bareteca

![Login, creacion y renombrado de la app para heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap11_zpss3pbabo2.png)

Se nos proporciona el add-ons de heroku para base de datos postgresql. En esta aplicacion usaremos sqlite en local, pero a la hora de desplegarlo en el PaaS usaremos postgresql. Tenemos que configurar la aplicacicón.

Si accedemos al add-on de Postgres que disponemos en la pestaña **Resources** en la aplicación de heroku se nos muestra información de la base de datos que usaremos.

![Información de la base de datos que proporciona heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap12_zpsedbvygxl.png)

Nos quedamos con el apartado de **URL**, para conectar a la base de datos desde la aplicación. En el archivo settings.py, que está en el directorio *bareteca* tenemos que añadir el código para indicar que, si está la aplicación en heroku, utilice la base de datos con la información necesaria. 

```python

import dj_database_url

DEPLOY_HEROKU = os.environ.get('PORT')
if DEPLOY_HEROKU:
    DATABASE_URL='postgres://zcwonvuwfvvxuz:M8yUboyHfxb5pG7ODgrdVh6PB0@ec2-107-20-222-114.compute-1.amazonaws.com:5432/d8o5mrbg8eealv'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
```

Podemos conectar la aplicacion desde el PaaS al repositorio donde subimos nuestro codigo que vamos desarrollando. Desde la web de heroku, en nuestro **Dashboard** accedemos a nuestra aplicación y en la pestaña **Deploy** conectamos la aplicación con github.

![Menú deploy de la aplicación en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap13_zpsnm3nz8nb.png)

Indicamos el repositorio con el que queremos conectar en el apartado **Connect to Github**.

![Repositorio para conectar con heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap14_zpsfdrixitm.png)

También he activado la opción de realizar el despliegue automático desde la rama master, y que espere a la integración continua antes de desplegarse (ya que la configuro con Snap-CI).

![Activar despliegue automático después de CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap16_zpslfn0szm2.png)

Subimos los fuentes de la aplicacicón y los archivos creados anteriormente a heroku con `$ git add`, `$ git commit` y `$ git push heroku master`.

![Haciendo push para desplegar aplicación en Heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap15_zpsyqobykit.png)

Ejecutamos el comando para que se configure y sincronice la base de datos (es necesario para varias dependencias).

`$ heroku run python manage.py migrate`

Para finalizar podemos acceder a la aplicación desplegada mediante la direccion http://bareteca.herokuapp.com o con el comando `$ heroku open`


#Integración Continua

Antes de realizar la integración continua he creado una serie de tests utilizando el sistema de test que ofrece Django, que utiliza un archivo llamado *test.py* en el que escribimos todos los tests que deseemos. Básicamente he utilizado este método porque tiene una estructura muy sencilla y es fácil de utilizar, además no es necesario instalar nada ya que viene incorporado.

##Travis

Accedemos a la página web de Travis (podemos acceder con al cuenta de github). Ya en nuestro perfil nos aparecen directamente los repositorios de Github en los que contribuimos.

Tan solo tenemos que activar nuestro repositorio.

![Repositorio activado a través de Travis](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap1_zpsojay25zi.png)

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

![Activando servicio de integración continua con Travis en github](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap2_zpsnx3hv7zt.png)

Desde la web de Travis podremos ver el proceso de integración y las operaciones pertinentes. Si todo ha ido correctamente deberíamos obtener un resultado parecido al siguiente:

![Resultado de la integración continua en Travis](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap3_zpsoipauwa5.png)

##Snap CI

Snap CI permite realizar el proceso de integración junto al proceso de despliegue de la aplicación en el PaaS que he elegido, heroku.

Nos registramos en la página web y una vez nos logueamos pedirá permiso para conectarse a nuestra cuenta de Github. Cuando se haga la conexión correctamente se nos mostrará un menú donde elegir el repositorio que queremos conectar para la integración. En caso de estar registrado hay que acceder al menú y añadir repositorio con el botón +Repository.

![Menú superior de snap ci](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap6_zpscvtfvc6b.png)

Elegimos el repositorio donde está nuestra aplicación en github.

![Selección del repositorio de github para conectarlo a Snap CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap4_zps2kf6ymac.png)

Al indicar el repositorio nos aparece el proceso para configurar los pasos y operaciones, contenidos en **Stages**, que se realizará para la integración continua y despliegue de la aplicación en heroku.

El primer **Stage** será el encargado de instalar las dependencias, lo llamaremos por ejemplo *Install* e introduciremos que realice el comando `$ pip install -r requirements.txt`. 

![Creación de stage para las dependencias](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap5_zpslhq9plsj.png)

El siguiente **Stage** será el encargado de realizar los tests con el comando `$ python manage.py test`.

![Creación de stage para los test](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap6_zps6b7icz5t.png)

Otro **Stage** importante aquí será el encargado de realizar el despliegue en heroku. Tenemos que crear un **Stage** de tipo **Deploy**, asociando este con nuestra cuenta creada en heroku y selecccionando la aplicación que creamos anteriormente en el PaaS.

![Creación de stage para el despliegue en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap7_zpsjyf6ufqt.png)

Por último, pero no menos importante, añadimos el paso para que se cree la base de datos necesaria para nuestra aplicación una vez desplegada esta (si no no funcionaría). Tenemos que añadir en este paso que se ejecute la orden `$ heroku run --app bareteca python manage.py migrate --noinput`.

![Creación de stage para la base de datos de la aplicación](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap8_zps3wzrl2p7.png)

Pulsamos el botón de **Build Now** para que se cree el proceso de integración continua.

> Si tenemos algún error con la versión de python, cambiarla en el apartado de edición de Build Pipeline donde creamos los stages.

Al terminar la configuración de la integración continua se lanzará el proceso y nos indicará el resultado de los diferentes **Stages** creados. Si todo ha salido bien obtendremos algo parecido a la siguiente imagen, con todos los **Stages** como *Passed*.

![Proceso de integración continua en Snap-CI](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap9_zpsitlb5jf2.png)

Se ha completado todas las operaciones y se ha desplegado la aplicación, podemos comprobarlo desde la web de heroku. En el apartado **Activity** de nuestra aplicación podemos ver información acerca de los despliegues.

![Información de los últimos despliegues en heroku](http://i1175.photobucket.com/albums/r628/jesusgorillo/cap10_zpsmznswdhq.png)

Ya está listo, cada vez que trabajemos con nuestro repositorio y se ejecute un `$ git push` se iniciará automáticamente el proceso de CI y despliegue.

