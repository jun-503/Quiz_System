from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.urls import reverse


from quiz.urls import urlpatterns

# Create your views here.
def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass']

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            quiz_view_url = reverse('quiz_view')
            return redirect(quiz_view_url)
        else:
            messages.error(request, "Bad Credentials! ")
            return redirect('/')
        
    return render(request, 'registration/login.html')

def signup(request):
    if request.method=="POST":
           # username = request.POST.get('username')
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            cPassword = request.POST['password2']

            if User.objects.filter(username=username):
                messages.error(request, "Username already exists ")
                return redirect('signup')
            
            if(User.objects.filter(email=email)):
                messages.error(request, "EMAIL already exists ") 
                return redirect('signup')
        
            if(len(username)>10):
                messages.error(request, "username must be 10 characters ") 
                return redirect('signup')

            myUser = User.objects.create_user(username,email,password)
            myUser.save()
            messages.success(request, "Your Account has been created successfully ")
            return redirect('signin')
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('signup')  # Redirect back to the signup page

    return render(request, 'registration/signup.html',{'messages': messages.get_messages(request)})
