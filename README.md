# CRMPodemosAprender

boty.py
    muestra los miembros del servidor
    muestra los foros creados en el servidor

mensajes.py
    mientras esta en ejecucion escucha e imprime:
        - Titulo del posteo
        - Autor del posteo
        - Mensaje del posteo
    luego por cada mensaje que se escribe en algun posteo hace lo mismo

saludoInicial.py
    - Cuando ingresa un nuevo usuario al servidor le envia un DM de bienvenida
    - Se estableca una respuesta automatica ante un mensaje predeterminado

Carpeta db
    Utiliza SqlAlchemy para hacer una base de datos utilizando SQLite (https://tutorials.technology/tutorials/Using-python-SQLAlchemy-with-SQLlite3-tutorial.html)


TABLAS Base de datos
    Clientes(Datos contacto)
    Oportunidades (Nombre, texto, Estado, )

    Historia
        Autor
        Cliente?
        Oportunidad?
        Texto
        Fecha
        Pendiente
        Quien se ocupa


USER STORIES
    Como vendedor
    Quiero poder ver todos los pendientes para mi
    Para poder sacarme alguno de encima

    Como vendedor
    Quiero poder agregar texto y un nuevo estado a la historia 
    Para actualizar lo que avance con un pendiente

    Como programador
    Quiero poder consultar las oportunidades pendientes de presupuesto
    Para ofertar a las que me interesan
