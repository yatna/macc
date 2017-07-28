from django.shortcuts import render

from .forms import *
from .models import *
from rest_framework import viewsets
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class FirstAideAPIViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = FirstAideAPI.objects.all()

class ListFirstAideAPIView(LoginRequiredMixin, ListView):

    model = FirstAideAPI
    template_name = 'firstaide/home.html'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListFirstAideAPIView, self).get_context_data(**kwargs)
        context['post_list'] = FirstAideAPI.objects.all().order_by('post_id')
        return context

class CreateFirstAideAPIView(LoginRequiredMixin, CreateView):
    
    model = FirstAideAPI
    form_class = FirstAideAPIForm
    template_name = 'firstaide/create_post.html'
    success_url='/firstaide/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreateFirstAideAPIView, self).form_valid(form)

class UpdateFirstAideAPIView(LoginRequiredMixin, UpdateView):
    
    model = FirstAideAPI
    form_class = FirstAideAPIForm
    template_name = "firstaide/edit_post.html"
    success_url='/firstaide/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdateFirstAideAPIView, self).form_valid(form)


class DeleteFirstAideAPIView(LoginRequiredMixin, DeleteView):

    model = FirstAideAPI
    template_name = "firstaide/delete_post.html"
    success_url = '/firstaide/'
    redirect_field_name = 'redirect_to'


class ViewFirstAideAPIView(LoginRequiredMixin, DetailView):
    model = FirstAideAPI
    template_name = "firstaide/view_post.html"
    redirect_field_name = 'redirect_to'



