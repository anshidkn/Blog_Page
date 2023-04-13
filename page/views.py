from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post,Comment
from .forms import PostForm,AddCommentForm


class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-id']
    
class ArticleDetailView(DetailView):
    model=Post
    template_name='article.html'

class AddPostView(CreateView):
    model=Post
    template_name='add_post.html'
    form_class=PostForm
    # fields="__all__"
    success_url=reverse_lazy('home')

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=PostForm
    # fields= "__all__"
    success_url=reverse_lazy('home')

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['pk']})
    
class CommentReplyView(CreateView):
    model = Comment
    template_name = 'add_reply.html'
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        form.instance.parent_id = self.kwargs['comment_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.kwargs['post_id']})

def comment_tree(request):
    comments = Comment.objects.filter(parent=None)
    context = {
        'comments': comments
    }
    return render(request, 'comment_tree.html', context)

