from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


# Create your views here.

def post_index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 9)
    try:
        page = int(request.GET.get('sayfa', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    contet = {
        'posts': posts,
    }
    return  render(request, 'anasayfa.html', contet )


def post_detaiL(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html',context)

def post_about(request):
    return render(request, 'post/about.html')