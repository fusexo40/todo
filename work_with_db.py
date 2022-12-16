import sqlite3

class db():

    def __init__(self) -> None:
        self.datab = sqlite3.connect('server.db') # Присоединение к базе данных
        self.sql = self.datab.cursor() # Создание курсора
        self.sql.execute("""CREATE TABLE IF NOT EXISTS tasks (task TEXT)""") # Создание таблици(если её нет)
        self.datab.commit()
        for value in self.sql.execute("SELECT * FROM tasks"): # Логи
            print(value[0])


    def delete_all_tasks(self) -> None: 
        self.datab.execute("DELETE FROM tasks") # Очистка всей таблици
        self.datab.commit()
        for value in self.sql.execute("SELECT * FROM tasks"): # Логи
            print(value[0])


    def add_task(self, task) -> None:
        self.sql.execute(f"INSERT INTO tasks VALUES ('{task}')") # Добавление задачии
        self.datab.commit()
        for value in self.sql.execute("SELECT * FROM tasks"): # Логи
            print(value[0])

    
    def get_task_list(self) -> list:
        answer = []
        for value in self.sql.execute("SELECT * FROM tasks"): # Возврат всех задач
            answer.append(value[0])
        return answer