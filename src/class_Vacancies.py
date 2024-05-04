class Vacancy:
    def __init__(self, name, url, salary, skills):
        self.name = name
        self.url = url
        self.salary = salary
        self.skills = skills

    def better_salary(self, other):
        """
        Метод сравнения вакансий между собой по зарплате
        """
        if self.salary > other.salary:
            print('Первая зп круче')
        elif self.salary < other.salary:
            print('Вторая зп круче')
        else:
            print('Обе зп хороши')

    def salary_exists(self):
        """
        Метод валидации данных: проверка, указана зарплата или нет
        """
        if self.salary != int:
            self.salary = 0
