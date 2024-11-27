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
        [x] El servidor debe de generar una conexion utilizando sockets
        [x] El servidor debe de permitir conectar a los clientes mediante la exposicion del socket
```

## Cliente

```
    Manejo de Claves
        [x] El cliente debe solicitar y almacenar la clave pública del servidor.
        [x] El cliente debe generar su propio par de claves pública-privada para la comunicación segura.
        [x] El cliente envia su clave publica al servidor para encriptar la informacion desde el server hacia el cliente.

    Registro
        [x] El cliente debe enviar una solicitud de registro al servidor cifrada con la clave pública del servidor, incluyendo la clave pública del cliente.
        [x] El cliente debe recibir y almacenar el ID de usuario asignado por el servidor.

    Envío de Transacciones
        [x] La solicitud de registro de transacciones requiere que el cliente se haya registrado.
        [x] El cliente debe enviar órdenes de compra de acciones cifradas con la clave pública del servidor, a partir de información en formato JSON.
        [x] Las transacciones se basarán en el número de ID del cliente, el tipo de operación (compra/venta) y el nombre de la acción.
        [x] El cliente debe asegurar que las transacciones se transmitan de manera segura.

    Verificación del Libro Mayor
        [x] El cliente puede solicitar y recibir una copia de sus propias transacciones.
        [x] El cliente puede solicitar una verificación de la integridad de todo el libro mayor.
```

## Requisitos No Funcionales

```
    Seguridad
        [x] El sistema debe usar algoritmos criptográficos fuertes para la generación y el cifrado de claves.
        [x] Todas las comunicaciones entre clientes y el servidor deben estar cifradas.

    Rendimiento
        [x] El servidor debe manejar peticiones de múltiples de clientes.

    Persistencia
        [x] El servidor puede emplear un sistema de archivos o un SMBD para el almacenamiento del libro.

    Usabilidad
        [x] El cliente debe tener una interfaz CLI, que soporte la adecuada operación.
        [x] Los nombres de comandos sugeridos para el cliente son: getKey register add copy verify
        [x] El cliente y el servidor deben proporcionar mensajes de error claros y retroalimentación a la operación.
```

## Restricciones Tecnológicas

```
    Seguridad
        [x] El sistema debe usar algoritmos criptográficos fuertes para la generación y el cifrado de claves.
        [x] Todas las comunicaciones entre clientes y el servidor deben estar cifradas.

    Lenguaje de Programación
        [x] Se usará Python como lenguaje de programación, bajo el paradigma POO.
        [x] La comunicación entre cliente y servidor estará basada en sockets.
        [x] Está permitido el uso de librerias en Python que generen valor al proyecto.
```

## Restricciones de Calidad del Servicio

```
    Confiabilidad
        [x] El servidor debe asegurar la integridad del libro mayor basado en blockchain.
        [x] El servidor debe velar por la confidencialidad en las operaciones realizdas por los clientes.
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

## Commands for generate keys in client and server

```
python3 -m server.generateKeys.privateKey
python3 -m server.generateKeys.publicKey

python3 -m client.generateKeys.privateKey
python3 -m client.generateKeys.publicKey
```

## Commands for run

```
python3 -m server.config.configServer

python3 -m client.config.configClient
```

## Config venv python server and client

```
python3 -m venv server_venv
python3 -m venv client_venv

source server_venv/bin/activate
source client_venv/bin/activate
desactivate
```

## Command for generate pip requeriments

```
pip freeze > requirements.txt
```

## Install pip requeriments

```
pip install -r requirements.txt
```

## Architecture server

