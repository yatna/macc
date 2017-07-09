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


class ListPostView(LoginRequiredMixin, ListView):

    model = SafetyToolsPost
    template_name = 'pcsa_safety_tools/home.html'

    def get_context_data(self, **kwargs):
        radar = SafetyToolsPost.objects.filter(category_id=1)
        unwanted_attention = SafetyToolsPost.objects.filter(category_id=2)
        tactics = SafetyToolsPost.objects.filter(category_id=3)
        bystander_intervention = SafetyToolsPost.objects.filter(category_id=4)
        safety_plan_basics = SafetyToolsPost.objects.filter(category_id=5)
        safety_plan = SafetyToolsPost.objects.filter(category_id=6)
        categories = [radar, unwanted_attention, tactics, bystander_intervention, safety_plan_basics, safety_plan]
        context = super(ListPostView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context


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
