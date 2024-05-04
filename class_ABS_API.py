from abc import ABC, abstractmethod


class AbstractApiService(ABC):
    @abstractmethod
    def __init__(self, file_worker):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
