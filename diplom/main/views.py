from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, CreateView

from main.forms import ApplicationForm
from main.models import ParticipationApplication


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def prices(request):
    return render(request, 'main/prices.html')


def cources(request):
    return render(request, 'main/cources.html')


def reiting(request):
    return render(request, 'main/reiting.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def forma(request):
    return render(request, 'main/forma.html', context={"user": request.user})


def profile(request):
    return render(request, 'main/profile.html')


def profile_courses(request):
    return render(request, "main/profile-courses.html", context={"courses": request.user.courses.all()})


class ApplicationFormView(CreateView):
    template_name = "main/application_form.html"
    form_class = ApplicationForm
    success_url = "/profile-courses"
    model = ParticipationApplication

    def get_context_data(self, **kwargs):
        kwargs["user"] = self.request.user
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = self.request.user
        course = form.cleaned_data["course"]
        form.instance.course = course
        form.instance.user = user
        user.courses.add(course)
        # print(dir(form))
        # print(form.cleaned_data)
        return super().form_valid(form)

def about(request):
    return render(request, "main/about_us.html")

def course1(request):
    return render(request, 'main/course1.html')

def course2(request):
    return render(request, 'main/course2.html')

def course3(request):
    return render(request, 'main/course3.html')

def module(request):
    return render(request, "main/modules.html")