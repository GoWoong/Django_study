from django.shortcuts import redirect
# from django.core.paginator import Paginator
from django.views.generic import (
  CreateView, ListView, DetailView, 
  UpdateView, DeleteView, RedirectView)
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post
# Create your views here.

# def index(request):
#   return redirect('post-list')

class IndexRedirectView(RedirectView):
  pattern_name = 'post-list'

# def post_list(request):
#   posts = Post.objects.all()
#   paginator = Paginator(posts, 6)
#   curr_page_number = request.GET.get('page')
#   if curr_page_number is None:
#     curr_page_number = 1
#   page = paginator.page(curr_page_number)
#   return render(request, 'posts/post_list.html', {"page":page})

class PostListView(ListView):
  model = Post
  ordering = ['-dt_created']
  paginate_by = 6


# def post_detail(request, post_id):
#   post = get_object_or_404(Post, id=post_id)
#   context = {"post":post}
#   return render(request, 'posts/post_detail.html',context)

class PostDetailView(DetailView):
  model = Post

# 일반적인 함수형 뷰
# def post_create(request):
#   if request.method == "POST":
#     post_form = PostForm(request.POST)
#     if post_form.is_valid():
#       new_post = post_form.save()
#       return redirect('post-detail', post_id = new_post.id)
#   else:
#     post_form = PostForm()
#   return render(request,'posts/post_form.html',context = {"form":post_form})
  
# 클래스 뷰
# class PostCreateView(View):
#   def get(self, request):
#     post_form = PostForm()
#     return render(request,'posts/post_form.html',{"form":post_form})
#   def post(self, request):
#     post_form = PostForm(request.POST)
#     if post_form.is_valid():
#         new_post = post_form.save()
#         return redirect('post-detail', post_id=new_post.id)
#     return render(request, 'posts/post_form.html', {'form': post_form})

# 제네릭 뷰
class PostCreateView(CreateView):
  model = Post
  form_class = PostForm
  
  def get_success_url(self):
    return reverse('post-detail',kwargs={'pk':self.object.id})


# def post_update(request, post_id):
#   post = get_object_or_404(Post, id=post_id)
#   if request.method == 'POST':
#     post_form = PostForm(request.POST, instance=post)
#     if post_form.is_valid():
#       post_form.save()
#       return redirect('post-detail',post_id = post_id)
#   else:
#     post_form = PostForm(instance=post) #post데이터가 폼에 바운드 된 상태로 생성
#   return render(request,'posts/post_form.html',{"form":post_form})

class PostUpdateView(UpdateView):
  model = Post
  form_class = PostForm
  def get_success_url(self):
    return reverse('post-detail', kwargs={'pk': self.object.id})

# def post_delete(request, post_id):
#   post = get_object_or_404(Post, id=post_id)
#   if request.method == 'POST':
#     post.delete()
#     return redirect('post-list')
#   else:
#     return render(request, 'posts/post_confirm_delete.html',{'post':post})

class PostDeleteView(DeleteView):
  model = Post
  # template_name = 'posts/post_confirm_delete.html' 이게 기본값이다.
  def get_success_url(self):
    return reverse('post-list')
