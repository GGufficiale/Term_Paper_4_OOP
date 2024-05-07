class Vacancy:
    """Класс для работы с вакансией"""
    def __init__(self, name: str, url: str, salary: dict | None, employer: str):
        self.name = name
        self.url = url
        self.__validate_salary(salary)
        self.employer = employer

    def __validate_salary(self, salary):
        """Приватный метод валидации, потому что он будет нужен только здесь
        Проверка на наличие зарплаты (None или не None)"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else "∞"

    def __str__(self):
        return f"""Имя: {self.name}
Зарплата от {self.salary_from} до {self.salary_to}
url: {self.url}
Название компании: {self.employer}"""

    def __lt__(self, other):
        """<"""
        # """Метод, чтобы сортировка работала в обе стороны - от и до"""
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)
