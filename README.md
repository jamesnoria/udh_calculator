# Calculadora de promedios - UDH

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/jamesnoria/udh_calculator) ![GitHub top language](https://img.shields.io/github/languages/top/jamesnoria/udh_calculator) ![GitHub](https://img.shields.io/github/license/jamesnoria/udh_calculator) ![GitHub last commit](https://img.shields.io/github/last-commit/jamesnoria/udh_calculator)

</div>


![image](https://github.com/jamesnoria/udh_calculator/blob/main/assets/init.gif)

## Descripción:

- Este proyecto comenzó siendo una automatización personal para saber que notas necesito para un determinado promedio, luego fue creciendo hasta el punto que pensé en lo interesante y útil que sería compartirlo con mis compañeros de la facultad o universidad.

## Funcionalidad:

- El programa entra al intranet de la UDH y coloca los datos ingresados previamente por el usuario de manera automática e ingresa al apartado de Notas Parciales de donde extrae las notas de los seis primeros cursos y se cierra al mismo tiempo que entrega la interfaz grafica de la "calculadora de promedios."

## Pre-requisitos:

- Google Chrome (navegador)
- Python 3.6+
- pip
- Unix-shell (no excluyente)

## Como usarlo:

1. Clonar este repositorio o bajar el zip:

    ```shell
    $ git clone https://github.com/jamesnoria/udh_calculator.git
    ```

2. Acceder a la carpeta:

    ```shell
    $ cd udh_calculator/
    ```

3. Instalar las librerias y paquetes necesarios (dentro de un ambiente virtual):

    ```shell
    $ pip install -r requirements.txt
    ```

4. Ejecutar el script:

    ```shell
    $ python3 main.py
    ```
5. Registrase como nuevo usuario y verificar los datos correctamente para que el programa funcione correctamente. Entonces el programa iniciará.

6. Insertar el código captcha solicitado:

    ```shell
    ¿Cual es el código que aparece?:
    ```

## Notas:
- El script esta limitado apenas para seis cursos, si deseas para más puedes escribirme a mi email en la sección de Contacto.
- Caso no funcione, revise bien esta documentación o ingrese sus datos de alumno correctamente. Puede contactarse conmigo para cualquier duda.

## Features:
<div align="center">

| FECHA | FEATURES |
|:-:|:-:|
| [16-03-2021] | - Registro inicial para nuevos usuarios. |
| [08-03-2021] | - 7 cursos agregados.                    |
| [12-12-2021] | - Slowly migration to Selenium4.         |
| [30-05-2022] | - Quinta nota agregada                   |

</div>

## Bugs corregidos:
<div align="center">

| FECHA | BUGS-FIXED |
|:-:|:-:|
| [15-03-2021] | - "Notas Parciales" xpath <br> - Supports Chrome version 90 <br> - Espacios en blanco TkinterGUI <br> - Vscode files for .gitignore |

</div>

## Licencia:

- Ver `LICENSE` para mayor información.

## Contacto:

- [![Portfolio](https://img.shields.io/badge/www.jamesnoria.me-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://jamesnoria.me/) [![Personal Mail](https://img.shields.io/badge/jnoria.dev@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white&link=mailto:jnoria.dev@gmail.com)](mailto:jnoria.dev@gmail.com) [![Linkedin](https://img.shields.io/badge/jamesnoria-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jamesnoria/)