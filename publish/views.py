from django.shortcuts import get_object_or_404, render

from .models import Post


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post.html", context={"post": post})
