
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
# from webhub import views as webhub_view


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

