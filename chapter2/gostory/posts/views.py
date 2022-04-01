from multiprocessing import context
from django.shortcuts import render
from posts.models import Post
# Create your views here.

def post_list(request):
  posts = Post.objects.all()
  context = {"posts": posts}
  return render(request, 'posts/post_list.html',context)