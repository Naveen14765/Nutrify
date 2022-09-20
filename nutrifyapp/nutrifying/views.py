from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Excercise, DateField
from django.db.models import Sum
import datetime
from dateutil import parser
from collections import Counter, defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render


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
    BSModalCreateView,
    BSModalUpdateView,
    BSModalDeleteView,

)

from .forms import (
    FoodModelForm,
    DateModelForm,
    ExcerciseModelForm,
    CommunityModelForm,
)
from .models import Health, CommunityPeople


class Index(generic.ListView):
    total_gained = 0
    total_loss = 0
    model = Health
    context_object_name = 'foods'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        date_current = DateField.objects.last().userinput
        context = super(Index, self).get_context_data(**kwargs)
        context['add_workout'] = Excercise.objects.filter(userName=self.request.user).filter(currentdate=date_current)
        context['gained_calories'] = Health.objects.filter(userName=self.request.user).filter(
            currentdate=date_current).aggregate(Sum('calories'))
        context['burnt_calories'] = Excercise.objects.filter(userName=self.request.user).filter(
            currentdate=date_current).aggregate(Sum('calories'))
        try:
            for i in Excercise.objects.filter(userName=self.request.user).filter(currentdate=date_current).aggregate(
                    Sum('calories')).values():
                self.total_loss = i
            for j in Health.objects.filter(userName=self.request.user).filter(currentdate=date_current).aggregate(
                    Sum('calories')).values():
                self.total_gained = j
            calories_left = self.total_gained - self.total_loss
            context['calories_left'] = {'calories_left': calories_left}

            return context
        except:

            return context

    def get_queryset(self):
        date_current = DateField.objects.last().userinput
        return Health.objects.filter(userName=self.request.user).filter(currentdate=date_current)


class FoodCreateView(BSModalCreateView):
    template_name = 'examples/create_food.html'
    form_class = FoodModelForm
    success_message = 'Success: Food Field was created.'
    success_url = reverse_lazy('index')


class DateCreateView(BSModalCreateView):
    template_name = 'examples/create_date.html'
    form_class = DateModelForm
    success_message = 'Success: date was created.'
    success_url = reverse_lazy('index')


class ExerciseCreateView(BSModalCreateView):
    template_name = 'examples/add_workout.html'
    form_class = ExcerciseModelForm
    success_message = 'Success: Date created successfully'
    success_url = reverse_lazy('index')


class FoodUpdateView(BSModalUpdateView):
    model = Health
    template_name = 'examples/update_food.html'
    form_class = FoodModelForm
    success_message = 'Success: Food was updated.'
    success_url = reverse_lazy('index')


class FoodDeleteView(BSModalDeleteView):
    model = Health
    template_name = 'examples/delete_food.html'
    success_message = 'Success: Food Field was deleted.'
    success_url = reverse_lazy('index')


class ExcerciseDeleteView(BSModalDeleteView):
    model = Excercise
    template_name = 'examples/delete_workout.html'
    success_message = 'Success: Excercise Field was deleted.'
    success_url = reverse_lazy('index')


def foods(request):
    data = dict()
    if request.method == 'GET':
        foods = Health.objects.all()
        data['table'] = render_to_string(
            '_foods_table.html',
            {'foods': foods},
            request=request
        )
        return JsonResponse(data)


def add_workout(request):
    data = dict()
    if request.method == 'GET':
        add_workout = Excercise.objects.all()
        data['table'] = render_to_string('_foods_table.html', {'add_workout': add_workout}, request=request)
        return JsonResponse(data)


class PostCommunity(generic.ListView):
    model = CommunityPeople
    context_object_name = 'communityposts'
    template_name = 'community.html'

    def get_queryset(self):
        return CommunityPeople.objects.all()


class CommunityPostCreateView(BSModalCreateView):
    template_name = 'examples/create_post.html'
    form_class = CommunityModelForm
    success_message = 'Success: Community Post was created.'
    success_url = reverse_lazy('community')


def analytics(request):
    return render(request, 'analytics.html', {})


def myposts(request):
    myposts = CommunityPeople.objects.filter(userName=request.user)
    return render(request, "myposts.html", {'myposts': myposts})


def delete_history(request, id):
    selected_history = CommunityPeople.objects.get(id=id)
    selected_history.delete()
    return redirect("myposts")
