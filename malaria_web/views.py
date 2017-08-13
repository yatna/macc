from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
import urllib.request, json 

from malaria_web.forms import PostForm
from malaria_web.models import Post, MalariaUsers
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

class ListAppUsersView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        with urllib.request.urlopen("https://rawgit.com/yatna/0e6b1ce2435de3e10a779aad40b4375b/raw/Malaria_users.json") as url:
            data = json.loads(url.read().decode())
            for user in data:
                MalariaUsers.objects.get_or_create(name=user['name'],email=user['email'],age=user['age'],gender=user['gender'],medicineType=user['medicineType'])
        queryset = MalariaUsers.objects.all()
        return queryset
    template_name = 'malaria/list_app_users.html'
    redirect_field_name = 'redirect_to'
