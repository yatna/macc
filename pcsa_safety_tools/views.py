from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .forms import SafetyToolsPostForm
from .models import SafetyToolsPost
from .serializers import SafetyToolsPostSerializer
from .services import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class SafetyToolsPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SafetyToolsPost.objects.all()
    serializer_class = SafetyToolsPostSerializer


'''class ListPostView(LoginRequiredMixin, ListView):

    model = SafetyToolsPost
    template_name = 'pcsa_safety_tools/home.html'

    radar = SafetyToolsPost.objects.filter(category_id=1)
    unwanted_attention = SafetyToolsPost.objects.filter(category_id=2)
    tactics = SafetyToolsPost.objects.filter(category_id=3)
    bystander_intervention = SafetyToolsPost.objects.filter(category_id=4)
    safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5)
    safety_plan = SafetyToolsPost.objects.filter(category_id=6)

    def get_object(self, **kwargs):
        return reverse('pcsa_safety_tools:home', kwargs = { 'categories': categories })'''


def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))
    radar = SafetyToolsPost.objects.filter(category_id=1)
    unwanted_attention = SafetyToolsPost.objects.filter(category_id=2)
    tactics = SafetyToolsPost.objects.filter(category_id=3)
    bystander_intervention = SafetyToolsPost.objects.filter(category_id=4)
    safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5)
    safety_plan = SafetyToolsPost.objects.filter(category_id=6)
    categories = [radar, unwanted_attention, tactics, bystander_intervention, safety_plan_basics, safety_plan]

    return render(request, 'pcsa_safety_tools/home.html', {'categories': categories})


class CreatePostView(LoginRequiredMixin, CreateView):
    
    model = SafetyToolsPost
    form_class = SafetyToolsPostForm
    template_name = 'pcsa_safety_tools/create_post.html'
    success_url='/safetytools/home/'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = SafetyToolsPost
    form_class= SafetyToolsPostForm
    template_name = "pcsa_safety_tools/edit_post.html"
    success_url='/safetytools/home/'


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = SafetyToolsPost
    template_name = "pcsa_safety_tools/delete_post.html"
    success_url = '/safetytools/home/'


class ViewPostView(LoginRequiredMixin, DetailView):
    model = SafetyToolsPost
    template_name = "pcsa_safety_tools/view_post.html"


'''
def create_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = SafetyToolsPostForm()
    if request.method == 'POST':
        form = SafetyToolsPostForm(request.POST)
        if form.is_valid():
            post = create_post_from_form(form)
            return render(request,
                          'pcsa_safety_tools/view_post.html',
                          {'post': post})

    return render(request,
                  'pcsa_safety_tools/create_post.html',
                  {'form': form})
'''

"""
    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)"""

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
            form = SafetyToolsPostForm(request.POST, instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title']
                edited_desc = form.cleaned_data['description']

                if (orig_title != edited_title) or \
                        (orig_desc != edited_desc):
                    post = create_post_from_form(form, owner)

                return HttpResponseRedirect(reverse('pcsa_safety_tools:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'pcsa_safety_tools/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = SafetyToolsPostForm(instance=post)
            return render(request,
                          'pcsa_safety_tools/edit_post.html',
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
            return HttpResponseRedirect(reverse('pcsa_safety_tools:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_safety_tools/delete_post.html',
                      {'post_id': post_id})
'''

'''
def view_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        return render(request,
                      'pcsa_safety_tools/view_post.html',
                      {'post': post})
    else:
        raise Http404
'''