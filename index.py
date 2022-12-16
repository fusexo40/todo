import sys
import sqlite3
from PyQt5 import uic, QtWidgets  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox
from work_with_db import db


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Загружаем дизайн
        self.setFixedSize(495, 477) # Фиксируем размер окна
        self.database = db() # Создаём экземпляр класса db
        self.setWindowTitle("to do")

        self.add_task.clicked.connect(self.addtask)
        self.clear_all.clicked.connect(self.clearalltasks)
        # Подключаем кнопки
        for task in self.database.get_task_list():
            self.verticalLayout.addWidget(QtWidgets.QCheckBox(task))
        # Загружаем задачи из базы данных (сделанно чтбы если ты закрыл приложение твои задачи сохранились)
        


    def addtask(self): # Кнопка добавления задачи
        text_of_task = self.task_name.toPlainText()
        if text_of_task != "" and text_of_task not in self.database.get_task_list(): # Проверка написанна ли задачи и нет ли её в списке задач
            self.verticalLayout.addWidget(QtWidgets.QCheckBox(text_of_task)) # Добавление задачи в приложение
            self.database.add_task(text_of_task) # Добавление задачи в базу данных
            self.task_name.setText("")


    def clearalltasks(self): # очистка всех задач
        self.database.delete_all_tasks()
        for i in reversed(range(self.verticalLayout.count())): # Очистка базы данных
            self.verticalLayout.itemAt(i).widget().deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())