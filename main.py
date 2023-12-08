import json


class Entity:
    def __init__(self, name_entity):
        self.name_entity = name_entity

    def __repr__(self):
        return f"Сущность: {self.name_entity}"

    def load_data(self):
        """ Загрузка данных с файла data.json """
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return []

    def add_entity(self):
        """ Добавление данных в файл data.json """
        data_json = self.load_data()
        data_json.append({"name_entity": self.name_entity})
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data_json, file)


class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __repr__(self):
        return f"{self.name} работает в {self.job}"

    def load_data(self):
        """ Загрузка данных с файла data.json """
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return []

    def add_employee(self):
        """ Добавление данных в файл data.json """
        data_json = self.load_data()
        data_json.append({"name": self.name, "job": self.job})
        with open("data.json", "w") as file:
            json.dump(data_json, file)


if __name__ == '__main__':
    cat = Entity('Сугроб')
    print(cat)
    cat.add_entity()

    employee = Employee('Петя', 'Foxford')
    print(employee)
    employee.add_employee()

