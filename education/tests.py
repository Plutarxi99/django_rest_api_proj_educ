from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    password = 'testpassword'
    email = 'test@test.test'

    def setUp(self):
        user, created = User.objects.get_or_create(
            email=self.email,
            is_active=True,
        )
        if created or not user.check_password(self.password):
            user.set_password(self.password)
            user.save()

        self.user = User.objects.get(pk=1)

        data = {
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(
            reverse('users:token_obtain_pair'),
            data=data
        )
        self.token = response.json()['access']

        self.course = Course.objects.create(
            name='test',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='test',
            course=self.course,
            link_to_video='https://www.youtube.com/'
        )

    def test_lesson_create(self):
        """ Тестирование создание урков"""
        data = {
            'name': 'test2',
            'course': self.course.id,
            'link_to_video': 'https://www.youtube.com/'
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data,
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'name': 'test2', 'description': None, 'picture': None,
             'link_to_video': 'https://www.youtube.com/', 'course': 1}
        )

    def test_lesson_list(self):
        """ Тестирование списка уроков"""

        response = self.client.get(
            reverse('education:lesson_list'),
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 1, 'course': 'test', 'name': 'test', 'description': None, 'picture': None,
                 'link_to_video': 'https://www.youtube.com/'}]}
        )

    def test_lesson_update(self):
        """ Тестирование обновление урока"""
        data = {
            'name': 'test_update',
            'course': self.course.id,
            'link_to_video': 'https://www.youtube.com/'
        }

        # response = self.client.post(
        #     reverse('blog:article_update', args=[self.article.pk]),
        #     data
        # )

        response = self.client.patch(
            '/education/lesson/update/1/',
            data=data,
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'id': 1, 'name': 'test_update', 'description': None, 'picture': None,
             'link_to_video': 'https://www.youtube.com/', 'course': 1}
        )

    def test_lesson_validator_url(self):
        """ Тестирование валидации на ссылку видео урока """
        data = {
            'name': 'test',
            'course': self.course.id,
            'link_to_video': 'https://www.skypro.com/'
        }

        response = self.client.patch(
            '/education/lesson/update/1/',
            data=data,
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEquals(
            response.json(),
            {'non_field_errors': ['Ссылка ведет на внешний ресурс начинающийся не с https://www.youtube.com/']}
        )

    def test_lesson_detail(self):
        """ Тестирование на получение одного урока"""

        response = self.client.get(
            '/education/lesson/1/',
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )
        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'name': 'test', 'description': None, 'picture': None, 'link_to_video': 'https://www.youtube.com/',
             'course': 1}
        )

    def test_lesson_delete(self):
        """ Тестирование удаление урока"""
        response = self.client.delete(
            '/education/lesson/delete/1/',
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

