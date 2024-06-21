from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

from users.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="название")
    logo = models.ImageField(verbose_name="логотип", null=True, blank=True)
    users = models.ManyToManyField(get_user_model(), related_name="courses", null=True)

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.title


class ParticipationApplication(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="participation_applications", verbose_name='Курсы')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participation_applications", verbose_name='Пользователь')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')
    time = models.TimeField(blank=False, null=False, verbose_name='Время')
    date = models.DateField(blank=False, null=False, verbose_name='Дата')
    wishes = models.TextField(blank=True, null=True, verbose_name='Оставьте комментарий')

    class Meta:
        verbose_name = "заявка на участие"
        verbose_name_plural = "заявки на участие"


class Reiting(models.Model):
    user = models.ManyToManyField(get_user_model(), related_name="reiting", null=True)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Отзыв")
    logo = models.ImageField(verbose_name="аватар", null=True, blank=True)
    date = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = "Отзывы"
    