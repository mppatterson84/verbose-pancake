from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10
    ordering = ['-pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['blog_active'] = 'active'
        context['blog_active_link'] = '#'
        context['blog_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = PostForm
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Post'
        context['new_active'] = 'active'
        context['new_active_link'] = '#'
        context['new_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

    # https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete'
        return context

def post_search_view(request):
    queryset_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) 
                ).distinct()
    else:
        queryset_list = None
    posts = queryset_list
    context = {
        'title': 'Search Posts',
        'posts': posts,
    }
    return render(request, 'blog/post_search.html', context)

class PostListAllView(ListView):
    model = Post
    template_name = 'blog/post_list_all.html'
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Posts'
        context['all_active'] = 'active'
        context['all_active_link'] = '#'
        context['all_active_sr'] = '<span class="sr-only">(current)</span>'
        return context