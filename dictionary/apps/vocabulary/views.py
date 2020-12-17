from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.utils import timezone

from .models import Word

def home(request):
  try:
    vocabulary_list = Word.objects.filter(author=request.user).order_by('-adding_date')
    return render(request, 'vocabulary/home.html', {'vocabulary_list':vocabulary_list})
  except:
    return render(request, 'vocabulary/home.html')

def add_word(request):
  word = Word.objects.filter(author=request.user.id)
  word.create(
    word=request.POST['word'],
    definition=request.POST['definition'],
    author=request.user,
    adding_date=timezone.now())
  return HttpResponseRedirect( reverse('vocabulary:home') )

def remove_word(request, article_id):
  word = Word.objects.get(id = article_id)
  word.delete()
  return HttpResponseRedirect( reverse('vocabulary:home') )

def update_word(request, article_id):
  word = Word.objects.get(id = article_id)
  word.word = request.POST['newWord']
  word.definition = request.POST['newDefinition']
  word.save()
  return HttpResponseRedirect( reverse('vocabulary:home') )

def memorization(request):
  return render(request, 'vocabulary/memorization.html')
