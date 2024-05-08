class Vacancy:
    """Класс для работы с вакансией"""
    def __init__(self, name: str, url: str, salary: dict | None, employer: str):
        self.name = name
        self.url = url
        self.__validate_salary(salary)
        self.employer = employer

    def __validate_salary(self, salary):
        """Метод валидации - проверка на наличие зарплаты (None или не None).
        Он приватный, потому что будет нужен только здесь"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else "∞"

    def __str__(self):
        """Метод для вывода инфо о вакансии в нужном нам формате"""
        return f"""Имя: {self.name}
Зарплата от {self.salary_from} до {self.salary_to}
url: {self.url}
Название компании: {self.employer}"""

    def __lt__(self, other):
        """<"""
        # """Метод для работы сортировки в обе стороны - "от" и "до""""
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)
