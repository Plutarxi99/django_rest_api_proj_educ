from django.core.management import BaseCommand

from education.models import *
from django.db import connection


class Command(BaseCommand):
    help = 'Заполнение базы данных'

    def handle(self, *args, **options):

        list_table = [
            'public.education_payment',
            'public.education_lesson',
            'public.education_course',
        ]
        # Подключается к базе данных и обнуляет автоинкремент и удаляет наполнение таблиц
        with connection.cursor() as cursor:
            for list_table_item in list_table:
                cursor.execute(f'DELETE FROM {list_table_item};')
                cursor.execute(f'TRUNCATE TABLE {list_table_item} RESTART IDENTITY CASCADE;')

        # Добавляет данные в таблицу catalog_product
        course_list = [
            {'name': 'Химия.Анаболики', 'picture': '', 'description': 'Для качков, чтобы быстро накачаться'},
            {'name': 'Компьютер', 'picture': '', 'description': 'Узнаешь, все комплектующие'},
            {'name': 'Мышцы', 'picture': '', 'description': 'Узнаешь, все мышцы в теле человека'},
        ]
        course_for_create = []
        for product_item in course_list:
            course_for_create.append(
                Course(**product_item)
            )

        Course.objects.bulk_create(course_for_create)
        # Добавляет данные в таблицу catalog_category
        lesson_list = [
            {'name': 'Креатин', 'description': 'Добавка для самочувствия', 'course': 1},
            {'name': 'Протеин', 'description': 'Добавка для роста мышц', 'course': 1},
            {'name': 'Витамины', 'description': 'Добавка для самочувствия', 'course': 1},
            {'name': 'Видеокарта', 'description': 'Выводит изображение', 'course': 2},
            {'name': 'Процессор', 'description': 'Высчитывает операции', 'course': 2},
            {'name': 'Маттеринская плата', 'description': 'Питает все элементы компьютера', 'course': 2},
            {'name': 'Бицепс', 'description': 'Должен быть большой', 'course': 3},
            {'name': 'Трицепс', 'description': 'Должен быть очень большой', 'course': 3},
            {'name': 'Трапеция', 'description': 'Должная быть волна за шеей', 'course': 3},
            {'name': 'Пресс', 'description': 'все 100 кубиков', 'course': 3},
        ]
        lesson_for_create = []
        for category_item in lesson_list:
            lesson_for_create.append(
                Lesson(**category_item)
            )
        Lesson.objects.bulk_create(lesson_for_create)

        # Добавляет данные в таблицу catalog_product
        payment_list = [
            {'user': 2, 'date': '2023-11-21T01:06:19.372Z', 'course': 3, 'lesson': 4, 'sum_of_pay': 15000,
             'way_of_pay': 'translation'},
            {'user': 2, 'date': '2023-11-22T01:06:19.372Z', 'course': None, 'lesson': 6, 'sum_of_pay': 8000,
             'way_of_pay': 'card'},
            {'user': 4, 'date': '2023-11-22T01:36:19.372Z', 'course': 3, 'lesson': None, 'sum_of_pay': 14000,
             'way_of_pay': 'translation'},
            {'user': 4, 'date': '2023-11-19T01:06:19.372Z', 'course': 3, 'lesson': 2, 'sum_of_pay': 12000,
             'way_of_pay': 'card'},
            {'user': 2, 'date': '2023-11-19T01:00:19.372Z', 'course': 2, 'lesson': 7, 'sum_of_pay': 50000,
             'way_of_pay': 'translation'},
            {'user': 5, 'date': '2023-11-24T01:06:19.372Z', 'course': None, 'lesson': 4, 'sum_of_pay': 2000,
             'way_of_pay': 'card'},
            {'user': 2, 'date': '2023-11-25T01:06:19.372Z', 'course': None, 'lesson': 8, 'sum_of_pay': 15000,
             'way_of_pay': 'translation'},
            {'user': 5, 'date': '2023-11-26T01:06:19.372Z', 'course': 2, 'lesson': None, 'sum_of_pay': 5000,
             'way_of_pay': 'card'},
        ]
        payment_for_create = []
        for payment_item in payment_list:
            payment_for_create.append(
                Payment(**payment_item)
            )
        Payment.objects.bulk_create(payment_for_create)
