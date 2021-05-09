# made by: James Noria
from tkinter import *
from udh_automatization import UdhAutomatization


# gui: graphical user interface
class UdhGui:

    def __init__(self, root, first_course, second_course,
                 third_course, fourth_course, fifth_course,
                 sixth_course, seventh_course):

        self.root = root
        self.root.title('Calculadora de Promedios UDH')

        self.first_course = first_course
        self.second_course = second_course
        self.third_course = third_course
        self.fourth_course = fourth_course
        self.fifth_course = fifth_course
        self.sixth_course = sixth_course
        self.seventh_course = seventh_course

        courses_names = Label(self.root, text='CURSOS', padx=20)
        ta1 = Label(self.root, text='TA1', padx=20)
        ta2 = Label(self.root, text='TA2', padx=20)
        ta3 = Label(self.root, text='TA3', padx=20)
        ta4 = Label(self.root, text='TA4', padx=20)
        emc = Label(self.root, text='EMC', padx=20)
        efc = Label(self.root, text='EFC', padx=20)
        promedio = Label(self.root, text='PROMEDIO', padx=20)

        courses_names.grid(row=1, column=0)
        ta1.grid(row=1, column=1)
        ta2.grid(row=1, column=2)
        ta3.grid(row=1, column=3)
        ta4.grid(row=1, column=4)
        emc.grid(row=1, column=5)
        efc.grid(row=1, column=6)
        promedio.grid(row=1, column=7)

    def media_button(self, mean, ta1, ta2, ta3, ta4, emc, efc):
        try:
            ta1 = ta1 if type(ta1) == str else ta1.get()
            ta2 = ta2 if type(ta2) == str else ta4.get()
            ta3 = ta3 if type(ta3) == str else ta4.get()
            ta4 = ta4 if type(ta4) == str else ta4.get()
            emc = emc if type(emc) == str else emc.get()
            efc = efc if type(efc) == str else efc.get()
            tests = (int(ta1) + int(ta2) + int(ta3) + int(ta4)) / 4
            mean['text'] = round((tests + int(emc) + int(efc)) / 3)
            return mean
        except ValueError:
            print('Por favor, inserte solo números.\nPlese, numbers only.')

    def first_course_gui(self):

        first_course_name = Label(self.root, text=self.first_course[0])
        first_course_name.grid(row=2, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.first_course[1] == '0':
            f_course_ta1 = Entry(self.root, width=2)
            f_course_ta1.insert(0, '00')
            f_course_ta1.grid(row=2, column=1)
        else:
            f_course_ta1 = self.first_course[1]
            f_course_ta1_ = Label(self.root, text=f_course_ta1)
            f_course_ta1_.grid(row=2, column=1)

        if self.first_course[2] == '0':
            f_course_ta2 = Entry(self.root, width=2)
            f_course_ta2.insert(0, '00')
            f_course_ta2.grid(row=2, column=2)
        else:
            f_course_ta2 = self.first_course[2]
            f_course_ta2_ = Label(self.root, text=f_course_ta2)
            f_course_ta2_.grid(row=2, column=2)

        if self.first_course[3] == '0':
            f_course_ta3 = Entry(self.root, width=2)
            f_course_ta3.insert(0, '00')
            f_course_ta3.grid(row=2, column=3)
        else:
            f_course_ta3 = self.fifth_course[3]
            f_course_ta3_ = Label(self.root, text=f_course_ta3)
            f_course_ta3_.grid(row=2, column=3)

        if self.first_course[4] == '0':
            f_course_ta4 = Entry(self.root, width=2)
            f_course_ta4.insert(0, '00')
            f_course_ta4.grid(row=2, column=4)
        else:
            f_course_ta4 = self.first_course[4]
            f_course_ta4_ = Label(self.root, text=f_course_ta4)
            f_course_ta4_.grid(row=2, column=4)

        if self.first_course[5] == '0':
            f_course_emc = Entry(self.root, width=2)
            f_course_emc.insert(0, '00')
            f_course_emc.grid(row=2, column=5)
        else:
            f_course_emc = self.first_course[5]
            f_course_emc_ = Label(self.root, text=f_course_emc)
            f_course_emc_.grid(row=2, column=5)

        if self.first_course[6] == '0':
            f_course_efc = Entry(self.root, width=2)
            f_course_efc.insert(0, '00')
            f_course_efc.grid(row=2, column=6)
        else:
            f_course_efc = self.first_course[6]
            f_course_efc_ = Label(self.root, text=f_course_efc)
            f_course_efc_.grid(row=2, column=6)

        first_course_mean = Label(self.root, text='00', font='bold')
        first_course_mean.grid(row=2, column=7)

        first_course_button = Button(self.root, text='Calcular',
                                     command=lambda: self.media_button(first_course_mean,
                                                                       f_course_ta1, f_course_ta2, f_course_ta3,
                                                                       f_course_ta4, f_course_emc, f_course_efc))
        first_course_button.grid(row=2, column=8)

    def second_course_gui(self):

        second_course_name = Label(self.root, text=self.second_course[0])
        second_course_name.grid(row=3, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.second_course[1] == '0':
            s_course_ta1 = Entry(self.root, width=2)
            s_course_ta1.insert(0, '00')
            s_course_ta1.grid(row=3, column=1)
        else:
            s_course_ta1 = self.second_course[1]
            s_course_ta1_ = Label(self.root, text=s_course_ta1)
            s_course_ta1_.grid(row=3, column=1)

        if self.second_course[2] == '0':
            s_course_ta2 = Entry(self.root, width=2)
            s_course_ta2.insert(0, '00')
            s_course_ta2.grid(row=3, column=2)
        else:
            s_course_ta2 = self.second_course[2]
            s_course_ta2_ = Label(self.root, text=s_course_ta2)
            s_course_ta2_.grid(row=3, column=2)

        if self.second_course[3] == '0':
            s_course_ta3 = Entry(self.root, width=2)
            s_course_ta3.insert(0, '00')
            s_course_ta3.grid(row=3, column=3)
        else:
            s_course_ta3 = self.second_course[3]
            s_course_ta3_ = Label(self.root, text=s_course_ta3)
            s_course_ta3_.grid(row=3, column=3)

        if self.second_course[4] == '0':
            s_course_ta4 = Entry(self.root, width=2)
            s_course_ta4.insert(0, '00')
            s_course_ta4.grid(row=3, column=4)
        else:
            s_course_ta4 = self.second_course[4]
            s_course_ta4_ = Label(self.root, text=s_course_ta4)
            s_course_ta4_.grid(row=3, column=4)

        if self.second_course[5] == '0':
            s_course_emc = Entry(self.root, width=2)
            s_course_emc.insert(0, '00')
            s_course_emc.grid(row=3, column=5)
        else:
            s_course_emc = self.second_course[5]
            s_course_emc_ = Label(self.root, text=s_course_emc)
            s_course_emc_.grid(row=3, column=5)

        if self.second_course[6] == '0':
            s_course_efc = Entry(self.root, width=2)
            s_course_efc.insert(0, '00')
            s_course_efc.grid(row=3, column=6)
        else:
            s_course_efc = self.second_course[6]
            s_course_efc_ = Label(self.root, text=s_course_efc)
            s_course_efc_.grid(row=3, column=6)

        second_course_mean = Label(self.root, text='00', font='bold')
        second_course_mean.grid(row=3, column=7)

        second_course_button = Button(self.root, text='Calcular',
                                      command=lambda: self.media_button(second_course_mean,
                                                                        s_course_ta1, s_course_ta2, s_course_ta3,
                                                                        s_course_ta4, s_course_emc, s_course_efc))
        second_course_button.grid(row=3, column=8)

    def third_course_gui(self):

        third_course_name = Label(self.root, text=self.third_course[0])
        third_course_name.grid(row=4, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.third_course[1] == '0':
            t_course_ta1 = Entry(self.root, width=2)
            t_course_ta1.insert(0, '00')
            t_course_ta1.grid(row=4, column=1)
        else:
            t_course_ta1 = self.third_course[1]
            t_course_ta1_ = Label(self.root, text=t_course_ta1)
            t_course_ta1_.grid(row=4, column=1)

        if self.third_course[2] == '0':
            t_course_ta2 = Entry(self.root, width=2)
            t_course_ta2.insert(0, '00')
            t_course_ta2.grid(row=4, column=2)
        else:
            t_course_ta2 = self.third_course[2]
            t_course_ta2_ = Label(self.root, text=t_course_ta2)
            t_course_ta2_.grid(row=4, column=2)

        if self.third_course[3] == '0':
            t_course_ta3 = Entry(self.root, width=2)
            t_course_ta3.insert(0, '00')
            t_course_ta3.grid(row=4, column=3)
        else:
            t_course_ta3 = self.third_course[3]
            t_course_ta3_ = Label(self.root, text=t_course_ta3)
            t_course_ta3_.grid(row=4, column=3)

        if self.third_course[4] == '0':
            t_course_ta4 = Entry(self.root, width=2)
            t_course_ta4.insert(0, '00')
            t_course_ta4.grid(row=4, column=4)
        else:
            t_course_ta4 = self.third_course[4]
            t_course_ta4_ = Label(self.root, text=t_course_ta4)
            t_course_ta4_.grid(row=4, column=4)

        if self.third_course[5] == '0':
            t_course_emc = Entry(self.root, width=2)
            t_course_emc.insert(0, '00')
            t_course_emc.grid(row=4, column=5)
        else:
            t_course_emc = self.third_course[5]
            t_course_emc_ = Label(self.root, text=t_course_emc)
            t_course_emc_.grid(row=4, column=5)

        if self.third_course[6] == '0':
            t_course_efc = Entry(self.root, width=2)
            t_course_efc.insert(0, '00')
            t_course_efc.grid(row=4, column=6)
        else:
            t_course_efc = self.third_course[6]
            t_course_efc_ = Label(self.root, text=t_course_efc)
            t_course_efc_.grid(row=4, column=6)

        third_course_mean = Label(self.root, text='00', font='bold')
        third_course_mean.grid(row=4, column=7)

        third_course_button = Button(self.root, text='Calcular',
                                     command=lambda: self.media_button(third_course_mean,
                                                                       t_course_ta1, t_course_ta2, t_course_ta3,
                                                                       t_course_ta4, t_course_emc, t_course_efc))
        third_course_button.grid(row=4, column=8)

    def fourth_course_gui(self):

        fourth_course_name = Label(self.root, text=self.fourth_course[0])
        fourth_course_name.grid(row=5, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.fourth_course[1] == '0':
            fth_course_ta1 = Entry(self.root, width=2)
            fth_course_ta1.insert(0, '00')
            fth_course_ta1.grid(row=5, column=1)
        else:
            fth_course_ta1 = self.fourth_course[1]
            fth_course_ta1_ = Label(self.root, text=fth_course_ta1)
            fth_course_ta1_.grid(row=5, column=1)

        if self.fourth_course[2] == '0':
            fth_course_ta2 = Entry(self.root, width=2)
            fth_course_ta2.insert(0, '00')
            fth_course_ta2.grid(row=5, column=2)
        else:
            fth_course_ta2 = self.fourth_course[2]
            fth_course_ta2_ = Label(self.root, text=fth_course_ta2)
            fth_course_ta2_.grid(row=5, column=2)

        if self.fourth_course[3] == '0':
            fth_course_ta3 = Entry(self.root, width=2)
            fth_course_ta3.insert(0, '00')
            fth_course_ta3.grid(row=5, column=3)
        else:
            fth_course_ta3 = self.fourth_course[3]
            fth_course_ta3_ = Label(self.root, text=fth_course_ta3)
            fth_course_ta3_.grid(row=5, column=3)

        if self.fourth_course[4] == '0':
            fth_course_ta4 = Entry(self.root, width=2)
            fth_course_ta4.insert(0, '00')
            fth_course_ta4.grid(row=5, column=4)
        else:
            fth_course_ta4 = self.fourth_course[4]
            fth_course_ta4_ = Label(self.root, text=fth_course_ta4)
            fth_course_ta4_.grid(row=5, column=4)

        if self.fourth_course[5] == '0':
            fth_course_emc = Entry(self.root, width=2)
            fth_course_emc.insert(0, '00')
            fth_course_emc.grid(row=5, column=5)
        else:
            fth_course_emc = self.fourth_course[5]
            fth_course_emc_ = Label(self.root, text=fth_course_emc)
            fth_course_emc_.grid(row=5, column=5)

        if self.fourth_course[6] == '0':
            fth_course_efc = Entry(self.root, width=2)
            fth_course_efc.insert(0, '00')
            fth_course_efc.grid(row=5, column=6)
        else:
            fth_course_efc = self.fourth_course[6]
            fth_course_efc_ = Label(self.root, text=fth_course_efc)
            fth_course_efc_.grid(row=5, column=6)

        fourth_course_media = Label(self.root, text='00', font='bold')
        fourth_course_media.grid(row=5, column=7)

        fourth_course_button = Button(self.root, text='Calcular',
                                      command=lambda: self.media_button(fourth_course_media,
                                                                        fth_course_ta1, fth_course_ta2, fth_course_ta3,
                                                                        fth_course_ta4, fth_course_emc, fth_course_efc))
        fourth_course_button.grid(row=5, column=8)

    def fifth_course_gui(self):

        fifth_course_name = Label(self.root, text=self.fifth_course[0])
        fifth_course_name.grid(row=6, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.fifth_course[1] == '0':
            fifth_course_ta1 = Entry(self.root, width=2)
            fifth_course_ta1.insert(0, '00')
            fifth_course_ta1.grid(row=6, column=1)
        else:
            fifth_course_ta1 = self.fifth_course[1]
            fifth_course_ta1_ = Label(self.root, text=fifth_course_ta1)
            fifth_course_ta1_.grid(row=6, column=1)

        if self.fifth_course[2] == '0':
            fifth_course_ta2 = Entry(self.root, width=2)
            fifth_course_ta2.insert(0, '00')
            fifth_course_ta2.grid(row=6, column=2)
        else:
            fifth_course_ta2 = self.fifth_course[2]
            fifth_course_ta2_ = Label(self.root, text=fifth_course_ta2)
            fifth_course_ta2_.grid(row=6, column=2)

        if self.fifth_course[3] == '0':
            fifth_course_ta3 = Entry(self.root, width=2)
            fifth_course_ta3.insert(0, '00')
            fifth_course_ta3.grid(row=6, column=3)
        else:
            fifth_course_ta3 = self.fifth_course[3]
            fifth_course_ta3_ = Label(self.root, text=fifth_course_ta3)
            fifth_course_ta3_.grid(row=6, column=3)

        if self.fifth_course[4] == '0':
            fifth_course_ta4 = Entry(self.root, width=2)
            fifth_course_ta4.insert(0, '00')
            fifth_course_ta4.grid(row=6, column=4)
        else:
            fifth_course_ta4 = self.fifth_course[4]
            fifth_course_ta4_ = Label(self.root, text=fifth_course_ta4)
            fifth_course_ta4_.grid(row=6, column=4)

        if self.fifth_course[5] == '0':
            fifth_course_emc = Entry(self.root, width=2)
            fifth_course_emc.insert(0, '00')
            fifth_course_emc.grid(row=6, column=5)
        else:
            fifth_course_emc = self.fifth_course[5]
            fifth_course_emc_ = Label(self.root, text=fifth_course_emc)
            fifth_course_emc_.grid(row=6, column=5)

        if self.fifth_course[6] == '0':
            fifth_course_efc = Entry(self.root, width=2)
            fifth_course_efc.insert(0, '00')
            fifth_course_efc.grid(row=6, column=6)
        else:
            fifth_course_efc = self.fifth_course[6]
            fifth_course_efc_ = Label(self.root, text=fifth_course_efc)
            fifth_course_efc_.grid(row=6, column=6)

        fifth_course_media = Label(self.root, text='00', font='bold')
        fifth_course_media.grid(row=6, column=7)

        fifth_course_button = Button(self.root, text='Calcular',
                                     command=lambda: self.media_button(fifth_course_media,
                                                                       fifth_course_ta1, fifth_course_ta2, fifth_course_ta3,
                                                                       fifth_course_ta4, fifth_course_emc, fifth_course_efc))
        fifth_course_button.grid(row=6, column=8)

    def sixth_course_gui(self):

        sixth_course_name = Label(self.root, text=self.sixth_course[0])
        sixth_course_name.grid(row=7, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.sixth_course[1] == '0':
            sixth_course_ta1 = Entry(self.root, width=2)
            sixth_course_ta1.insert(0, '00')
            sixth_course_ta1.grid(row=7, column=1)
        else:
            sixth_course_ta1 = self.sixth_course[1]
            sixth_course_ta1_ = Label(self.root, text=sixth_course_ta1)
            sixth_course_ta1_.grid(row=7, column=1)

        if self.sixth_course[2] == '0':
            sixth_course_ta2 = Entry(self.root, width=2)
            sixth_course_ta2.insert(0, '00')
            sixth_course_ta2.grid(row=7, column=2)
        else:
            sixth_course_ta2 = self.sixth_course[2]
            sixth_course_ta2_ = Label(self.root, text=sixth_course_ta2)
            sixth_course_ta2_.grid(row=7, column=2)

        if self.sixth_course[3] == '0':
            sixth_course_ta3 = Entry(self.root, width=2)
            sixth_course_ta3.insert(0, '00')
            sixth_course_ta3.grid(row=7, column=3)
        else:
            sixth_course_ta3 = self.sixth_course[3]
            sixth_course_ta3_ = Label(self.root, text=sixth_course_ta3)
            sixth_course_ta3_.grid(row=7, column=3)

        if self.sixth_course[4] == '0':
            sixth_course_ta4 = Entry(self.root, width=2)
            sixth_course_ta4.insert(0, '00')
            sixth_course_ta4.grid(row=7, column=4)
        else:
            sixth_course_ta4 = self.sixth_course[4]
            sixth_course_ta4_ = Label(self.root, text=sixth_course_ta4)
            sixth_course_ta4_.grid(row=7, column=4)

        if self.sixth_course[5] == '0':
            sixth_course_emc = Entry(self.root, width=2)
            sixth_course_emc.insert(0, '00')
            sixth_course_emc.grid(row=7, column=5)
        else:
            sixth_course_emc = self.sixth_course[5]
            sixth_course_emc_ = Label(self.root, text=sixth_course_emc)
            sixth_course_emc_.grid(row=7, column=5)

        if self.sixth_course[6] == '0':
            sixth_course_efc = Entry(self.root, width=2)
            sixth_course_efc.insert(0, '00')
            sixth_course_efc.grid(row=7, column=6)
        else:
            sixth_course_efc = self.sixth_course[6]
            sixth_course_efc_ = Label(self.root, text=sixth_course_efc)
            sixth_course_efc_.grid(row=7, column=6)

        sixth_course_media = Label(self.root, text='00', font='bold')
        sixth_course_media.grid(row=7, column=7)

        sixth_course_button = Button(self.root, text='Calcular',
                                     command=lambda: self.media_button(sixth_course_media,
                                                                       sixth_course_ta1, sixth_course_ta2, sixth_course_ta3,
                                                                       sixth_course_ta4, sixth_course_emc, sixth_course_efc))
        sixth_course_button.grid(row=7, column=8)

    def seventh_course_gui(self):

        seventh_course_name = Label(self.root, text=self.seventh_course[0])
        seventh_course_name.grid(row=8, column=0)
        # getting the "TA1, TA2, TA3, TA4, EMC, EFC" grades
        if self.seventh_course[1] == '0':
            seventh_course_ta1 = Entry(self.root, width=2)
            seventh_course_ta1.insert(0, '00')
            seventh_course_ta1.grid(row=8, column=1)
        else:
            seventh_course_ta1 = self.seventh_course[1]
            seventh_course_ta1_ = Label(self.root, text=seventh_course_ta1)
            seventh_course_ta1_.grid(row=8, column=1)

        if self.seventh_course[2] == '0':
            seventh_course_ta2 = Entry(self.root, width=2)
            seventh_course_ta2.insert(0, '00')
            seventh_course_ta2.grid(row=8, column=2)
        else:
            seventh_course_ta2 = self.seventh_course[2]
            seventh_course_ta2_ = Label(self.root, text=seventh_course_ta2)
            seventh_course_ta2_.grid(row=8, column=2)

        if self.seventh_course[3] == '0':
            seventh_course_ta3 = Entry(self.root, width=2)
            seventh_course_ta3.insert(0, '00')
            seventh_course_ta3.grid(row=8, column=3)
        else:
            seventh_course_ta3 = self.seventh_course[3]
            seventh_course_ta3_ = Label(self.root, text=seventh_course_ta3)
            seventh_course_ta3_.grid(row=8, column=3)

        if self.seventh_course[4] == '0':
            seventh_course_ta4 = Entry(self.root, width=2)
            seventh_course_ta4.insert(0, '00')
            seventh_course_ta4.grid(row=8, column=4)
        else:
            seventh_course_ta4 = self.seventh_course[4]
            seventh_course_ta4_ = Label(self.root, text=seventh_course_ta4)
            seventh_course_ta4_.grid(row=8, column=4)

        if self.seventh_course[5] == '0':
            seventh_course_emc = Entry(self.root, width=2)
            seventh_course_emc.insert(0, '00')
            seventh_course_emc.grid(row=8, column=5)
        else:
            seventh_course_emc = self.seventh_course[5]
            seventh_course_emc_ = Label(self.root, text=seventh_course_emc)
            seventh_course_emc_.grid(row=8, column=5)

        if self.seventh_course[6] == '0':
            seventh_course_efc = Entry(self.root, width=2)
            seventh_course_efc.insert(0, '00')
            seventh_course_efc.grid(row=8, column=6)
        else:
            seventh_course_efc = self.seventh_course[6]
            seventh_course_efc_ = Label(self.root, text=seventh_course_efc)
            seventh_course_efc_.grid(row=8, column=6)

        seventh_course_media = Label(self.root, text='00', font='bold')
        seventh_course_media.grid(row=8, column=7)

        seventh_course_button = Button(self.root, text='Calcular',
                                     command=lambda: self.media_button(seventh_course_media,
                                                                       seventh_course_ta1, seventh_course_ta2, seventh_course_ta3,
                                                                       seventh_course_ta4, seventh_course_emc, seventh_course_efc))
        seventh_course_button.grid(row=8, column=8)

    def main(self):
        self.first_course_gui()
        self.second_course_gui()
        self.third_course_gui()
        self.fourth_course_gui()
        self.fifth_course_gui()
        self.sixth_course_gui()
        self.seventh_course_gui()
