from abc import ABC, abstractmethod


class ActionsWithVacancies(ABC):
    """
    Абстрактный Класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла
    по критериям и удаления информации о вакансиях
    """
    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def get_info_according_to_criteria(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
