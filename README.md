### Requisitos del Software

## Requisitos del Proyecto de Software

```
Este proyecto tiene como objetivo desarrollar un sistema de libro mayor centralizado utilizando tecnología blockchain, donde los usuarios pueden registrarse de manera segura, enviar órdenes de compra de acciones y verificar la integridad de las transacciones. El sistema se implementará utilizando sockets en Python para la comunicación entre clientes y el servidor. La interfaz de interacción será basada en la Línea de Comandos (CLI).

Durante el desarrollo del proyecto, se empleará y documentará la metodología TDD. El informe final del proyecto debe incluir evidencias del segimiento de la metodología y documentos de diseño. El reporte se enviará en formato PDF. La fecha de entrega será acordada en clase, de manera tal que los distintos grupos puedan exponer su solución. Durante la presentación, se hará la demostración del producto de software obtenido y se explicará cómo se repartió el trabajo entre los miembros del equipo.

```

### Requisitos del Producto de Software

## Requisitos Funcionales

# Lado Servidor

```
    Generación de Claves Pública y Privada
        [x] El servidor debe generar un par de claves pública-privada para la comunicación segura. Para ello se espera que Usted emplee servicios de PKI disponible en el lenguaje de su elección.
        [x] El servidor debe proporcionar su clave pública a los clientes que la soliciten.

    Registro de Usuario
        [x] El servidor debe aceptar solicitudes de registro por parte de los clientes, cuyo contenido será cifrado con la clave pública del servidor.
        [x] El servidor debe desencriptar las solicitudes de registro, almacenar la clave pública del cliente y asignar un ID de usuario único.

    Manejo de Transacciones
        [x] El servidor debe recibir órdenes de compra o venta de acciones por parte de los clientes.
        [x] El servidor debe validar y agregar las transacciones al libro mayor basado en blockchain.
        [x] Las transacciones se basarán en el número de ID del cliente, el tipo de operación (compra/venta) y el nombre de la acción.

    Gestión del Libro Mayor
        [x] El servidor debe mantener y gestionar el libro mayor basado en blockchain.
        [x] El servidor debe proporcionar una copia de las transacciones realizadas para un usuario en particular, a solicitud.
        [x] El servidor debe verificar y confirmar la integridad de todo el libro mayor a solicitud del cliente.

    Conexion
        [] El servidor debe de generar una conexion utilizando sockets
        [] El servidor debe de permitir conectar a los clientes mediante la exposicion del socket
```

## Cliente

```
    Manejo de Claves
        [] El cliente debe solicitar y almacenar la clave pública del servidor.
        [] El cliente debe generar su propio par de claves pública-privada para la comunicación segura.

    Registro
        [] El cliente debe enviar una solicitud de registro al servidor cifrada con la clave pública del servidor, incluyendo la clave pública del cliente.
        [] El cliente debe recibir y almacenar el ID de usuario asignado por el servidor.

    Envío de Transacciones
        [] La solicitud de registro de transacciones requiere que el cliente se haya registrado.
        [] El cliente debe enviar órdenes de compra de acciones cifradas con la clave pública del servidor, a partir de información en formato JSON.
        [] Las transacciones se basarán en el número de ID del cliente, el tipo de operación (compra/venta) y el nombre de la acción.
        [] El cliente debe asegurar que las transacciones se transmitan de manera segura.

    Verificación del Libro Mayor
        [] El cliente puede solicitar y recibir una copia de sus propias transacciones.
        [] El cliente puede solicitar una verificación de la integridad de todo el libro mayor.
```

## Requisitos No Funcionales

```
    Seguridad
        [] El sistema debe usar algoritmos criptográficos fuertes para la generación y el cifrado de claves.
        [] Todas las comunicaciones entre clientes y el servidor deben estar cifradas.

    Rendimiento
        [] El servidor debe manejar peticiones de múltiples de clientes.

    Persistencia
        [] El servidor puede emplear un sistema de archivos o un SMBD para el almacenamiento del libro.

    Usabilidad
        [] El cliente debe tener una interfaz CLI, que soporte la adecuada operación.
        [] Los nombres de comandos sugeridos para el cliente son: getKey register add copy verify
        [] El cliente y el servidor deben proporcionar mensajes de error claros y retroalimentación a la operación.
```

## Restricciones Tecnológicas

```
    Seguridad
        El sistema debe usar algoritmos criptográficos fuertes para la generación y el cifrado de claves.
        Todas las comunicaciones entre clientes y el servidor deben estar cifradas.

    Lenguaje de Programación
        Se usará Python como lenguaje de programación, bajo el paradigma POO.
        La comunicación entre cliente y servidor estará basada en sockets.
        Está permitido el uso de librerias en Python que generen valor al proyecto.
```

## Restricciones de Calidad del Servicio

```
    Confiabilidad
        El servidor debe asegurar la integridad del libro mayor basado en blockchain.
        El servidor debe velar por la confidencialidad en las operaciones realizdas por los clientes.
```

## Contenido del Blockchain

```
El blockchain almacenará cada bloque con una estructura similar a la ilustrada a continuación en formato JSON:

{
"index": 0,
"timestamp": "2023-02-15 17:36:11.050751",
"data": "Genesis Block",
"hash": "a72b31187098cfc2940a1f16cfc8edecfca1121c7b37d157d640042aeecc45c4",
"previous_hash": "0"
}

{
"index": 1,
"timestamp": "2023-02-15 17:36:11.051068",
"data": {
"user_id": "nID",
"operation_type": "buy",
"stock_name": "AAPL"
},
"hash": "6c9b6de9c01d87630a24b0c007119f92e06664a5d99a0b651bae36d2b37f3145",
"previous_hash": "a72b31187098cfc2940a1f16cfc8edecfca1121c7b37d157d640042aeecc45c4"
}
```

## Generate init py
```
touch /home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/server/generateKeys/__init__.py
```

## Command generate relative imports in python form root folder CryptoBlockchain

```
python3 -m server.generateKeys.privateKey
python3 -m server.generateKeys.publicKey
python3 -m server.users.registerUser
python3 -m server.cryptography.cryptography
python3 -m server.interface.manager

```