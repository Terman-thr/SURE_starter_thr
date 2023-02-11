from django.shortcuts import render
from django.http import HttpResponse


def get_index(request):
    return render(request, 'index.html', {'name': 'thr'})
