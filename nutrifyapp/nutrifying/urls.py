from django.urls import path
from . import views
from django.contrib.auth import views as auth_user

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index/', views.Index.as_view(), name='index'),
    path('register/', views.registerPage, name='register'),
    path('community/', views.PostCommunity.as_view(), name='community'),
    path('myposts/', views.myposts, name='myposts'),
    path('friendzone/', views.friendzone, name='friendzone'),
    path('friendrequest/', views.friendrequest, name='friendrequest'),
    path('create_post/', views.CommunityPostCreateView.as_view(), name='create_post'),
    path("login", views.login_request, name="login"),
    path('logout/', auth_user.LogoutView.as_view(template_name='home.html'), name="logout"),
    path('create/', views.FoodCreateView.as_view(), name='create_food'),
    path('create_date/', views.DateCreateView.as_view(), name='create_date'),
    path('update/<int:pk>', views.FoodUpdateView.as_view(), name='update_food'),
    path('foods/', views.foods, name='foods'),
    path('delete/<int:pk>', views.FoodDeleteView.as_view(), name='delete_food'),
    path('delete_excercise/<int:pk>', views.ExcerciseDeleteView.as_view(), name='delete_excercise'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('add_exercise/', views.ExerciseCreateView.as_view(), name='add_exercise'),
    path('delete_history/<int:id>', views.delete_history,name='delete_history'),
]
