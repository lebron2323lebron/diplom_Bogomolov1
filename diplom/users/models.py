from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from datetime import date, timedelta

from django.utils.text import slugify

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    second_name=models.CharField(max_length=100, blank=True)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/avatars/%Y/%m/%d/',
        default='images/avatars/default.jpg',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        """
        Сортировка, название таблицы в базе данных
        """
        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращение строки
        """
        return self.user.username

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        return f'https://ui-avatars.com/api/?size=150&background=random&name={self.slug}'