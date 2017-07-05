from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from pcsa.forms import PostForm
from pcsa.models import PcsaPost
from pcsa.services import (create_post_from_form, delete_post_by_id,
                           get_post_by_id)

from .models import PcsaPost
from .serializers import PcsaPostSerializer
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class PcsaPostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Post endpoint that provides `list` and `detail` actions
    `list` action returns a list of all Posts
    `detail` action returns a particular Post instance based on id
    """
    queryset = PcsaPost.objects.all()
    serializer_class = PcsaPostSerializer


class ListPostView(ListView):

    model = PcsaPost
    template_name = 'pcsa/list_posts.html'


class CreatePostView(LoginRequiredMixin, CreateView):

    model = PcsaPost
    form_class = PostForm
    template_name = 'pcsa/create_post.html'
    success_url='/pcsa/list_posts'
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = PcsaPost
    fields = ['title','description']
    template_name = "pcsa/edit_post.html"
    success_url='/pcsa/list_posts'
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = PcsaPost
    template_name = "pcsa/delete_post.html"
    success_url = '/pcsa/list_posts'
    login_url = '/'
    redirect_field_name = 'redirect_to'


class ViewPostView(LoginRequiredMixin, DetailView):

    model = PcsaPost
    template_name = "pcsa/view_post.html"
    login_url = '/'
    redirect_field_name = 'redirect_to'


'''def list_posts(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post_list = PcsaPost.objects.all()
    return render(request,
                  'pcsa/list_posts.html',
                  {'post_list': post_list})
'''

'''def create_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            owner = request.user.pcuser
            post = create_post_from_form(form, owner)
            return render(request,
                          'pcsa/view_post.html',
                          {'post': post})

    return render(request,
                  'pcsa/create_post.html',
                  {'form': form})'''

'''        
def edit_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        if request.method == 'POST':

            # need to get the original title_post and description_post
            # before it is changed when calling instance on PostForm
            orig_title = post.title
            orig_desc = post.description
            form = PostForm(request.POST, instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title']
                edited_desc = form.cleaned_data['description']

                if (orig_title != edited_title) or \
                        (orig_desc != edited_desc):
                    post = create_post_from_form(form, owner)

                return HttpResponseRedirect(reverse('pcsa:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'pcsa/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = PostForm(instance=post)
            return render(request,
                          'pcsa/edit_post.html',
                          {'form': form, 'post': post})
    else:
        raise Http404
'''


'''
def delete_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if delete_post_by_id(post_id):
            return HttpResponseRedirect(reverse('pcsa:list_posts'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa/delete_post.html',
                      {'post_id': post_id})
'''


'''
def view_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        return render(request,
                      'pcsa/view_post.html',
                      {'post': post})
    else:
        raise Http404
'''