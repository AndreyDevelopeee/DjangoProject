from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('employ', views.employ, name='employ'),
    path('login', views.login, name='login'),
    path('create_objav', views.create_objav, name='create_objav'),
]
