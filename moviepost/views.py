from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView,DetailView,DeleteView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
from .forms import MoviePostForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルPhotoPostをインポート
from .models import MoviePost


@method_decorator(login_required,name='dispatch')
class PostedView(CreateView):
    form_class=MoviePostForm
    template_name = "post.html"
    success_url = reverse_lazy('moviepost:post_success')
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name ='post_success.html'
    
class UsercontentsView(ListView):
    template_name='contents_home.html'
    context_object_name='orderby_records'
    queryset=MoviePost.objects.order_by('-posted_at')
    paginate_by=4
    
class UsercontentsmainView(ListView):
    template_name='contents_main.html'
    context_object_name='orderby_records'
    queryset=MoviePost.objects.order_by('-posted_at')
    paginate_by=4
    
    
class MovieDeleteView(DeleteView):
  model=MoviePost
  template_name='delete.html'
  success_url=reverse_lazy('mywebsite:home')
  def delete(self,request,*args,**kwargs):
    return super().delete(request,*args,**kwargs)
