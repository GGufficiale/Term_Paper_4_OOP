import json


class JsonSaver:
    """
    Класс для сохранения инфо о вакансиях в JSON-файл
    """
    def load_data_from_file(self):
        """Загрузка данных из файла .json"""
        with open("products.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        for product in data:
            products_list = []
            for p in product['products']:
                products_list.append(p)
            return products_list

    def make_products_list(self):
        """Загрузка данных из файла .json"""
        with open("products.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        for product in data:
            products_list = []
            for p in product['products']:
                products_list.append(p)
