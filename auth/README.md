# Autenticacion JWT

Este paquete queda reservado para las funciones transversales de autenticacion. Todavia no valida ni emite tokens.

## Responsabilidades previstas

- `auth/security.py`: hash y verificacion de contrasenas; creacion y decodificacion de JWT.
- `auth/dependencies.py`: dependencia FastAPI para extraer el bearer token, validarlo y obtener al usuario actual.
- `Services/auth_service.py`: validar credenciales y coordinar la emision de tokens.
- `Routers/auth_router.py`: endpoints de login y, si se necesita, registro.
- `Services/schemas/auth_schema.py`: esquemas de entrada y salida, como login y respuesta de token.
- `repository/usuario_repository.py`: busqueda de usuario por identificador de acceso.

## Pendiente antes de activar login

`UsuarioModel` actualmente no tiene un campo de contrasena hasheada ni un identificador de acceso unico. No se debe guardar ni comparar contrasenas en texto plano. Antes de conectar el login, hay que decidir ese identificador (por ejemplo, nombre de usuario o correo), guardar solo el hash y definir la clave secreta del JWT mediante una variable de entorno.