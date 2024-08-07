import random


class Help:
    @staticmethod
    def generate_email():
        return f"KamilPracticum{random.randint(100, 999)}@yandex.ru"