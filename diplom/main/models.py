from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="participation_applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participation_applications")
    price = models.DecimalField(max_digits=11, decimal_places=2)
    phone_number = PhoneNumberField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    wishes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "заявка на участие"
        verbose_name_plural = "заявки на участие"


class Reiting(models.Model):
    user = models.ManyToManyField(get_user_model(), related_name="reiting", null=True)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Отзыв")
    logo = models.ImageField(verbose_name="аватар", null=True, blank=True)
    date = models.DateField(blank=False, null=False)
    