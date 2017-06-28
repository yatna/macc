import smtplib
import uuid

import jinja2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jinja2.ext import loopcontrols
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from webhub.checker import check
from webhub.models import *
from webhub.serializers import *
from webhub import views as webhub_view

# SMTP port for sending emails
SMTP_PORT = 465

#link for the localhost
website = "http://systerspcweb.herokuapp.com/"

jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['ui']), extensions=[loopcontrols])

#apis for malaria begin here
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
#List all pcusers, or create a new pcuser.
@api_view(['GET', 'POST'])
def pcuser_list(request):
    if request.method == 'GET':
        pcuser = Pcuser.objects.all()
        serializer = PcuserSerializer(pcuser, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PcuserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Retrieve, update or delete a pcuser instance.
@api_view(['GET', 'PUT', 'DELETE'])
def pcuser_detail(request, pk):
    try:
        pcuser = Pcuser.objects.get(pk=pk)
    except Pcuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PcuserSerializer(pcuser)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PcuserSerializer(pcuser, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pcuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#Calls index page
def index(request):
    return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))
    
#Calls dashboard wish is shown after a user is logged in
def dashboard(request):
    
    retval = check(request)
    if retval != None:
        return retval
    
    template_values = {'pcuser' : request.user.pcuser,
                    }
    return HttpResponse(jinja_environ.get_template('dashboard.html').render(template_values)) 

#Called when a user clicks login button. 
@csrf_exempt
def login_do(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            if 'redirect' in request.POST.keys():
                return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":request.POST['redirect'].replace("!!__!!","&")}))
            return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":"/"}))
            
    else:
        # Return an 'invalid login' error message.
        if "js" in request.POST.keys():
            if len(User.objects.filter(username=request.POST['username'])) == 0:
                return HttpResponse("inv_user")
            return HttpResponse("inv_pass")
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Invalid Login.', "text1":'Click here to go to home page.',"link":'/'}))
    
    
#Called when a user clicks logout button.
def logout_do(request):
    logout(request)
    redirect_url = "/"
    if 'redirect_url' in request.POST.keys():
        redirect_url = request.POST['redirect_url']
    return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":redirect_url}))
    
    
def profile(request):
    
    try:
        pcuserid = request.POST['id']
        if pcuserid == request.user.pcuser.pk:
            return HttpResponse(jinja_environ.get_template('profile.html').render({"pcuser":request.user.pcuser, "profiler":request.user.pcuser}))
        else:
            return HttpResponse(jinja_environ.get_template('profile.html').render({"pcuser":request.user.pcuser, "profiler":Pcuser.objects.get(pk=pcuserid)}))
    except:
        return HttpResponse(jinja_environ.get_template('profile.html').render({"pcuser":request.user.pcuser, "profiler":request.user.pcuser}))


#Calls the edit profile page. The autofill data is sent too.
def edit_profile_page(request):
    if not request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))
    pcuserid = request.POST['id']
    return HttpResponse(jinja_environ.get_template('edit_profile.html').render({"pcuser":Pcuser.objects.get(pk=pcuserid)}))

#Edit profile function. Called after a user presses done in edit profile. New data is requested from frontend and stored.
@csrf_exempt
def edit_profile(request):
    if not request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))

    
    #To remove profile picture
    if 'reset_image' in request.POST.keys():
        request.user.pcuser.image = "http://vfcstatic.r.worldssl.net/assets/car_icon-e0df962a717a5db6ebc8b37e80b05713.png"
        if str(request.user.pcuser.imageobj) != '':
            path = '/vagrant/submit/media/propics/' + request.user.username + request.user.pcuser.imageobj.url[request.user.pcuser.imageobj.url.rfind('.'):]
            if os.path.isfile(path):
                os.remove(path)
        request.user.pcuser.save()
        return edit_profile_page(request)
    
    
    if 'image' in request.FILES.keys():
        #delete old file
        if str(request.user.pcuser.imageobj) != '':
            path = '/vagrant/submit/media/propics/' + request.user.username + ".jpg"
            if os.path.isfile(path):
                os.remove(path)
        request.user.pcuser.imageobj = request.FILES['image']
        request.user.pcuser.image = '/static/' + request.user.username + ".jpg"
    
    
    
    
    
    
    request.user.pcuser.gender = request.POST['gender']
    request.user.pcuser.phone = request.POST['phone']
    request.user.pcuser.email = request.POST['email']
    request.user.pcuser.location = request.POST['location']
    request.user.first_name = request.POST['first_name']
    request.user.last_name = request.POST['last_name']
    
    request.user.pcuser.save()
    
    request.user.save()
    
    return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                          "text":'Profile edit successful.',"text1":'Click here to view the profile.',"link":'/profile/?id='+ str(request.user.pcuser.id)}))

#Forgot Password page call function.
def forgot_pass_page(request):
    if request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                              "text":'<p>Please log out before requesting reset in password.</p>\
                                                                                  <p>Click OK to go to the homepage</p>',"link":'/'}))
    return HttpResponse(jinja_environ.get_template('forgot_password.html').render({"pcuser":None}))




