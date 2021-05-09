from tkinter import *
from student_input import StudentInput
from udh_automatization import UdhAutomatization
from udh_gui import UdhGui


# Getting info from user-student:
udh_data = StudentInput()
udh_data.student_welcome()

# Log in into UDH intranet:
student = UdhAutomatization(udh_data.student_init()[0],
                            udh_data.student_init()[1],
                            udh_data.student_init()[2])

# Activating the GUI:
root = Tk()

student_grades = UdhGui(root, student.first_course(), student.second_course(),
                        student.third_course(), student.fourth_course(),
                        student.fifth_course(), student.sixth_course(),
                        student.seventh_course())
student_grades.main()

root.mainloop()
