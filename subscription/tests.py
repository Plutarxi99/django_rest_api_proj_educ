from django.urls import reverse
from rest_framework.test import APITestCase

from education.models import Course, Lesson
from subscription.models import Subscription
from users.models import User


class SubsTestCase(APITestCase):
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
        self.subs = Subscription(user=self.user)
        self.subs.save()
        self.subs.course.add(self.course)
        # self.subs = Subscription.objects.create(
        #     user=self.user,
        #     course=None
        # )

    def test_subs_create(self):
        """ Тестирование создание подписки на курс """
        self.subs.course.add(self.course)  # добавление курса в подписку
        response = self.client.get(
            '/education/course/1/',
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )
        self.assertEquals(
            response.json(),
            {'id': 1, 'lessons': [], 'is_subs': 'Подписан', 'name': 'test', 'picture': None, 'description': None,
             'owner': 1}
        )

    def test_subs_update(self):
        """ Тестирование изменение подписки на курс """
        self.subs.course.add(self.course)

        course_t = Course.objects.create(
            name='test_course',
            owner=self.user
        )
        self.subs.course.add(course_t)  # добавление курса в подписку
        data = {
            'user': 1,
            "course": [1]
        }

        response = self.client.patch(
            '/subscription/update/1/',
            data=data,
            headers={'Authorization': 'Bearer {}'.format(self.token)}
        )
        self.assertEquals(
            response.json(),
            {'id': 1, 'user': 1, 'course': [1]}
        )
