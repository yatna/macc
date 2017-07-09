from profiles.models import Pcuser
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PcuserForm
from allauth.account.views import PasswordChangeView


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['pcuser'] = self.request.user.pcuser
        return context


class EditProfile(LoginRequiredMixin, UpdateView):
    
    template_name = 'profiles/edit_profile.html'
    form_class = PcuserForm
    model = Pcuser
    success_url = "/profile/"


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user.first_name = self.request.POST['first_name']
        instance.user.last_name = self.request.POST['last_name']
        instance.user.email = self.request.POST['email']
        instance.user.save()
        return super(EditProfile, self).form_valid(form)
