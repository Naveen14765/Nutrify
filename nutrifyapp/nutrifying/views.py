from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Excercise


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homepage(request):
    return render(request, 'home.html', {})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerPage(request):
    if request.method == "POST":
        form = CreateUserForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CreateUserForms()
    return render(request, "register.html", {"form": form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect('homepage')
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form": form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, 'index.html', {})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home.html")


from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    FoodModelForm,
    ExcerciseModelForm,
)
from .models import Health


class Index(generic.ListView):
    model = Health
    context_object_name = 'foods'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['add_workout'] = Health.objects.filter(userName=self.request.user)
        return context

    def get_queryset(self):
        return Health.objects.filter(userName=self.request.user)


class FoodCreateView(BSModalCreateView):
    template_name = 'examples/create_food.html'
    form_class = FoodModelForm
    success_message = 'Success: Food Field was created.'
    success_url = reverse_lazy('index')


class ExerciseCreateView(BSModalCreateView):
    template_name = 'examples/add_workout.html'
    form_class = ExcerciseModelForm
    success_message = 'Success: Workout created successfully'
    success_url = reverse_lazy('index')


class FoodUpdateView(BSModalUpdateView):
    model = Health
    template_name = 'examples/update_food.html'
    form_class = FoodModelForm
    success_message = 'Success: Food Field was updated.'
    success_url = reverse_lazy('index')


class FoodDeleteView(BSModalDeleteView):
    model = Health
    template_name = 'examples/delete_food.html'
    success_message = 'Success: Food Feild was deleted.'
    success_url = reverse_lazy('index')

