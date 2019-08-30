from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@sajeesh.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test1@myhotel.com',
            password='password123',
            first_name='Sajeesh',
            last_name='Namboo',
        )

    def test_users_listed(self):
        """ Test that users are listing on user page"""
        url = reverse('admin:recipe_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Testing the user edit page works"""
        url = reverse('admin:recipe_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Testing the create user page works"""
        url = reverse('admin:recipe_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
