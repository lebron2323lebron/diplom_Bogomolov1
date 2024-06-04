from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="название")
    logo = models.ImageField(verbose_name="логотип", null=True, blank=True)
    users = models.ManyToManyField(get_user_model(), related_name="courses")

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"