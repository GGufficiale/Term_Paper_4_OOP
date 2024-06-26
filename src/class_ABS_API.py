from abc import ABC, abstractmethod
import requests


class AbstractApiService(ABC):
    """Абстрактный класс для работы с НН API"""
    @abstractmethod
    def get_response(self, text, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass

    @abstractmethod
    def get_filter_vacancies(self, text, per_page):
        pass


class HeadHunter(AbstractApiService):
    """Класс для работы с НН API"""

    def __init__(self):
        """Определение API-ссылки, с которой будет вестись работа"""
        self.__url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int = 20):
        """Запрос на НН API"""
        params = {"text": text, "per_page": per_page}
        # Если нужно, чтобы вакансия искалась сразу в описании, то:
        # params = {"text": f"NAME: {text}", "per_page": per_page}
        response = requests.get(self.__url, params=params)
        return response

    def get_vacancies(self, text: str, per_page: int = 20) -> list:
        """Получение вакансий в формате json"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies

    def get_filter_vacancies(self, text: str, per_page: int = 20) -> list:
        """Метод фильтрации значений (вакансий) из массы с НН по выбранным нами параметрам"""
        filter_vacancies = []
        vacancies = self.get_vacancies(text, per_page)
        for vacancy in vacancies:
            filter_vacancies.append({
                "name": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["name"]
            })
        return filter_vacancies


# hh = HeadHunter()
# """Проверка вывода отфильтрованных вакансий"""
# print(hh.get_filter_vacancies("python"))

# hh = HeadHunter()
# """Проверка вывода зп, чтоб понять ее формат"""
# data = hh.get_filter_vacancies("python")
# for i in data:
#     print(i["salary"])