#Called when the user clicks forgot password after the data is validated. This sends a verification mail to the user.
@csrf_exempt
def forgot_pass(request):
    if request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>Please log out in order to request for a password reset.</p>\
                                                                                  <p>Please go back or click here to go to the homepage</p>',"link":'/'}))
    if 'username' not in request.POST.keys() or 'email' not in request.POST.keys():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Invalid Request. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
    user = User.objects.filter(username=request.POST['username'])
    if len(user) == 0:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'User Does not exist. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
    user = user[0]
    if user.email != request.POST['email']:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Invalid email. Please go back or',"text1":'click here to go to the homepage',"link":'/'}))
    user.pcuser.reset_pass = uuid.uuid4().hex
    user.pcuser.save()
    
    subject = "Password Reset Request"
    msg = 'Subject: %s \n\nYou have requested for a password reset on Mobile App Control Center\n\
    Please click on the following link (or copy paste in your browser) to reset your password.\n\n\
    %s/reset_pass_page/?reset_pass=%s&email=%s\n\n\
    If you have not requested for a reset of password, please ignore.' % (subject, website, user.pcuser.reset_pass, user.email)
    
    x = send_email(msg, user.email)
    if x[0] == 0:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Could not process request, please try again later by going back or',"text1":'clicking here to go to the homepage', "link":'/'}))
    else:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>An email has been sent to your regestered email address.</p>\
                                                                                  <p>Check your email and click on the link to reset your password.</p>',"text1":'<p>Click here to go to the homepage</p>',"link":'/'}))
    

    
#Reset Password page call function.
@csrf_exempt
def reset_pass_page(request):
    if request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                              "text":'<p>Please log out before requesting reset in password.</p>',"text1":'<p>Click here to go to the homepage</p>',"link":'/'}))
    if "reset_pass" not in request.POST.keys() or 'email' not in request.POST.keys():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>Invalid Request</p>',"text1":'Click here to go to the homepage</p>', "link":'/'}))
    reset_pass = request.POST['reset_pass']
    if reset_pass == "":
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>Invalid Request</p>',"text1":'<p>click here to go to the homepage</p>', "link":'/'}))
    user = Pcuser.objects.filter(reset_pass=reset_pass)
    if len(user)==0:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                                "text":'Invalid Request.',"text1":'Please go back or click here to go to the homepage',"link":'/'}))
    
    user = user[0].user
    
    if user.email != request.POST['email']:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                                "text":'Invalid Email.',"text1":'Please go back or click here to go to the homepage',"link":'/'}))
    return HttpResponse(jinja_environ.get_template('reset_password.html').render({'pcuser':None, 'reset_pass':reset_pass}))



#Called when the user clicks change password button. Checks if the previous password is valid or not.
@csrf_exempt
def change_pass(request):
    if "reset_pass" in request.POST.keys():
        reset_pass = request.POST['reset_pass']
        if reset_pass == "":
            return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                                  "text":'<p>Invalid Request</p>', "text1":'<p>click here to go to the homepage</p>',"link":'/'}))
        user = Pcuser.objects.filter(reset_pass=reset_pass)
        if len(user)==0 or 'pass' not in request.Policies.keys():
            return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                                  "text":'Invalid Request.',"text1":'Please go back or click here to go to the homepage',"link":'/'}))
        user = user[0].user
        user.set_password(request.POST['pass'])
        user.save()
        user.pcuser.reset_pass = ""
        user.pcuser.save()
        logout(request)
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Password Changed.',"text1":'Please click here to go to the homepage and log in again.',"link":'/logout_do/'}))
    else:
        retval = check(request)
        if retval != None:
            return retval
        if "pass" not in request.POST.keys() or "oldpass" not in request.POST.keys():
            return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                                  "text":'Invalid Request.', "text1":'Please go back or click here to go to the homepage',"link":'/'}))
        if not request.user.check_password(request.POST['oldpass']):
            return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                                  "text":'Invalid Old Password.',"text1":'Click here to go to the homepage',"link":'/'}))
        request.user.set_password(request.POST['pass'])
        request.user.save()
        logout(request)
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Password Changed.',"text1":'Please click here to go to the homepage and log in again.',"link":'/logout_do/'}))
    
    
    
#Change password page call function    
def change_pass_page(request):
    retval = check(request)
    if retval != None:
        return retval
    return HttpResponse(jinja_environ.get_template('change_password.html').render({"pcuser":request.user.pcuser}))
        

#called when user wishes to go to the about PeaceCorps
def aboutPC(request):
    return HttpResponse(jinja_environ.get_template('aboutPC.html').render({"pcuser":None}))  

#called when user wishes to go to the Policies
def policies(request):
    return HttpResponse(jinja_environ.get_template('policies.html').render({"pcuser":None}))  

#called when user wishes to go to the Important details
def details(request):
    return HttpResponse(jinja_environ.get_template('details.html').render({"pcuser":None}))  

#called when user wishes to go to the Help
def helpPC(request):
    return HttpResponse(jinja_environ.get_template('helpPC.html').render({"pcuser":None}))  

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

