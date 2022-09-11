from django.urls import path
from . import views
from django.contrib.auth import views as auth_user

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.Index.as_view(), name='index'),
    path('register/', views.registerPage, name='register'),
    path("login", views.login_request, name="login"),
    path('logout/', auth_user.LogoutView.as_view(template_name='home.html'), name="logout"),
    path('create/', views.FoodCreateView.as_view(), name='create_food'),
    path('update/<int:pk>', views.FoodUpdateView.as_view(), name='update_food'),
    path('delete/<int:pk>', views.FoodDeleteView.as_view(), name='delete_food'),
    path('add_exercise/', views.ExerciseCreateView.as_view(), name='add_exercise'),
]
