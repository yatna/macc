
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status, viewsets

from rest_framework.decorators import api_view

from django.shortcuts import render

from webhub.serializers import *
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from profiles.models import Pcuser
from django.http import Http404
from django.http import HttpResponseRedirect
from webhub import views as webhub_view


# SMTP port for sending emails
SMTP_PORT = 465

#link for the localhost
website = "http://systerspcweb.herokuapp.com/"

#apis for malaria begin here
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ListUsers(APIView):

    def get(self, request, format=None):
        pcuser = Pcuser.objects.all()
        serializer = PcuserSerializer(pcuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PcuserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PcuserDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Pcuser.objects.get(pk=pk)
        except Pcuser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PcuserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PcuserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# <<<<<<< HEAD
# =======
    
    
    
#     request.user.pcuser.photo =request.FILES['photo']
    
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




# #Called when the user clicks forgot password after the data is validated. This sends a verification mail to the user.
# @csrf_exempt
# def forgot_pass(request):
#     if request.user.is_authenticated():
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'<p>Please log out in order to request for a password reset.</p>\
#                                                                                   <p>Please go back or click here to go to the homepage</p>',"link":'/'}))
#     if 'username' not in request.POST.keys() or 'email' not in request.POST.keys():
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'Invalid Request. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
#     user = User.objects.filter(username=request.POST['username'])
#     if len(user) == 0:
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'User Does not exist. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
#     user = user[0]
#     if user.email != request.POST['email']:
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'Invalid email. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
#     user.pcuser.reset_pass = uuid.uuid4().hex
#     user.pcuser.save()
    
#     subject = "Password Reset Request"
#     msg = 'Subject: %s \n\nYou have requested for a password reset on Mobile App Control Center\n\
#     Please click on the following link (or copy paste in your browser) to reset your password.\n\n\
#     %s/reset_pass_page/?reset_pass=%s&email=%s\n\n\
#     If you have not requested for a reset of password, please ignore.' % (subject, website, user.pcuser.reset_pass, user.email)
    
#     x = send_email(msg, user.email)
#     if x[0] == 0:
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'Could not process request, please try again later by going back or',"text1":'clicking here to go to the homepage', "link":'/'}))
#     else:
#         return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
#                                                                               "text":'<p>An email has been sent to your regestered email address.</p>\
#                                                                                   <p>Check your email and click on the link to reset your password.</p>',"text1":'<p>Click here to go to the homepage</p>',"link":'/'}))
    
# >>>>>>> Added User's Display Picture in profile

class DashboardView(LoginRequiredMixin,TemplateView):

    template_name = 'ui/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


class AboutPC(TemplateView):
    
    template_name = 'ui/aboutPC.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPC, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


class Policies(TemplateView):
    
    template_name = 'ui/policies.html'

    def get_context_data(self, **kwargs):
        context = super(Policies, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


class Details(TemplateView):
    
    template_name = 'ui/details.html'

    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


class HelpPC(TemplateView):
    
    template_name = 'ui/helpPC.html'

    def get_context_data(self, **kwargs):
        context = super(HelpPC, self).get_context_data(*kwargs)
        try:
            context['pcuser'] = self.request.user.pcuser
        except:
            context['pcuser'] = None
        return context


def login_real(request):
    print("yolo")
    return render(request,"login_real.html")

def login_social(request):
    username= request.POST['uname']
    user=User.objects.get(username=username)
    print(user.email)
    print(username)
    gender="Restricted"
    location= "N.A"
    phone="N.A"
    num_results = Pcuser.objects.filter(user=user).count()
    if num_results ==0:
           
        print("num rsults")
        print(num_results)
    
        entry = Pcuser(user=user, phone=phone, gender=gender, location=location, verified = uuid.uuid4().hex)      
        entry.save()
    else:
        pcuser=Pcuser.objects.get(user=user)
        entry=pcuser

    
    if 'redirect' in request.POST.keys():
        return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":request.POST['redirect'].replace("!!__!!","&")}))
    return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":"/"}))

