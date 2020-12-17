from django.urls import path, include

from . import views

app_name = 'vocabulary'

urlpatterns = [
  path('', views.home, name = 'home'),
  path('add_word', views.add_word, name = 'add_word'),
  path('<int:article_id>/remove_word/', views.remove_word, name = 'remove_word'),
  path('<int:article_id>/update_word/', views.update_word, name = 'update_word'),
  path('memorization', views.memorization, name = 'memorization'),
]
