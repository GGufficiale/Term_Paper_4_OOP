from src.class_ABS_API import HeadHunter
from src.class_Vacancies import Vacancy
from src.class_ABS_actions_with_Vacancies_and_JSON_class import JsonSaver
import json

hh = HeadHunter()
vacancies = hh.get_filter_vacancies("python")
# vacancies_cls_example = []
# for i in vacancies:
#     """Распаковка значений словаря для создания экземпляров класса - перемещено в файл с json классом"""
#     vacancies_cls_example.append(Vacancy(**i))
# print(vacancies_cls_example)

# for i in vacancies_cls_example:
#     """Вывод на печать всех значений словаря с разделителем"""
#     print(i)
#     print("*" * 20)

# sorted_vacancies = sorted(vacancies_cls_example)
# for i in sorted_vacancies:
#     """Цикл для вывода отсортированных вакансий по одной"""
#     print(i)
#     print("*" * 20)

# json_saver = JsonSaver()
# json_saver.write_data(vacancies)
# data = json_saver.get_vacancies()
# """Цикл для проверки вывода вакансий из json файла"""
# for i in data:
#     print(i)
#     print("*" * 20)


def get_value(dictionary, *keys):
    """
    Возвращает значение из словаря по заданному пути ключей
    :param dictionary: словарь, из которого мы получаем значение
    :param keys: к-во ключей в виде строки, определяющих путь к значению.
    :return: значение из словаря, связанное с заданным путем ключей.
     Если хотя бы один ключ не существует или путь прерывается значениями None, будет возвращено None.
    """
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary


def user_interaction():
    print("Привет! Я - поиск вакансий на HН.ru. Чтобы все было хорошо, к-во вакансий пишите цифрами. "
          "Ключевые слова разделяйте пробелами")
    vacancy_name = input('Введите название вакансии: ')
    keyword_vacancy = input('Введите ключевые слова для фильтрации вакансий: ').split()

    try:
        top_n = int(input('Введите к-во вакансий для отображения по убыванию зарплаты: '))
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print('Получено некорректное значение. Будут выданы все результаты:')
        top_n = None

    vacancy_hh = HeadHunter()
    all_vacancy = vacancy_hh.get_vacancies(vacancy_name)

    if len(all_vacancy) == 0:
        print("По вашему запросу вакансий не найдено")
    else:
        print(f"Всего к-во вакансий по запросу '{vacancy_name}': {len(all_vacancy)}")
        print(f"Топ {top_n or len(all_vacancy)} вакансий по зарплате:")

        good_vacancy = []

        if not keyword_vacancy:
            top_n_vacancy = top_n or len(all_vacancy)
            for vacancy in all_vacancy[:top_n_vacancy]:
                try:
                    name = get_value(vacancy, 'name')
                    url = get_value(vacancy, 'url')
                    salary = get_value(vacancy, 'salary')
                    employer = get_value(vacancy, 'employer')
                    good_vacancy.append(Vacancy(name, url, salary, employer))
                except Exception as e:
                    print(f"Ошибка обработки вакансии: {e}")
        else:
            for vacancy in all_vacancy:
                try:
                    name = get_value(vacancy, 'name')
                    url = get_value(vacancy, 'url')
                    salary = get_value(vacancy, 'salary', 'from')
                    employer = get_value(vacancy, 'employer')
                    if any(keyword.lower() in str(vacancy).lower() for keyword in keyword_vacancy):
                        good_vacancy.append(Vacancy(name, url, salary, employer))
                except Exception as e:
                    print(f"Ошибка обработки вакансии: {e}")

        if len(good_vacancy) == 0:
            top_n_vacancy = top_n or len(all_vacancy)
            print(f"Ключевые слова не найдены. Будут выданы все результаты: {top_n_vacancy} вакансий.")
            good_vacancy = all_vacancy[:top_n_vacancy]
        else:
            top_vacancy = sorted(good_vacancy, key=lambda x: x.salary_to if x.salary_to is not None else 0,
                                 reverse=True)
            good_vacancy = top_vacancy[:top_n]

        for vacancy in good_vacancy:
            print(vacancy)

    with open('vacancies.json', 'w') as file:
        json.dump(good_vacancy, file, default=lambda x: x.__dict__)
        # записывает в файл vacancies.json выбранные пользователем вакансии


if __name__ == "__main__":
    user_interaction()
