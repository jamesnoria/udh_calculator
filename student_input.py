import sqlite3
import pandas as pd


class StudentInput:
    """ Student registration for the first time (only if is new) """

    def __init__(self):
        """ Data Base Connection """
        self.db = sqlite3.connect('./students.db')
        self.sql = self.db.cursor()

    def student_init(self):
        """ Getting student_id, password and dni from data base """
        data = self.sql.execute('SELECT * FROM students;')
        return data.fetchone()

    def student_welcome(self):
        """ Validation for new students """
        df = pd.read_sql_query('SELECT * FROM students;', self.db)
        # if data base is empty:
        if df.empty:
            print('***** Bienvenido a la Calculadora de Promedios *****')
            print(
                'Necesito registrarte por ÚNICA vez para acceder directamente de ahora en adelante')
            while True:
                student_id = input('Código de alumno: ')
                student_pw = input('Contraseña: ')
                student_dni = input('DNI: ')
                print(
                    f'\nEstos son los datos que ingresaste:\nCódigo de alumno: {student_id}\nContraseña: {student_pw}\nDNI: {student_dni}')
                print(
                    '\nEstos datos tienen que estar correctos ya que si no lo estan, TODO el programa no funcionará')
                right_option = input('¿Estas seguro de ingresarlos? (si/no): ')
                if right_option == 'si':
                    self.sql.execute(f"""
                    INSERT INTO students (id, password, dni)
                    VALUES ('{student_id}', '{student_pw}', '{student_dni}');
                    """)
                    self.db.commit()
                    print('\n¡LISTO!, ya estas registrado')
                    break
                else:
                    continue
