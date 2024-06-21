from django.contrib import admin

from .models import Course, ParticipationApplication, Reiting


class CourseAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(ParticipationApplication)
admin.site.register(Reiting)
