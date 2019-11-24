from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:word_id>', views.spell, name='spell'),
    path('input', views.input, name='input')
]
