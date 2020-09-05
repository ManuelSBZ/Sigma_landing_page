# Sigma_landing_page

El presente repositorio anexa la solución a el desafio propuesto por Sigma.

- Para explorar la solucion en producción ingresar al siguiente link : https://manuelsemecodjsigma.herokuapp.com/signup/
- Tambien cuenta con los archivos necesarios y ser containerizado, solo usando el comando "docker-compose up --build"
en la carpeta que contiene el docker-compose.yaml.

Recurso admin : https://manuelsemecodjsigma.herokuapp.com/admin (USUARIO: admin , CONTRASEÑA: admin)

Caracteristicas formulario:

- Selección encadenada Departamento --> Ciudad.
- Realizacion de peticiones asincronas para validacion de campos(mejor experiencia de usuario).
- Limitación del tamaño/'length' de los caracteres.
- Validación de campo email según el dominio.

Caracteristicas del administrador:
-Exportar csv de la base de datos una vez autenticado bajo la url
(DEBE ESTAR AUTENTICADO): https://manuelsemecodjsigma.herokuapp.com/admin/sigmapp/singin/

PD: el recurso colombia.json en https://sigma-studios.s3-us-west-2.amazonaws.com/test/colombia.json
presenta un formato ilegible para ser tratado como json. Por ej: Atlantico no prensenta comillas dobles,
por consiguiente se usa un recurso auxliar helper.py para proveer los departamentos y ciudades.
