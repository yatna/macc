from profiles.models import Pcuser
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PcuserForm
from allauth.account.views import PasswordChangeView


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'profiles/profile.html'

# <<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['pcuser'] = self.request.user.pcuser
        return context
# =======
# # Create your views here.
# @csrf_exempt
# def login_do(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
    
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             if 'redirect' in request.POST.keys():
#                 return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":request.POST['redirect'].replace("!!__!!","&")}))
#             return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":"/"}))
            
#     else:
#         # Return an 'invalid login' error message.
#         if "js" in request.POST.keys():
#             if len(User.objects.filter(username=request.POST['username'])) == 0:
#                 return HttpResponse("inv_user")
#             return HttpResponse("inv_pass")
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'Invalid Login.', "text1":'Click here to go to home page.',"link":'/'}))
    
    
# #Called when a user clicks logout button.
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def logout_do(request):
#     logout(request)
#     redirect_url = "/"
#     if 'redirect_url' in request.POST.keys():
#         redirect_url = request.POST['redirect_url']
#     return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":redirect_url}))
    
# @login_required(login_url='/login_do/')
# def profile(request):
    
#     try:
#         pcuserid = request.GET['id']
#         if pcuserid == request.user.pcuser.pk:
#             return HttpResponse(jinja_environ.get_template('profile.html').render({"pcuser":request.user.pcuser, "profiler":request.user.pcuser}))
#         else:
#             return HttpResponse(jinja_environ.get_template('profile.html').render({"pcuser":request.user.pcuser, "profiler":request.user.pcuser}))
#     except:
#         return HttpResponseForbidden("You can't view someone else's details")


# #Calls the edit profile page. The autofill data is sent too.
# @login_required(login_url='/login_do/')
# def edit_profile_page(request):
#     if not request.user.is_authenticated():
#         return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))
#     pcuserid = request.GET['id']
#     return HttpResponse(jinja_environ.get_template('edit_profile.html').render({"pcuser":request.user.pcuser}))

# #Edit profile function. Called after a user presses done in edit profile. New data is requested from frontend and stored.
# @csrf_exempt
# @login_required(login_url='/login_do/')
# def edit_profile(request):
#     if not request.user.is_authenticated():
#         return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))


#     new_photo = request.FILES.get('photo',False)
#     if(new_photo):
#         request.user.pcuser.photo = new_photo
#     request.user.pcuser.gender = request.POST['gender']
#     request.user.pcuser.phone = request.POST['phone']
#     request.user.pcuser.email = request.POST['email']
#     request.user.pcuser.location = request.POST['location']
#     request.user.first_name = request.POST['first_name']
#     request.user.last_name = request.POST['last_name']
    
#     request.user.pcuser.save()
    
#     request.user.save()
    
#     return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
#                                                                           "text":'Profile edit successful.',"text1":'Click here to view the profile.',"link":'/profile/?id='+ str(request.user.pcuser.id)}))

# #Forgot Password page call function.
# def forgot_pass_page(request):
#     if request.user.is_authenticated():
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
#                                                                               "text":'<p>Please log out before requesting reset in password.</p>\
#                                                                                   <p>Click OK to go to the homepage</p>',"link":'/'}))
#     return HttpResponse(jinja_environ.get_template('forgot_password.html').render({"pcuser":None}))
# >>>>>>> Added User's Display Picture in profile


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