```
.
├── authentication
│   ├── __init__.py
│   ├── loginUser.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── loginUser.cpython-312.pyc
│   │   ├── registerUser.cpython-312.pyc
│   │   └── users.cpython-312.pyc
│   └── registerUser.py
├── config
│   ├── configDatabase.py
│   ├── configServer.py
│   └── __pycache__
│       ├── configDatabase.cpython-312.pyc
│       └── configServer.cpython-312.pyc
├── cryptography
│   ├── cryptography.py
│   ├── __init__.py
│   └── __pycache__
│       ├── cryptography.cpython-312.pyc
│       └── __init__.cpython-312.pyc
├── data
│   └── database.db
├── generateKeys
│   ├── __init__.py
│   ├── privateKey.py
│   ├── publicKey.py
│   └── __pycache__
│       ├── generatePrivateKey.cpython-312.pyc
│       ├── generatePublicKey.cpython-312.pyc
│       ├── __init__.cpython-312.pyc
│       ├── privateKey.cpython-312.pyc
│       └── publicKey.cpython-312.pyc
├── interface
│   ├── __init__.py
│   ├── manager.py
│   └── __pycache__
│       ├── __init__.cpython-312.pyc
│       └── manager.cpython-312.pyc
├── keys
│   ├── private_key_server.pem
│   ├── public_key_client.pem
│   └── public_key_server.pem
├── models
│   ├── bagActionModel.py
│   ├── blockchainModel.py
│   ├── __pycache__
│   │   ├── bagActionModel.cpython-312.pyc
│   │   ├── blockchainModel.cpython-312.pyc
│   │   └── userModel.cpython-312.pyc
│   └── userModel.py
├── __pycache__
│   ├── app.cpython-312.pyc
│   └── __init__.cpython-312.pyc
├── repositories
│   ├── bagActionRepository.py
│   ├── blockchainRepository.py
│   ├── __pycache__
│   │   ├── bagActionRepository.cpython-312.pyc
│   │   ├── blockchainRepository.cpython-312.pyc
│   │   └── userRepository.cpython-312.pyc
│   └── userRepository.py
├── requirements.txt
└── services
    ├── blockchainService.py
    ├── __pycache__
    │   ├── blockchainService.cpython-312.pyc
    │   ├── transactionsService.cpython-312.pyc
    │   └── usersService.cpython-312.pyc
    ├── transactionsService.py
    └── usersService.py

20 directories, 52 files
```

## Architecture for Client

```
.
├── config
│   ├── configServer.py
│   └── __pycache__
│       └── configServer.cpython-312.pyc
├── cryptography
│   ├── cryptography.py
│   └── __pycache__
│       └── cryptography.cpython-312.pyc
├── generateKeys
│   ├── privateKey.py
│   ├── publicKey.py
│   └── __pycache__
│       ├── privateKey.cpython-312.pyc
│       └── publicKey.cpython-312.pyc
├── keys
│   ├── private_key_client.pem
│   ├── public_key_client.pem
│   └── public_key_server.pem
├── __pycache__
│   └── app.cpython-312.pyc
└── requirements.txt

9 directories, 13 files
```

## Show diagrams

