from django.shortcuts import render

from .forms import *
from .models import *
from rest_framework import viewsets
from django.http import *
from .serializers import *
from rest_framework.response import Response
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class FirstAideAPIViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = firstAideAPISerializer
    page_id=""
    page_type=""
    title=""

    def get_queryset(self):
        queryset = FirstAideAPI.objects.all().filter(post_id=self.kwargs['id'])
        FirstAideAPIViewSet.page_id = queryset.values_list('post_id',flat=True)[0]
        FirstAideAPIViewSet.page_type = queryset.values_list('page_type',flat=True)[0]
        FirstAideAPIViewSet.title= queryset.values_list('title',flat=True)[0]
        return queryset

    def list(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(instance, many=True)

        serializer_data = {"page_id": FirstAideAPIViewSet.page_id,"page_type":FirstAideAPIViewSet.page_type,"title":FirstAideAPIViewSet.title}
        serializer_data .update({"content": {"cards":serializer.data}})
        return Response(serializer_data) 

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



