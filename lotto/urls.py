from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lotto_index'),
    path('form', views.post),
]
