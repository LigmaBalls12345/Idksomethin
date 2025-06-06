from core import *

student = MyStat("login","password") # Пример создания объекта учебного аккаунта
student.get_marks() # Отправляет запрос на сайт mystat, после чего присылает оценки
student.get_dates("2001-09-11") # Присылает расписание на указанный месяц
student.get_average_mark() # Возвращает среднюю оценку ученика
