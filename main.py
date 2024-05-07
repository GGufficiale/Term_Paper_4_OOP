from src.class_ABS_API import HeadHunter
from src.class_Vacancies import Vacancy
from src.class_ABS_actions_with_Vacancies_and_JSON_class import JsonSaver

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

js = JsonSaver()
js.write_data(vacancies)
data = js.get_vacancies()
for i in data:
    print(i)
    print("*" * 20)
