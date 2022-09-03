from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms


def index(request):
    return render(request, 'index.html', {})


def registerPage(request):
    form = CreateUserForms()
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    return render(request, 'login.html', {})
