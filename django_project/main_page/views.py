from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    if request.method == 'POST':
        f = Post(title=request.POST.get('title'), text=request.POST.get('text'))
        f.save()

    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'index.html',
        context={
            'post_list': page_obj,
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


def create_post(request):
    return render(request, 'create_post.html')
