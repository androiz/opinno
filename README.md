# OPINNO TEST


## Consideraciones

- Debido a los requisitos de imágenes y el tamaño de la aplicación, he optado por usar una
base de datos sqlite, para simplificar y que sea mas sencilla la prueba.
- Como no se especifica, he considerado que no tenemos gestión de usuarios, por lo que las
visitas recientes han quedado asociadas a la sesión.
- En cuanto a los datos proporcionados por [swapi.dev](http://swapi.dev) , he precargado 
solo una pequeña muestra para poder llevar a cabo la prueba.
- Para la gestión de imagenes he utilizado la librería externa `django-filer`.

## Run services

Para iniciar la aplicación, necesitaremos montar un virtualenv previamente sobre `python3.7`.

Una vez lo tengamos y lo tengamos activo, debemos instalar las dependecias:
```
pip install -r requirements.txt
```

Como se incluye la base de datos, no es necesario aplicar ninguna migración por lo que 
ya podemos iniciar el servicio:
```
python manage.py runserver 0.0.0.0:8080
```

El user/pass para acceder al admin es `opinno`.


## Author

Código implementado por Andrés Rojano Ruiz.
