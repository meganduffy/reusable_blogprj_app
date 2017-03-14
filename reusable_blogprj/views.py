from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list(request):
    """
    Create a view that will return a list of Posts that were
    published prior to 'now' and render them to the 'blogposts.html'
    template
    """
    # Django allows us to append strings to table fields that act as boolean operators
    # __lte = les-than-or-equal-to
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')  # - indicates descending order
    return render(request, "blog/blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that returns a single Post object based on the
    post id and render it to the 'postdetail.html' template or return
    a 404 error if the post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "blog/postdetail.html", {'post': post})


def top_five(request):
    """
    Create a view that will return a list of top 5 Posts sorted by views
    """
    most_pop = Post.objects.filter(published_date__lte=timezone.now()
                                   ).order_by('-views')[:5]
    return render(request, "blog/top_five.html", {'most_pop': most_pop})


@login_required(login_url='/login/')
def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    # Else GET method is used
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html', {'form':form})


@login_required(login_url='/login/')
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blogpostform.html', {'form': form})