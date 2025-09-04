# Api-rest-video-renta
Desarrollo backend para una tienda de video. construida cn lenguaje python y el framework fastAPI, el objetivo es gestionar un catalogo de discos(peliculas o videos digitales) junto con las operaciones de registro de usuario, venta y alquiler.

##Estructura del proyecto
|--Main.py  # punto de entrada de la aplicación de la API, FastAPI
|
  entidades/ #Directorio de paquetes que contiene todas las clases
    |-__init__.py
    |-disco.py
    |-usuario.py
    |-venta.py
    |-alquiler.py
    |-catalogo.py
##Intalación y ejecución
  1. Clonar el repositorio
     git clone https://github.com/usuario/test-alquiler-video.git

  2. cd test-alquiler-video
  3. Crear y activar entorno virtual (opcional, recomendado)
  4. python -m venv
  5. source venv/bin/activate #Linux/Mac
  6. venv\Scrits\activate     #windows
  7. instalar dependencias
      7.1 pip install fastapi uvivorn pydantic
  8. Ejecutar el servidor
      8.1. uvicorn main:app --reload
  9. Acceder a la API
      *Documentación interactiva http//127.0.0.1:8000/docs
      *Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

  ## Endpoints principales (version inicial)
  Metodo endpoints Descripción
  GET     /discos/       Lista de los discos disponibles
  POST    /discos/       Agregar un nuevo disco
  PUT     /discos/{id}   Actualizar información de un disco
  DELETE  /discos/{id}   Eliminar un disco
  POST    /usuarios/     Registro de un nuevo usuario
  POST    /ventas/       Registrar ventas
  POST    /alquileres/   Registrar un alquiler

  ##Tecnologias utilizadas 
  *python 3.12.8
  *FastAPI
  *Uvicorn (servidor ASGI)

  ##Proyecto desarrolladp como casa de estudio
    * Nombre: **Deyling Espinoza.**<76592960z@gmail.com>
    *Github: @Alee-log
