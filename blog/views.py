from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
                 'blog/post/list.html',
                 {'posts': posts})

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
