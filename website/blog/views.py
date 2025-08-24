from django.shortcuts import render,get_object_or_404,redirect
from blog.models import post

# Create your views here.
def allpost(request):
    posts = post.objects.all()
    return render(request,'posts.html',{'post':post})

def detail(request,post_id):
    detail = get_object_or_404(post,pk=post_id)
    return render(request,'details.html',{'detail':detail})
