from abc import ABC, abstractmethod
from src.class_Vacancies import Vacancy
import json


class ActionsWithVacancies(ABC):
    """
    Абстрактный Класс, который обязывает реализовывать методы для добавления вакансий в файл,
    получения данных из файла по критериям и удаления информации о вакансиях
    """

    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self, name):
        pass


class JsonSaver(ActionsWithVacancies):
    """Класс для работы с JSON файлом и сохранением инфо в него"""
    def __init__(self, filename="vacancies.json"):
        """Метод для автоматического создания и наименования JSON файла"""
        self.filename = f"data/{filename}"

    def write_data(self, vacancies):
        """Метод для записи инфо в JSON файл"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list[Vacancy]:
        """Метод получения вакансий из json файла"""
        with open(self.filename, encoding="utf-8") as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            """Распаковка значений словаря для создания экземпляров класса"""
            vacancies.append(Vacancy(**vacancy))
            # Можно было бы записать vacancies.append(Vacancy(name=vacancy["name"]) итд.)
        return vacancies

    def delete_vacancy(self, name) -> list[Vacancy]:
        """Метод удаления вакансий из json файла"""
        with open(self.filename, encoding="utf-8") as f:
            data = json.load(f)
            data.remove(name)
        return data
