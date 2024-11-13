import random


def generate_login():
    first_name = 'karina'
    last_name = 'mihalevskaia'
    cohort_number = 14
    random_digits = random.randint(100, 999)
    domain = 'yandex.ru'
    return f'{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}'
