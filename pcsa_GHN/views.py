from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .forms import ContactForm, ghnPostForm
from .models import Contact, ghnPost
from .serializers import ContactSerializer, ghnPostSerializer
from .services import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ghnPostsViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ghnPost.objects.all()
    serializer_class = ghnPostSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ListPostView(LoginRequiredMixin, ListView):

    model = ghnPost
    template_name = 'pcsa_GHN/home.html'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(ListPostView, self).get_context_data(**kwargs)
        context['post_list'] = ghnPost.objects.all()
        context['contact_list'] = Contact.objects.all()
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    
    model = ghnPost
    form_class = ghnPostForm
    template_name = 'pcsa_GHN/create_post.html'
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    
    model = ghnPost
    form_class = ghnPostForm
    template_name = "pcsa_GHN/edit_post.html"
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdatePostView, self).form_valid(form)


class DeletePostView(LoginRequiredMixin, DeleteView):

    model = ghnPost
    template_name = "pcsa_GHN/delete_post.html"
    success_url = '/gethelpnow/'
    redirect_field_name = 'redirect_to'


class ViewPostView(LoginRequiredMixin, DetailView):
    model = ghnPost
    template_name = "pcsa_GHN/view_post.html"
    redirect_field_name = 'redirect_to'


class CreateContactView(LoginRequiredMixin, CreateView):
    
    model = Contact
    form_class = ContactForm
    template_name = 'pcsa_GHN/create_contact.html'
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(CreateContactView, self).form_valid(form)


class UpdateContactView(LoginRequiredMixin, UpdateView):
    
    model = Contact
    form_class = ContactForm
    template_name = "pcsa_GHN/edit_contact.html"
    success_url='/gethelpnow/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.owner = self.request.user.pcuser
        return super(UpdateContactView, self).form_valid(form)


class DeleteContactView(LoginRequiredMixin, DeleteView):

    model = Contact
    template_name = "pcsa_GHN/delete_contact.html"
    success_url = '/gethelpnow/'
    redirect_field_name = 'redirect_to'


class ViewContactView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "pcsa_GHN/view_contact.html"
    redirect_field_name = 'redirect_to'
