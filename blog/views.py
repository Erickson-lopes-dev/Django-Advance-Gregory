from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, ListView, CreateView, DetailView, UpdateView, DeleteView
# from django.views.generic.detail import
from blog.models import Post


def list_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})


def create_post(request):
    if request.POST:
        Post.objects.create(
            title=request.POST['title'],
            sub_title=request.POST['sub_title'],
            content=request.POST['content'],
            user=request.user
        )
        return render(request, 'blog/create.html', {'save': 'Salvo com sucesso'})
    return render(request, 'blog/create.html')


def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'blog/update.html', {'post': post})
    else:
        Post.objects.filter(pk=pk).update(
            title=request.POST['title'],
            sub_title=request.POST['sub_title'],
            content=request.POST['content'],
            user=request.user)
        return render(request, 'blog/update.html',
                      {'update_status': 'item atualizado', 'post': Post.objects.get(pk=pk)})


def delete_post(request, pk):
    if request.method == 'GET':
        Post.objects.get(pk=pk).delete()
    return redirect(reverse('list'))


class HomePageView(TemplateView):
    template_name = 'blog/post_list.html'


class MyView(View):
    def get(self, request):
        return render(request, 'blog/post_list.html')

    # def post(self, request):
    #     return render(request, 'blog/post_list.html')


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = 'um nome para exibir'
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'sub_title', 'content']
    success_url = reverse_lazy('list_post')

    # colocando o usuario que esta logado dentro do usuario
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'sub_title', 'content']
    success_url = reverse_lazy('list_post')

    # colocando o usuario que esta logado dentro do usuario
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    # success_url = reverse_lazy('list_post')

    def get_success_url(self):
        # pode salvar informações como o a informação que vai ser excluida etc ..
        reverse_lazy('list_post')
