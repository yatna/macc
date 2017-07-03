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


'''
def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))
    post_list = ghnPost.objects.all()
    contact_list = Contact.objects.all()
    return render(request, 'pcsa_GHN/home.html', {'post_list': post_list, 'contact_list': contact_list})
'''


'''def create_post(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = ghnPostForm()
    if request.method == 'POST':
        form = ghnPostForm(request.POST,request.FILES)
        if form.is_valid():
            owner = request.user.pcuser
            post = create_post_from_form(form, owner)
            return render(request,
                          'pcsa_GHN/view_post.html',
                          {'post': post})

    return render(request,
                  'pcsa_GHN/create_post.html',
                  {'form': form})'''

'''
def create_contact(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return render(request,
                          'pcsa_GHN/view_contact.html',
                          {'contact':contact})

    return render(request,
                  'pcsa_GHN/create_contact.html',
                  {'form': form})
'''


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
            orig_link = post.link
            orig_photo = post.photo
            form = ghnPostForm(request.POST, request.FILES,instance=post)

            if form.is_valid():

                owner = request.user.pcuser
                edited_title = form.cleaned_data['title']
                edited_desc = form.cleaned_data['description']
                edited_link = form.cleaned_data['link']
                edited_photo = form.cleaned_data['photo']

                if (orig_title != edited_title) or \
                    (orig_desc != edited_desc) or \
                    (orig_link != edited_link) or \
                    (orig_photo != edited_photo) :

                    post = create_post_from_form(form, owner)

                return HttpResponseRedirect(reverse('pcsa_GHN:view_post',
                                                    args=(post_id,)))
            else:
                return render(request,
                              'pcsa_GHN/edit_post.html',
                              {'form': form, 'post': post})
        else:
            form = ghnPostForm(instance=post)
            return render(request,
                          'pcsa_GHN/edit_post.html',
                          {'form': form, 'post': post})
    else:
        raise Http404
'''


'''
def edit_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    contact = Contact.objects.get(pk=contact_id)
    if contact:
        if request.method == 'POST':

            # need to get the original title_post and description_post
            # before it is changed when calling instance on PostForm
            orig_office = contact.office_name
            orig_number = contact.contact_number
            form = ContactForm(request.POST, instance=contact)

            if form.is_valid():

                edited_office = form.cleaned_data['office_name']
                edited_number = form.cleaned_data['contact_number']

                if (orig_office != edited_office) or \
                        (orig_number != edited_number):
                    contact = create_contact_from_form(form)

                return HttpResponseRedirect(reverse('pcsa_GHN:view_contact',
							args=(contact_id,)))
            else:
                return render(request,
                              'pcsa_GHN/edit_contact.html',
                              {'form': form, 'contact': contact})
        else:
            form = ContactForm(instance=contact)
            return render(request,
                          'pcsa_GHN/edit_contact.html',
                          {'form': form, 'contact': contact})
    else:
        raise Http404
'''


'''
def delete_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if delete_post_by_id(post_id):
            return HttpResponseRedirect(reverse('pcsa_GHN:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_GHN/delete_post.html',
                      {'post_id': post_id})
'''
'''
def delete_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    if request.method == 'POST':
        if contact_id:
            contact = Contact.objects.get(pk=contact_id)
            contact.delete()
            return HttpResponseRedirect(reverse('pcsa_GHN:home'))
        else:
            raise Http404
    else:
        return render(request,
                      'pcsa_GHN/delete_contact.html',
                      {'contact_id': contact_id})
'''

'''
def view_post(request, post_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    post = get_post_by_id(post_id)
    if post:
        return render(request,
                      'pcsa_GHN/view_post.html',
                      {'post': post})
    else:
        raise Http404
'''

'''
def view_contact(request, contact_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('webhub:index'))

    contact = get_contact_by_id(contact_id)
    if contact:
        return render(request,
                      'pcsa_GHN/view_contact.html',
                      {'contact': contact})
    else:
        raise Http404
'''
