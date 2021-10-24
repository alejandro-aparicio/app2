from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(author__lte='1').order_by('author')
    return render(request, 'catalogo/post_list.html', {'posts': posts})
