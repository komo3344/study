from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('hello/', views.HelloView.as_view()),
]