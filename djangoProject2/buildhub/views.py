from django.shortcuts import render,redirect
from . forms import BlogForm
from .models import BlogPost
# Create your views here.
def blog(request):
    blog=BlogPost.objects.all()
    return render(request,'buildhub/blog.html',{'blog':blog})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirect after successfully creating the course
    else:
        form = BlogForm()
    # Make sure to explicitly render courseform.html
    return render(request, 'buildhub/blogform.html', {'form': form})