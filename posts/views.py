from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import NewPostForm


def create_testimonials(request):

    if request.method == "POST":

        form = NewPostForm(request.POST)
        print("in post", form.errors)
        if form.is_valid():

            post_form = form.save(commit=False)
            post = Post.objects.create(
                post=form.cleaned_data.get('post'),
                name=form.cleaned_data.get('name')
            )

            return redirect('testimonials')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})


def list_testimonials(request):
    testimonials = Post.objects.all()

    return render(request, 'home.html')