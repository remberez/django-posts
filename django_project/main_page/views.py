from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    all_posts = Post.objects.all()
    return render(
        request,
        'index.html',
        context={
            'post_list': all_posts,
        }
    )


def detail_post(request, pk):
    obj = Post.objects.get(pk=pk)
    context = {
        'title': obj.title,
        'text': obj.text,
        'date_created': obj.date_of_creation
    }
    return render(
        request,
        'detail_post.html',
        context=context,
    )