import re

from rest_framework.exceptions import ValidationError


class LinkInVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """
        Метод класс для его вызова
        Валидирует, чтобы ссылка вела только на внешний ресурс с доменом youtube.com
        """
        pattern = 'https://www.youtube.com/'
        tmp_val = dict(value).get(self.field)  # получение заполняемой строки
        reg = re.match(pattern, tmp_val)  # если ссылка начинается с pattern, то возвращает значение

        if not bool(reg):
            raise ValidationError(f'Ссылка ведет на внешний ресурс начинающийся не с {pattern}')
