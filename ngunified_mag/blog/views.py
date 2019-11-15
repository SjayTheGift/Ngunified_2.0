from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_posted')
    paginate_by = 5
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
