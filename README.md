# Calculadora de promedios - UDH

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/jamesnoria/udh_calculator) ![GitHub top language](https://img.shields.io/github/languages/top/jamesnoria/udh_calculator) ![GitHub](https://img.shields.io/github/license/jamesnoria/udh_calculator) ![GitHub last commit](https://img.shields.io/github/last-commit/jamesnoria/udh_calculator)

</div>


![image](https://github.com/jamesnoria/udh_calculator/blob/master/assets/init.gif)

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
    git clone https://github.com/jamesnoria/udh_calculator.git
    ```

2. Acceder a la carpeta:

    ```shell
    cd udh_calculator/
    ```

3. Instalar las librerias y paquetes necesarios (dentro de un ambiente virtual):

    ```shell
    pip install -r requirements.txt
    ```
4. Modificar las siguientes lineas en el archivo main.py, colocar los datos correspondientes **DENTRO DE LAS COMIILLAS** y asegurarse que sean los correctos:

    ```python
        student = UdhAutomatization('',#-> CODIGO DE ALUMNO
                                    '',#-> CONTRASEÑA
                                    '')#-> DNI
    ```

5. Una vez guardado el archivo main.py con los datos, ejecutar el script:

    ```shell
    python main.py #Windows
    python3 main.py #Linux or Unix
    ```

6. Insertar el código captcha solicitado:

    ```shell
    ¿Cual es el código que aparece?:
    ```

7. Disfrutar de la calculadora de promedios.
## Notas:
- El script esta limitado apenas para seis cursos, si deseas para más puedes escribirme a mi email en la sección de Contacto.
- Caso no funcione, revise bien esta documentación o ingrese sus datos de alumno correctamente. Puede contactarse conmigo para cualquier duda.

## Bugs corregidos:
<div align="center">

| FECHA | BUGS-FIXED |
|:-:|:-:|
| [15-03-2021] | - "Notas Parciales" xpath <br> - Supports Chrome version 90 <br> - Espacios en blanco TkinterGUI <br> - Vscode files for .gitignore |

</div>

## Licencia:

- Ver `LICENSE` para mayor información.

## Contacto:

- [![Twitter Badge](https://img.shields.io/badge/-James_Noria-1ca0f1?style=flat-square&logo=twitter&logoColor=white&link=https://twitter.com/jamesnoria)](https://twitter.com/jamesnoria) [![Gmail Badge](https://img.shields.io/badge/-jamesnoria@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:jamesnoria@gmail.com)](mailto:jamesnoria@gmail.com)