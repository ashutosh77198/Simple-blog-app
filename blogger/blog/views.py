from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles=BlogPost.objects.all()
    return render(request,'blog/artice_list.html',{'articles':articles})
def article_detail(request,slug):
    article=BlogPost.objects.get(slug=slug) 
    return render(request,'blog/article_detail.html',{'article':article})
    #return HttpResponse(slug)
@login_required(login_url="/accounts/login/")    
def article_create(request):
    if request.method=="POST":
        form=forms.CreateBlogPost(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('list')

    else:
        form=forms.CreateBlogPost()
    return render(request,'blog/article_create.html',{'form':form})