from django.shortcuts import render,get_object_or_404
from . models import *
# Create your views here.
def post(request):
	posts=Post.objects.all()
	return render (request,'blog/post.html',{'posts':posts})

def detail(request,post_id):
	post= get_object_or_404(Post,pk=post_id)
	return render (request,'blog/detail.html',{'post':post})
