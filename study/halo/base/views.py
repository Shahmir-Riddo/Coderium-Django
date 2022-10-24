from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email exists")

        elif User.objects.filter(username=username).exists():

            messages.error(request, "Username exists")

        else:

            user = User.objects.create_user(username=username, email=email, password= password)
            user.save()
            messages.info(request, "Registered Successfully")
            return redirect('/login/')

  
      


            
        
    return render(request, 'signup.html')


    

def login(request):
    

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

   
        user = authenticate(request, username=username, password=password)
        if user is not None:

            auth.login(request, user)
            return redirect("index")

    else:
        messages.info(request,  "Invalid Info")
        return render(request, "login.html")



    
    
   

 
def logout(request):

    auth.logout(request)
    redirect(request, "/")

def profile(request):
    bio = request.POST.get('bio')
    context = {
        "maleimg": "https://img.icons8.com/color/344/circled-user-male-skin-type-6--v1.png",
        "femaleimg": "https://img.icons8.com/color/344/circled-user-female-skin-type-7--v1.png",
        "bios": bio
    }
    
    return render(request,'profile.html', context)


def editprofile(request):
    if request.method == 'POST':

        bio = request.POST.get('bio')
    context = {
            "maleimg": "https://img.icons8.com/color/344/circled-user-male-skin-type-6--v1.png",
            "femaleimg": "https://img.icons8.com/color/344/circled-user-female-skin-type-7--v1.png",
            "bios": "bio",
        }
        
        

   
    
  
    
   
        
    
    
      
    return render(request, 'editprofile.html', context)


def htmleditor(request):
    return render(request, "htmleditor.html")

def error(request):
    return render(request, "error.html")

def loginerror(request):
    return render(request, "loginerror.html")