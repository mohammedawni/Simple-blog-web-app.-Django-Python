from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from .models import Post
from django.contrib import messages
# Create your views here.
def all_posts(request):
    all_posts = Post.objects.filter(active = True)
    context = {
        'all_posts' : all_posts,
    }
    return render(request, 'posts.html', context)

def post(request, id):
    post = get_object_or_404(Post ,id = id )
    context = {
        'post' : post,
    }
    return render(request, 'detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Post Created Successful.')
            return redirect('/')
    else:
        form = PostForm()

    return render(request, 'create.html', {'form':form})


def edit_post(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES, instance = post)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Post Edited Successfully.')
            return redirect('/')
    else:
        form = PostForm(instance = post)

    context = {
        'form' : form,
    }
    return render(request, 'edit.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    messages.success(request,'Post Deleted Successfully.')
    return redirect('/')
