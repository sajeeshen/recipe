from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """  Managing the create and save user actions """
        if not email:
            raise ValueError("User must have a valid email")
        user = self.model(email=self.normalize_email(email),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Creating the super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email

class Recipe(models.Model):
    """Recipe object"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='createduser'
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """" Ingredient model"""
    text = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name="ingredient")

    def __str__(self):
        return self.text


class Step(models.Model):
    """" Ingredient model"""
    step_text = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='step')

    def __str__(self):
        return self.step_text