[Show Diagram in Draw.io](https://viewer.diagrams.net/index.html?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=CrytpoBlockchain.drawio#R%3Cmxfile%3E%3Cdiagram%20id%3D%22XXn5lf5rI0VbRaILsol7%22%20name%3D%22ClassDiagramServer%22%3E7V3bbuM4Ev2aANMPCUTdbD%2FmMr0DbHo36O7B9jwJisTYmsiWQ8lJPF%2B%2FpG62LOpiWxRlu4AGOqYlUeYpsqpOFYtX2v3881%2FEXs6%2BBS72r1TF%2FbzSHq5UdYwUnf7HWtZJi26MkoYp8dykCW0afnj%2F4LRRSVtXnovDwoVREPiRtyw2OsFigZ2o0GYTEnwUL3sJ%2FGKvS3uKSw0%2FHNsvt%2F7Pc6NZ%2BrvU0ab9D%2BxNZ1nPyJwk38zt7OL0l4Qz2w0%2Btpq036%2B0exIEUfLX%2FPMe%2B2zwsnFJ7vta8W3%2BYgQvojY33D%2F%2BETl%2F48eXtf1qfLv%2F59YOlesUnXfbX6U%2FmA7kizdNXzlaZ%2BNA337J%2FlzN%2Fa%2FEntM%2F7z5mXoR%2FLG2HtX9Q%2BGnbLJr79BOify4DbxFh8vs7fT8GgkLbCHZWJPTe8XccJlCzVtplZHsLTNI7ncD37WXoPfvZFR%2Fp0COTfUrfGZMIf1YOBsqHmMomDuY4Imt6SXrDNUKTFJdUMLXROG342OA8MtO22RbGmpI22qlsTfPHb4af%2FpEisAcaSC3BcR%2FD8QMT%2BnPLoHx4c99eMDBe6Bj%2BSL9hY2j73nRB%2F3YwA4E2sOHyqFzfpl9EAcPLmXm%2B%2B2ivgxX7cWFkO6%2FZp7tZQLx%2FGDQZovRrEqVTVDULV%2Fxgd%2BYgM2yfMizQTtM3%2B7Nw4aMdRrkgbAPPbpzbZOot7oIoCuaZLNSLXSvhqJ4LlRKjFcVFN0vCoukcYRmbomRFK8nKlWr6DDjXey%2FIifm2YosMG96AisIt%2FZJMn39D9AfTvhU0Sv5X1S%2Fx%2BCnPFMspCVYL93rnFtUw0mu3%2FkjvYhJ4%2FWLPPX%2Bd3EA7tucMnbT7BxLQX6QqP%2BxFSP%2F7FiyC3UuSZ%2B62zumVYQw49%2FLN15v3SFYX9hZIX34mX%2Fh0ibnOsIm%2FmmRfxTJ1nT6EfbUkydPMvCdzmv4fDzG9dNE0xld0TVFUR1G4T7on62UUTJnWXGdPpYKQPDi55LcvW1%2FEoGYvsbMOUFGPXyoiwSu%2BT97gYREkC4Pn%2BztN2drg45eocmVgg%2BEtpo%2FxNQ%2F6puV7KtysKaD3vvixVpt5rosXbFYHkR3Zm7U71gOx9Bt39B8dlnvlxrgyHhh6xh3afKb%2F2OUkoose%2FS1UJbB%2BMF0fPjBbI8RN%2FWThLc%2F9dLKrLSe7Kmyyl%2FV0SQiYeOdCkNkq6CAJmFMsfbyB%2FCeTiIdrVBILrSwWGkcEfPsZ%2B09B6EVewJ5Pkmt3RKMJ%2FaJ4e4sZJl4kEnZDbbnGi0LdgCV%2B8Eu8rSCEXrhPcvFLxcqejMA%2B3ZjUMn92uN3EZpkVpiYiX5OE2H%2FJR74jDTa3F9T7qeoyF5COevtW2xtoymFoSrPsQwnTlHe3yvXD7a8PhJaP0fj19u31jVyXl8zEg3pgI22HGHyo4fhQaKSXpMUYC3KiuNJigoIFBZt0o6ja88TgdmNZ3sKLLKtP5eqm65W1In7lb%2BxqHJO7OuhD0VTD1KpQT1vCN59KSnzP1%2BRfZrt8Zb86%2FY%2F9%2BBv3ufAg0Pz9aP5qzbqPi8xdyoUp%2FhF4yMd5yAeAznGQ%2BfpbEOZjUN%2Bgvhv9Y4dgO8LUQQ5DNrlqlDjokkHoEo4TKUyXcL2YslswxQtMqBT9G6%2FDsgt5XrFRUym6aaqZxZq2AEGaykFEQyNRXGgZkyfivSeQgFMv1Kk3a8VFLUqL0TKKjjJaqHtR4ZmCYBb0ZBYU9GZX3jAJ7Qq9fdOdnZCt8dYyWVisV1wZmd2n11iiGG%2FKINFT0VK%2BcN9huXr2PcfCn0tqOtBJebxXHvfOJuC2QGuI3303REA8H5KOjEnasT7h92gahjaq7HNfTmWfoaboWvFkOPsxpkMxljLEbLnEC%2Fd0R3gyLv5ONB7zu6SujL3yI6v%2BF%2F%2F2pdLDAL%2Bjl%2BhVhSlTTWLxMwB1UaYLj9EAFuvoPI962Dn%2BJhd2YXkeEzBYgcdqtE9D%2B71gm0pI%2BWjde4OeA7Huxw%2FjDHF1Hyc%2FQaY42nN%2BHCim%2B4%2FhBaIRMW1%2B%2BNiDgTxAA9kct7OURqogU0ktJ0I%2FxZQJsMByWeBxxvtm26nKNrXOTQTM7uteVCB7evhWdY2tuR3eqWBTOiV%2F97EdwLyVLV%2FHG1RltDsUp5THr4kgABMo1dBRKzKVq5lArvoyRDGBajneDUzg8UxgA%2BycLeBc2EUxgSqErodvs8h3rRMmMFcx4ogOEK4BGSwnL6aO71XnNIjhq1t2DjygYFa2h7UKwNgfjOYZCWCIA8P1wqVvr2F2DBgQmCEyAXFm2HkFOIYCRy8hvX5bgVfrlVcblwOIXIIFmaIiiPm%2Bgy3UsTvFWXSQDtosmAYL2%2F9903oX%2B7bYTYHYXPMYxEQZG7O%2FcRSt0%2FCfvYqC4ojSUSPrX%2BzDjaKoWcNf7IE3qqJlDQ9Z8C%2F5tN7%2B9ISJR8cg3gq02erD3v2AQB79%2FcGKOLgRSlWJbELNxrohnfAxJ9i3I%2B%2B9%2BHo8QONbbwmx11sXpNK%2BefITa7jaRBwzILNqEpq2LRz7Xk%2F%2FSN5gI1r5Tzlc2sp8Xrzx6yWmJs57GxmdaDshYT0r6tq0sU%2FLGjuf%2FXo5KJwXFoLsAYF6YVQrK7vFNVFZS3DlRBUmJ1AZ5m7wRHwN8fcndaRDVjXXc6o2%2BEAQXzrOvbtQNRJz5wfOqzOjSlKM2JyAg1mXjLNJsoNRyZ%2F0GFD9yZYaGJWtJ33HUy%2BkdhEMzM6TfhK6ZtsOS4kQpJtkjA%2F1dWfU9qPmb4RdaxWDvi%2FndGBtsg5rvP2HETpV%2FXRFPnUH2zPp%2Fu2AMJNBmOl711XjukJIF5WJpkNlNRGZaA24oxEnFU1QbTX%2B%2B0FxteF7wPJDQn1ld4Bsna7XLV9Kw33TXiAR7fyEgKR%2BaZ%2B4M3fIWrBgTtUPFNAfntteddFoAR0u7TD8CIgLQt27UPuMgupdokHCLkfCZthfCjDoYOxbjD3%2B9CDZTZbc2wvXx5YTzOd2dUU3EUtsfZciTpo4bFmFzD3WdCFEJBpxUvf4TKSo1L0yIzVn502ffUHua22nuIaOOOU1kDHioKFlxxx3TxCiEhx39vQ2Dm%2Bl54BDRpXA%2BTqulZnJTrYjh07O67wX6rGowuIIKhDKgyjLbVmxamKsBDvTaqix2jZHST3bUysNqBcu2z%2BMWw6obl3E5Pq2U6Prv0v20nalD23say%2FX9OVV1xFnBshA8a%2BxzL962K80yDs0jJOazg3iJHbUeklv6LxGKFWD65raN6c1dD%2FJqq%2Bh8xYutQLOfNDacBZbzF%2F3ay91qw5SEVtNwZKdFEFXcCtaL%2FEAXzCMAuc1CTwM7%2BXeVvYi8qJ1169Wo%2BjavhpdvJzOh%2BzFD%2BzD3gw4D8GcR4XjXZ18xXWakCnMadIg%2BUpE8lU97igjTZqAF5Z8VS5zW1iswFeG5Cv6fxRYruccFiECVdKrKkGTMn3OJ%2BBMUWtK%2BZSRzZ4nIGxlE7Y5UV9N2BrI4MhLdmHnApMFHUAJAWHbhg1oRdjmK07hqq752phHAcoWKNsTptCAspXLPkbenJqMsTYYHIO2JEHwMkD6LM4l6nG4YCE8m4WwjfXQaDO0n90zO5wNcmLjdy9YhdaQ3g%2BoA8HUQUX9tGoWmusJimOhjXKqF7DQHbDQ9bjzWGgu8KJYaAMytiQSACfDQrPNlTVJ5EJS5Gv6S25%2F8JwIthrLluEL3DYybTEbqGAq1zlK2Ts8FEM5sJ%2BnW2COCZaBdTxY65gXWONaScLOpDXKBXJY6TMIqckOqanqjdEUU9O41ccNYSY1VNWRbY6cXUyNpckK3f4Q5%2BGuVv1m4g4UEfnULgRrqkR0oOnOWxUzBvpyeXWNgbwfmNRiTWqjohp%2FNeHMN5OE7RU1yrlqQDgfTzg34I6MlvaxKOu4jDrBSzaM1GnBl7fNXxtxzqPmb%2FNXhW3zN8o7EPJt%2Ft8zdNbg5wr1cysokOwpymjX0%2BXNZI0XMxSXPQpbGCR6usfbblQrvXjTB6bX7HD%2FOvVgsnVssml7m2y8%2BS5sd4FRPlgLLLYOLLZ62LMIfRPswuhMOCZr%2BIu8%2FNCbhT%2BpkR1h622FSeURQiLyBKhdGOF55%2FWWQYghReC4FIFi5aJDI9KQEHAEDLbrbsHQ56rU2CvALg721dKlOgGQvzzkXezjk0W%2B%2B1Zw0Xt10c22lFx2Snbn3prJqdia78cFLncQXK5u7lK5PLnhhQDEUbkm7AMYvpcPVO6p6Alz76Jj3PkujMo1oeaYCCq3AXYelcuDXRSVa0K8bviLvHwfCqhcEGKgFApUblbOCEhcSQD4VG1bcWUpQEFiRIMBEFofXjSzssrdPaqH%2Bi4BfMFxFAa%2BFQXNi2HnvGrNvAdK9bxd5dbUmDhKtZyyzPZ%2BApk6CDI1OyWtRlxUXpKcIkpcMuEEJ3vATjYwqSejHvYunMWf76KY1BHUzRLCpNbDzmNSebCLYlKzQhOwyA94kZfvNgGTCkIMLEKBQsoqWQCHJxEA63mdFPvok7yr7g8g7wfypEBFj5jXdQigiwPdIZjlPzPce53i1f0B2sKz3QHti0A7zXA%2FHbTltgIf1ysf15Z%2FR1nNmc6pmSwOtEXNUNF995xLrC6jKWU8%2BNVldEMUIGa5bMBmS8KPBBoIoQkNoSVzoqa4jFrcj8ApoqprHKFRx8KEBqoOSOSmjjcX%2BJuOIJYmV3cb%2B8bS%2BLNe2K6EcpVtiKV1EEurh50TS%2BPCLmxXAtTLHv5SL9%2FvTTmtxhzgrh3f5BzGqh%2FY35E3nf%2Bs7VPoIEg4zNl5gfxWPN8s%2Bu8jID1P9HRG1M14YDbFIc9Wov7X9yOSywHtI9D2wmQjgUXtvn4j0XX7FwDxHjaRwPQ%2Bf7BdL1z69joBHLZPSkSCZYDktg1soZSMBEyFoUyFGscXgOgBCNhMfKHgR4zoPnzinWcrxLp6jXVx8lT4sS5V2D7Rcgmun8RehGnFaEiMGEBihDZpcbysgXhyo4mSG6TwoqTAyJ8rI1%2BXZME7pGvPHIuTt2daJaHkq%2BlBowMaXIYGH%2B19HBJ3JTZEHWA5guOQRGSrNMDOOS6RC7uwnd%2BQmChR%2B56Mj3t%2BB4%2BAFJ%2BuDSl%2FPvheCAciDQCH%2BbotCsC3nhHm0RazBKBfAujPq7UE46Me7%2B6L3LCKpAu2ca%2BfDt9W9iLyoiqWpfuMxGrOAuaOuLlDZ4YPkwcmD0yeAybPSUd3gcPtlcMdj9uReUhXBdF543L5TlbcGcKvQwi%2F6i2ir3mFg0L0VVgx8DEU%2FryTQZx1aBjsFm%2FfMyQIKqLbNWC8%2F1F53CkvalP6GI7KExHma4CdV%2BCZB7uoMN8YjsqTss6fmLMjsqItyBME3I6XTCj1e5GQQ6nfCwGdJZqcTi1QgPoIqAmeU6cP0L4MtKGq8yWhDVEToMTaciO8Gss8bgQJK%2BmLkFZCHbtTnIVD6KDNgmmwsP3fN613sY%2BK3RSIzTWPQcxxsTH7G0fROo132KsoKI4oHTWy%2FsXoMOVGUUZZy1%2FsiTeaPs4aHrJwR%2FJpvf3pCROPDkJclnlTdpm9%2FCGhCzoCwYo4uObCbJ9fZBNqoNdcmNRBLKNOsG9H3nvx%2FXiQxrfeEmKvty5I5X3z5CfWcJXHWCY7B2iq6fayr4ddT%2F9I3mAjXPlPOVzeyhQsFY4ZBYguFEmWxm6Y7twLeytqeRHgF%2FbuZAfr3a1y%2FXD76wOh5WM0fr19e30j1%2BXQ6WMw9RZ%2FxhYExE0FKoiKqHr6lFxBpMKio7K%2B4B6hrHXApnMlBYKmEsnPbiKm4XFbKAHnQeAcjzFSk5fU08FWvnCfe0%2FWyyiY0mVrVhclV8Ar6NwrqFa3e8XJued8dLAdlvt6ECY%2FMkx%2BAOi8fCiuZhel2CFKfgoLPrMHtwdZQ%2FwVP%2Ba6lIq1vjuuy2deghRiszYsJqTDpR2GHwHpOBwKk%2BhEUwOGOB07pp7B7OvT7ONk0HMtgC6oYO7rTUoWwHc89cIIE%2BCBJPNAI1TkgbJD3rZr3k141uJIGGOogL04bHsRiKDTx3lIJdieVs%2B%2B5%2FwbQ2G67Se1pNYgMj80Y6z%2B8GPeAYo8BWsK06%2FlkByQcMeTcPWoj1ui3sWeRD7qEF67GG07RAJhiheYxLmKDfsMzlTXDxETkjrhcmjWHquKnBOtC4Iunb0E43qoxvWkpZk1ElXvGSl6CfM%2Bk14ZPtsZr1f12a5XzYmtaVNjCqvRNoVVryCrW6ewHgmQIQOgDgfaRG0HumKu9DXQ5oXOBHPSEiBjJBeg8YUCNG47g0zJM2hyoQC13w4hV5fk%2BzsuDSDTaLvEVUQf%2BwKoTG1eBkCtZ9DRAB20ocjY2SCkZWHoqh1F40n9DWK2FCF0AdZ83badRvGp2oUoeD9aseKflh34UiU918gY1d4hSnxOyNeoS9wZqBiYymnIQfkMKKcQ291NfzqzfYn6qLh2U9xS7bRF00x4NI0m7IDEbL%2FjFib3tZhASlqHKWkVx65mTxnvyItekhZ9zJGW%2FNiv7qWFFzKH4OnJpKQ1JxjddBnpjKxl3KH1iteW43tsMkAi3ECla0gpXzLlNMTkvToKfKbBygY4iPduR7hPPJIejwcEgpMyavIkVuVeqX88Q0ZYdFLlJYFB6t%2BxZaobYEdZ3aUm3EXVqVZ5267BwBiW%2BSq%2FvBxexLSE5dJJ16B9RCSFsW4r%2BgMrWbYQX2C1RRef2XQ4AWNcPuqFRbDedwfUzwb1mR3OoBz6paBNV3LvZW0ND%2FSu%2B2r8hSBlgteUhj0AQiTsMvcdDALz7ZVlgNALWV9A3KSJ20kXhAdKegCUdJ4E3sRNopEqiJ1EWS7GyWZJtU2WU6XkWu4ky6mTpiSpncrQuzcIypXLR%2FtUpaBtrpwcKdjNlRusGMjdlJJ%2FSM6LGOX5tx0fF9E2jxuZbaVKPVKqjlzDZW9VmUwm29Cxwz8Qkgxelrg20CVB382zG4%2Fql4TSDSNN62FJ0OWeI7OzJDStCB3KD28jIVf1mDLE51rbEQdtMtFq5afxDlECJHcXh0QB4limwxEgalEUpEFXjAaTRFeUI%2B%2FoS%2BKkbPwYgMQZHJU3HInb3UV2RhJnlDO5%2BjXAdFPdljo0APtLb7tLVT12I%2F5B0ohMY9fFMuuFi96h1d4hSrjOVIE2rlJ6F3LRDLym75beTmQ7vW%2BD79Ei1rhFTtOPvQGl6auCRfJSNWzrRW0kRcWauzu7zQansnSDkXIJguVHSnUaGXIg58hQtLuLTzPTwrOVyq3pDlGSMIKVpF4LoooYUs%2FmkYaUXuRBCgMtY2UYd2Le7M0b5SNcoSIE4ZrFM2R5SNLmeVYERzwNXRFDoB9JwBIXNniyXfbfAhezK%2F4P%3C%2Fdiagram%3E%3Cdiagram%20id%3D%22nj8Vv5NBGJqPoMXIBL6p%22%20name%3D%22ClassDiagramClient%22%3E7V1bc%2BI6Ev41VE0eSFm%2BAY%2BTZLK7dSZb2cnW2T1PlLCF0URYjCwCzK8%2Fki0DxjaXxBcgqkpVcFuypP5aUl%2FUdse6ny7%2FweBs8kR9RDqm4S871kPHNG17AMQ%2FSVklFADcXkIJGPYVbUN4wb%2BRIhqKOsc%2BijIFOaWE41mW6NEwRB7P0CBjdJEtNqYk2%2BoMBihHePEgyVP%2Fh30%2BSah9s7eh%2FxPhYMLX4xskd6YwLaxGEk2gTxdbJOtbx7pnlPLk13R5j4jkXsqXpN5jyd11xxgK%2BTEVbPYn%2FmEtBuz36qmHvv3sOXfDrnrKGyRzNWCPrWacBhLOleo4X6XcEGOYyZ%2FzKXlkcCp%2B3i0mmKOXGfQkfSGqCdqET4m4AuLnjOKQI%2FbtTfRSQmEIGkPenEX4Df1AUQK4pAoEOcQhYqqmRwmBswiPSFpioQAArrxSPUeMo2UpS8Ca0UJEEZ0izsSoDFXBUdCkwmkMFGGxgdruKdpkC2bLVkSoxCtYP3uDgPihQDgBEDMPCA3HOLh2KLrAsLJo9Ow8GAO7AIyeWwEY1PjzP48%2FjcFfrxR2n%2Bndv5a%2FxwWz4z4G4wUxMdg8JAs8JTCUUIwFB1%2FUHclBSHAQit8ekhAIgmQWFsvMV3WDU4mWN8HE%2Fw5XdC7HFnHovaZXdxPK8G8JTIqnuM24WjFNN1PiRdZcQyyRfU6RADukJ7jMFPwOI74Wg23YZcUpZAEO7yjndJpKwn6hO0o0ymdCqbyYwMpIi1sgLfagQFoAqEta8lO3Y7pEQufjt4ykuL%2FmctWXDKZCGL6KmywYfQF2xxRNG6CX%2FDfNm5iDxkigGTA6D%2F3uThXTcVTZrR%2BqlpTB7hhOMVklFUTDcCrxUc0%2FMCoGZBovMIzEvyca0t0iyTN3qVNRMoohLyy%2Bub3pR7K6yF4Ae7ZMbhCxxHRTbOJbg%2FRWLFVd9RB5a8aSp7nrltxA%2FY9ZLIqGh3jcMa2eYXqGUfik%2B8zGlzxVyEHy4KTIl5utGzGoaSd2VgIh7HGnOKOv6D7pwUNIk6UBE7JDSlcHgsa8dG2QzMBh8D0u82BvKD%2BUcEsSFXXHJFYzJtj3USjnNeWQw83aHe8DsfA7d%2BJPsOXeuHU6zoNEz7kDm2vxJ4szLpY9MRaxJch2kFghFkiuEpVM%2FvKVNz%2F51WQXq91Rcz0tV%2FlUtwqm%2Bo4ISOFei0CqOoJ34T8VSBK0Afy%2FUh4euiAnFFZeKKwCASBwhMgzjTDHVD6fJWV3BOMQ9lnhxuEEMcxrBN0xjwO9XxPmtl7e21vey1hc3sYHNwpoAADGhU%2Fy0bhkf0h4eUozrtDvR15hMxEK%2FSFDv%2BZyupXsRxEi4zWGFe2DHp1OYeiXDrHa1nyxMpU2VRViSa0K2jBMazRwCtv4t1zKixsp1Rqqlu3POEukETSMlEFWPksOYHAcVWt5TWp57pEWnVOXQZc%2BeAty5AcotesFxyY0oCEk3zbUu3gfR75CYVPmO421Nsmwn4jzlTLc4ZzTLDsFy9jq%2F7L%2BrZNe%2FqUeF188LDNXK3WV9FV28B12thgknTMP7TNvlTItJlyA3oEqQwRy%2FJbtXfWYORqzS8Ms7eWWav0EQxhoF1u7LjYj62Kz8uuxA4rW49oW5DTqom2wT2GD7TEbnucjgr0%2F0OmeuovXufe5MDPRiYtnzFyo9cP5PJ5AzRiDpzbzPnvwchBQUXVMw2EShpwzdJFoPEISXT4cQvGciB1dKDUc%2BUM5PT4XFk1RtZ1frZ2fKPinhHMKFUtg2HUpln0d0KkhoHMAd3CsRVFXSMccaHviE9kT7XurA8SHs9h0Gb6i1cfd1ueknFwcGFEWDI9guZppMFoBg6EAR3z%2FZKg69hjbl6E8O9lMrDNuD00hJk02OINRtKCsLKCrhbo%2BoSY0wGHjEq0l7PNImDdB3qvexc4Ljo3XTOPQ0sIrdInhCAZDGMMQaRzaweENo8VwRKj36k3g%2Fq1Qw1AjDJBgH3KkoWgdiulqyBkMI70wtQ2D3h5aR2E0XykI9iFQi82Cy6yVqluLuFhym%2FQy%2FJrDkGNedjKi6uZmDHuXH1m9uKkjJgbRc%2BeK547ed%2BoNw0hJ1ht%2FSwCgJdY%2BqpZ4P0FkpnnfDu8ZimbC3ihb82vZsg%2B0qeGu0cpE4VwdnNRO4fNAQ2%2F7bSNQdIhVw9EWHB%2FgvaZeB1Wfdm70tDOw%2BsederWBWVeSbO%2BskmRvB4N%2BZ3%2BibHz1jBgWDIhfS9dE9mz6vslDybPJMeIGsmcLR5N%2FF1GAQsTE7voHWkX5DNore2%2FgEW8NBJZTML3Mfl1pqmmXtiDZylfUGc01ZjRbe4Wl72aFBTg5WbGL3jBZ3ysmrPwrJg8ppDoD4XIzEPZlNDP8lqzZZSr5zW11qn%2BciJC0eMSxwQsywvKDqpBrm3OW7%2BSUVsjbUMiT%2Ffikt0kW7QJOXdmHVtGbY3X24UezDw%2FA3s8rioWw15V8aBW9RFRv%2Fde69bfv7ovgG9KpAueKxuFc0MpPnxzZuJaCxhKC9ZQ8IzB0dnabYPg4mhG40rPjjAHRM6RNQHK5nxqONuHgB97TfjXRdO2eatQ91c%2BHiwv9FMCtK1xs5T99se2t1gGt1gJa5k7wM%2B%2FSWn8cLSMqVXy%2BrlhUHO3UuganVsE2UMFJ5AiWbJCVRraSww%2Fb4a2ybfmUVmPZlCdyJLi2ElLjprAPSidDy5nY80otlpNbl1N5e2pYoLj55CFVNKmG6wxUw%2FaguEXXcaxeaZunuq1OYXWs98ppdfU8Fqzot8JiufCiPR8EOnsOD%2FrZcYJ%2Bv7hJYSnAOZFvDtk34i83Osp7jmq0fWqUt1A3smqL8ro6yltHlHc%2F7AUfESqEvbYor%2F5kxVUoxBfjhkriikcf7aolsHhs69odWXMw6yQx0GhcpXNY65mN6plu3l1bqHD0akvuATnMm0zuAbeGYXYy6T3CxOs0mN6jztUdTO9J0zQO5vckOlxbX8ez86dDs5%2Bq1%2F73amb7%2FkQjkKbopbkjwB3kZrpVGJgZ1OVtt%2FUR0s9kXHzoe3hVJ48ce%2BzgerXKM4XjalJ5KoTjcnOrTqFWx%2FIR07bGOdgaie53ik%2B7UAPp1eXTtvMnQ7RP%2B%2BM%2B7QOwAyPv1C7EvS6ntq1PeXwmvbN99xkKPWnyDn0xfVtwaMtmS9q7Xn2qfdR9pFH%2FfKhn5nrzWXEa9c8WINGmzBmYMsDIx02Kddra4iZ506Xhl6KZmbhJXTGTNDx0KDySxh3OPDziWG3D5oAMbLeG4V4MdCXpBUdDF1f9yhhcbRVQy9Hmyc%2BS0NlkLaSv3ljPfRUgfSypAIw0WlpSQ%2FxIOrGRo%2FVoPiBadqui1TVuxQa%2FLVsxpW3hOvatiImToGnZ6uaEy1Y5KWXCla9h9twGhGvQhnBVKAep8%2FHwIlNyYOKj%2B4O4ZFQqkRtYZET8ifpIlvgb%3C%2Fdiagram%3E%3C%2Fmxfile%3E#%7B%22pageId%22%3A%22XXn5lf5rI0VbRaILsol7%22%7D)









