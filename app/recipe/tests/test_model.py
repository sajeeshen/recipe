from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def test_create_user_with_email(self):
        """ Testing the API can create a new user with email"""
        email = "sajeeshe@gmail.com"
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test creating with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            'sajeesh@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)