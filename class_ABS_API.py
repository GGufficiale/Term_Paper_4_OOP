from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
