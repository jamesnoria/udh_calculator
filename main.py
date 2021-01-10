from udh_automatization import UdhAutomatization
from udh_gui import UdhGui
from tkinter import *

if __name__ == "__main__":

    student = UdhAutomatization('',#-> CODIGO DE ALUMNO
                                '',#-> CONTRASEÑA
                                '')#-> DNI

    root = Tk()

    student_grades = UdhGui(root, student.first_course(), student.second_course(),
                            student.third_course(), student.fourth_course(),
                            student.fifth_course(), student.sixth_course())
    student_grades.main()

    root.mainloop()
