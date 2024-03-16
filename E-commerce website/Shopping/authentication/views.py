from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

#from django.shortcuts import render,redirect,HttpResponse
#from django.contrib.auth.models import User
from django.views.generic import View
#from django.contrib import messages
#from django.template.loader import render_to_string
#from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
#from .utils import TokenGenerator,generate_token
#from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password not matched")
            return render(request,'auth/signup.html')

        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exist")

        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.save()
        return HttpResponse("User created",email)
    return render(request,"auth/signup.html")

def handlelogin(request):
    if request.method=="POST":
    #print('hello')
        username=request.POST['email']
        userpassword=request.POST['pass1']
        user=authenticate(request,username=username,password=userpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Username or password")
            message ='invalid username or password'
            #return render(request,'login.html',{'message':message})
            return redirect('/authentication/login/')

    return render(request,"auth/login.html")

def handlelogout(request):
    return redirect('/authentication/login')

