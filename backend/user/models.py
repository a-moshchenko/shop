from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse

from .managers import CustomUserManager


class Customer(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=255, unique=True, verbose_name='логин')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    slug = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='media/user_photo',
                               verbose_name='Фото',
                               default='not_available.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELD = ['login']
    USERNAME_FIELD = 'login'

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
