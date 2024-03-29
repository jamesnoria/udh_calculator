# made by: James Noria
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class UdhAutomatization:

    def __init__(self, student_id, student_password, student_dni):

        # open chrome and udh website
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.get('http://www.udh.edu.pe/websauh/alogin.aspx')

        # Student Login
        self.student_id = student_id
        stud_user = self.driver.find_element(By.XPATH, '//*[@id="txtusuario"]')
        stud_user.send_keys(self.student_id)
        stud_user.send_keys(Keys.ENTER)

        self.student_dni = student_dni
        stud_dni = self.driver.find_element(By.XPATH, '//*[@id="txtDNI"]')
        stud_dni.send_keys(self.student_dni)

        self.student_password = student_password
        stud_password = self.driver.find_element(
            By.XPATH, '//*[@id="txtclave"]')
        stud_password.send_keys(self.student_password)

        web_captcha = self.driver.find_element(
            By.XPATH, '//*[@id="txtCaptcha"]')
        captcha_input = input('¿Cual es el código que aparece?: ')
        web_captcha.send_keys(captcha_input)
        web_captcha.send_keys(Keys.ENTER)

        # Access to 'notas parciales'
        student_grades = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_Menu1"]/ul/li[23]/a')
        student_grades.send_keys(Keys.ENTER)

        # self.driver.close()

    def first_course(self):
        # Access to the first course and every grade in it
        try:
            f_course_grades = []
            first_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl02_Label2"]').text
            f_course_grades.append(first_course_name)
            f_course_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[4]').text
            f_course_grades.append(f_course_ta1)
            f_course_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[5]').text
            f_course_grades.append(f_course_ta2)
            f_course_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[6]').text
            f_course_grades.append(f_course_ta3)
            f_course_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[7]').text
            f_course_grades.append(f_course_ta4)
            f_course_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[8]').text
            f_course_grades.append(f_course_ta5)
            f_course_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[10]').text
            f_course_grades.append(f_course_emc)
            f_course_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[2]/td[11]').text
            f_course_grades.append(f_course_efc)

            # return a list with the name and all grades
            return f_course_grades
        except:
            f_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return f_course_grades

    def second_course(self):
        # Access to the second course and every grade in it
        try:
            s_course_grades = []
            second_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl03_Label2"]').text
            s_course_grades.append(second_course_name)
            s_course_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[4]').text
            s_course_grades.append(s_course_ta1)
            s_course_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[5]').text
            s_course_grades.append(s_course_ta2)
            s_course_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[6]').text
            s_course_grades.append(s_course_ta3)
            s_course_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[7]').text
            s_course_grades.append(s_course_ta4)
            s_course_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[8]').text
            s_course_grades.append(s_course_ta5)
            s_course_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[10]').text
            s_course_grades.append(s_course_emc)
            s_course_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[3]/td[11]').text
            s_course_grades.append(s_course_efc)

            # return a list with the name and all grades
            return s_course_grades
        except:
            s_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return s_course_grades

    def third_course(self):
        # Access to the third course and every grade in it
        try:
            t_course_grades = []
            third_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl04_Label2"]').text
            t_course_grades.append(third_course_name)
            t_course_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[4]').text
            t_course_grades.append(t_course_ta1)
            t_course_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[5]').text
            t_course_grades.append(t_course_ta2)
            t_course_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[6]').text
            t_course_grades.append(t_course_ta3)
            t_course_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[7]').text
            t_course_grades.append(t_course_ta4)
            t_course_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[8]').text
            t_course_grades.append(t_course_ta5)
            t_course_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[10]').text
            t_course_grades.append(t_course_emc)
            t_course_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[4]/td[11]').text
            t_course_grades.append(t_course_efc)

            # return a list with the name and all grades
            return t_course_grades
        except:
            t_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return t_course_grades

    def fourth_course(self):
        # Access to the fourth course and every grade in it
        try:
            fth_course_grades = []
            fourth_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl05_Label2"]').text
            fth_course_grades.append(fourth_course_name)
            fth_score_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[4]').text
            fth_course_grades.append(fth_score_ta1)
            fth_score_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[5]').text
            fth_course_grades.append(fth_score_ta2)
            fth_score_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[6]').text
            fth_course_grades.append(fth_score_ta3)
            fth_score_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[7]').text
            fth_course_grades.append(fth_score_ta4)
            fth_score_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[8]').text
            fth_course_grades.append(fth_score_ta5)
            fth_score_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[10]').text
            fth_course_grades.append(fth_score_emc)
            fth_score_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[5]/td[11]').text
            fth_course_grades.append(fth_score_efc)

            # return a list with the name and all grades
            return fth_course_grades
        except:
            fth_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return fth_course_grades

    def fifth_course(self):
        # Access to the fifth course and every grade in it
        try:
            fifth_course_grades = []
            fifth_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl06_Label2"]').text
            fifth_course_grades.append(fifth_course_name)
            fifth_score_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[4]').text
            fifth_course_grades.append(fifth_score_ta1)
            fifth_score_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[5]').text
            fifth_course_grades.append(fifth_score_ta2)
            fifth_score_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[6]').text
            fifth_course_grades.append(fifth_score_ta3)
            fifth_score_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[7]').text
            fifth_course_grades.append(fifth_score_ta4)
            fifth_score_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[8]').text
            fifth_course_grades.append(fifth_score_ta5)
            fifth_score_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[10]').text
            fifth_course_grades.append(fifth_score_emc)
            fifth_score_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[6]/td[11]').text
            fifth_course_grades.append(fifth_score_efc)

            # return a list with the name and all grades
            return fifth_course_grades
        except:
            fifth_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return fifth_course_grades

    def sixth_course(self):
        # Access to the sixth course and every grade in it
        try:
            sixth_course_grades = []
            sixth_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl07_Label2"]').text
            sixth_course_grades.append(sixth_course_name)
            sixth_score_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[4]').text
            sixth_course_grades.append(sixth_score_ta1)
            sixth_score_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[5]').text
            sixth_course_grades.append(sixth_score_ta2)
            sixth_score_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[6]').text
            sixth_course_grades.append(sixth_score_ta3)
            sixth_score_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[7]').text
            sixth_course_grades.append(sixth_score_ta4)
            sixth_score_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[8]').text
            sixth_course_grades.append(sixth_score_ta5)
            sixth_score_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[10]').text
            sixth_course_grades.append(sixth_score_emc)
            sixth_score_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[7]/td[11]').text
            sixth_course_grades.append(sixth_score_efc)

            # return a list with the name and all grades
            return sixth_course_grades
        except:
            sixth_course_grades = ['Curso vacio', '0', '0', '0', '0', '0', '0', '0']
            return sixth_course_grades

    def seventh_course(self):
        # Access to the seventh course and every grade in it
        try:
            seventh_course_grades = []
            seventh_course_name = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1_ctl08_Label2"]').text
            seventh_course_grades.append(seventh_course_name)
            seventh_score_ta1 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[4]').text
            seventh_course_grades.append(seventh_score_ta1)
            seventh_score_ta2 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[5]').text
            seventh_course_grades.append(seventh_score_ta2)
            seventh_score_ta3 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[6]').text
            seventh_course_grades.append(seventh_score_ta3)
            seventh_score_ta4 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[7]').text
            seventh_course_grades.append(seventh_score_ta4)
            seventh_score_ta5 = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[8]').text
            seventh_course_grades.append(seventh_score_ta5)
            seventh_score_emc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[10]').text
            seventh_course_grades.append(seventh_score_emc)
            seventh_score_efc = self.driver.find_element(
                By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody/tr[8]/td[11]').text
            seventh_course_grades.append(seventh_score_efc)

            # closing chrome after get info
            self.driver.close()

            # return a list with the name and all grades
            return seventh_course_grades
        except:
            seventh_course_grades = [
                'Curso vacio', '0', '0', '0', '0', '0', '0', '0']

            # closing chrome after get info
            self.driver.close()

            return seventh_course_grades
