from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,CommentForm
from .models import BlogPost, BlogImage,Like,Comment
from django.shortcuts import get_object_or_404

# Create your views here.
def blog(request):
    blog=BlogPost.objects.all().order_by('-created')
    return render(request,'buildhub/blog.html',{'blog':blog})


@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()


            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'buildhub/blogform.html', {'form': form})


def blog_details(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'buildhub/blog_details.html', {'blog': blog})

@login_required
def like_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    like, created = Like.objects.get_or_create(blog=blog, user=request.user)
    if not created:
        like.delete()  # Unlike if already liked
    return redirect('blog_details', blog_id=blog.id)


@login_required
def add_comment(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('blog_details', blog_id=blog.id)
    else:
        form = CommentForm()
    return render(request, 'buildhub/add_comment.html', {'form': form, 'blog': blog})