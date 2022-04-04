from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
  # memo = forms.CharField(max_length=80, validators=[validate_symbols])
  class Meta:
    model = Post
    fields = ['title', 'content'] #'__all__'
    widgets = {
      "title":forms.TextInput(attrs={
        "class":"title",
        "placeholder": "제목을 입력 하세요."}),
      "content": forms.Textarea(attrs={
        "placeholder": "내용을 입력하세요."})
      }
  def clean_title(self):
    title = self.cleaned_data['title']
    if '*' in title:
      raise ValidationError('*는 포함될 수 없습니다.')
    return title

  # 이전 방식
  # title = forms.CharField(max_length=50, label="제목")
  # content = forms.CharField(label="내용", widget=forms.Textarea)
