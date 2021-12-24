from django.http import response
from django.shortcuts import redirect, render
from . models import *
from django.http.response import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from . forms import *
from django.contrib import messages


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)


def create(request):
    if request.method == 'POST':    
        post = Post.objects.create(
            post = request.POST['post']
            )
        messages.success(request, 'Task Created')
        return redirect('home')

    return render(request, 'home.html')


def delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    messages.success(request, '✔ Done')
    return redirect('home')


def contact(request):
    return render(request, 'contact.html')

