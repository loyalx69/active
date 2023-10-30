from django.shortcuts import render
from simple_app.models import Mypost
from django.utils import timezone

def Post(request):
    all_posts = Mypost.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'index.html', context)