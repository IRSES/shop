# models.py

from django.db import models
from django.core.validators import RegexValidator


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/img/')  # Путь для сохранения изображений товаров
    def __str__(self):
        return self.title
# Сделать расширения модели Product чтоб была любая инфа 1 ко всем


name_regex = r'^[А-ЩЬЮЯҐЄІЇа-щьюяґєії\'\s]+$'
name_validator = RegexValidator(
    regex=name_regex,
    message="Використовуйте українську мову.",
    code='invalid_name'
)
email_validator = RegexValidator(
    message="Введіть валідну пошту.",
    code='invalid_emale'
)
class FormData(models.Model):
    name = models.CharField('Ім\'я', validators=[name_validator], max_length=100)
    email = models.EmailField('Пошта', unique=True, validators=[email_validator], max_length=100)


# class Marks():
#     mark = 
# class ProductDescription(models.Models):
#     title

# расширить функциональность второй таблицей(добавить что-то(инфа с повторением(подвиды растейний из разных стран)))

# 3 кнопка админ панель(пароль логин)