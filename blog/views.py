from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# View to display all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create post
def create_post(request):
    post = Post.objects.create(title="New Post", content="This is a new post.")
    return render(request, 'blog/post_detail.html', {'post': post})

# Update post
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.title = "Updated Post Title"
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

# Delete post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
