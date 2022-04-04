from django import forms
from .models import Post
class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post

    fields = ['title', 'content'] #'__all__'


  # 이전 방식
  # title = forms.CharField(max_length=50, label="제목")
  # content = forms.CharField(label="내용", widget=forms.Textarea)
