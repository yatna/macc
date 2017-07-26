from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from malaria_web.forms import PostForm
from malaria_web.models import Post
from malaria_web.services import (create_post_from_form, create_revpost,
                                  delete_post_by_id, get_post_by_id,
                                  get_revposts_of_owner)
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ListPostView(LoginRequiredMixin, ListView):

    model = Post
    template_name = 'malaria/list_posts.html'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        result = super(ListPostView, self).get_queryset()
        category = self.request.GET.get('category')
        if self.request.GET:
            if self.request.GET.get('asc'):
                result = Post.objects.order_by(category)
            elif self.request.GET.get('desc'):
               result = Post.objects.order_by('-'+category)
            print(result)

        return result
        


class CreatePostView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = PostForm
    template_name = 'malaria/create_post.html'
    success_url='/malaria/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = Post
    form_class = PostForm
    template_name = "malaria/edit_post.html"
    success_url='/malaria/list_posts'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = Post
    template_name = "malaria/delete_post.html"
    success_url = '/malaria/list_posts'
    redirect_field_name = 'redirect_to'


class ViewPostView(LoginRequiredMixin, DetailView):

    model = Post
    template_name = "malaria/view_post.html"
    redirect_field_name = 'redirect_to'
