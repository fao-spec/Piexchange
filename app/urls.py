# my_app/urls.py

from django.urls import path
from . import views
from .views import signup, signin, signout, wallet_connect, idkyou

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('wallet-connect/', wallet_connect, name='wallet_connect'),
    path('idkyou/', views.idkyou, name='idkyou'),
]
