from django.shortcuts import render, get_object_or_404
from blog.models import Post
# we can use from .models import Post also
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# from django.http import HttpResponse


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):  # shortcut then function view
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):  # shortcut then function view
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):  # just to get all the post of username when clicked on their username......
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):  # more shortcut then PostListView
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin is for classed based view and @decorator is for functional view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # to get the id of current loggedin user
        form.instance.author = self.request.user
        return super().form_valid(form)  # see models.py after this to set the path to redirect after posting a blog


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # for UserPassesTestMixin to be alble to update he post created by the loggedin users only but not other users post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # more shortcut then PostListView
    model = Post
    success_url = '/'

    def test_func(self):  # to be alble to update he post created by the loggedin users only but not other users post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
