from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer then deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                'blog/post/list.html',
                {'page': page,
                'posts': posts})

def post_detail(request, year, month, day, post):
    try:
        post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day = day)
        print(post.title)
        print(post.author)
        print(post.get_absolute_url())
    except Exception as exc:
        print("Exception occured in post_detail", end="\n")
        print(exc)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


