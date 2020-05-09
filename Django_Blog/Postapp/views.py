from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class Home(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Postapp/home.html'
    ordering = '-date_posted'



class UserPostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Postapp/user_post.html'
    ordering = '-date_posted'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date_posted')



def about(request):
    return render(request, template_name='Postapp/about.html')


class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'Postapp/post_detail.html'


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'user/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # class Meta:
        

# LoginRequiredMixin so we cant post without being logged in
# UserPassesTestMixin check if user author is the same as the logged in
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'user/post_form.html'
    fields = ['title', 'content']


# To provide the current logged in user as an author of the post
# otherwise we get an integrity error
# This provides the author field in the model with the current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Since it's an update function we must check if the user who wants to 
# update the post is the author of the post

    def test_func(self):
        # First we get the object we want to check
        post = self.get_object()
        # Check if the current user == the author of the post
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'user/post_confirm_delete.html'
    success_url = '/'
    


    def test_func(self):
        # First we get the object we want to check
        post = self.get_object()
        # Check if the current user == the author of the post
        if self.request.user == post.author:
            return True
        return False
    

