# models.py

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import *


class ProductDescription(models.Model):
    details = models.TextField()


    def __str__(self):
        return self.details


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/')
    short_description = models.ForeignKey(ProductDescription, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title


ukrainian_name_validator = RegexValidator(
    regex = r'^[А-ЩЬЮЯҐЄІЇа-щьюяґєії\'\s]+$',
    message="Використовуйте українську або англійську мову.",
    code='invalid_name_ukrainian'
)


english_name_validator = RegexValidator(
    regex = r'^[A-Za-z\'\s]+$',
    message="Використовуйте українську або англійську мову.",
    code='invalid_name_english'
)


email_validator = RegexValidator(
    message="Введіть валідну пошту.",
    code='invalid_emale'
)


class FormData(models.Model):
    name = models.CharField('Ім\'я', max_length=100)
    email = models.EmailField('Пошта', unique=True, validators=[email_validator], max_length=100)


    def validate_ukrainian_name(self):
        ukrainian_name_validator(self.name)


    def validate_english_name(self):
        english_name_validator(self.name)


# reg auth users
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Звичайний користувач'),
        ('manager', 'Менеджер'),
        ('admin', 'Адміністратор'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_set',  
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  
        related_query_name='user',
    )