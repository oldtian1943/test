from django.shortcuts import render
from .models import Post

from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

from .forms import PostForm

from django.contrib.auth.decorators import login_required

PostOwner=True
# Create your views here.
def check_post_owner(post_owner,request_user,PostOwner=True):
    if post_owner != request_user:
        raise Http404
        PostOwner=False

def home(request):
    posts=Post.objects.order_by('date_added')
    context={'posts':posts,' PostOwner':PostOwner}
    return render(request,'blogs/home.html',context)

@login_required
def post(request,post_id):
    post=Post.objects.get(id=post_id)
    
    PostOwner=True
    if post.owner != request.user:
        PostOwner=False
        
    context={'post':post,'PostOwner':PostOwner}
    return render(request,'blogs/post.html',context)

@login_required
def add_post(request):
    if request.method !='POST':
        form=PostForm()
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.owner=request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:home'))
    context={'form':form}
    return render(request,'blogs/add_post.html',context)

@login_required
def edit_post(request,post_id):
    
    post=Post.objects.get(id=post_id)
    
    check_post_owner(post.owner,request.user,PostOwner=True)
    
    if request.method !='POST':
        form=PostForm(instance=post)
    else:
        form=PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post',
                                                  args=[post.id]))
                                                
    context={'post':post,'form':form,'PostOwner':PostOwner}
    return render(request,'blogs/edit_post.html',context)



































