from django.shortcuts import render
from blog import urls
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all
    return render(request,'index.html', {'posts':posts})

def posts(request, pk):
    posts = Post.objects.get(html_tag=pk)
    return render(request,'posts.html', {'posts':posts})
