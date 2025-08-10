from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User  # Make sure you have this import

def insertuser(request):
    
    if request.method == 'POST':
        vname = request.POST.get('uname')
        vemail = request.POST.get('uemail')
        vnumber = request.POST.get('unumber')
        vpassword = request.POST.get('upassword')
        
        us = User(uname=vname, uemail=vemail, unumber=vnumber, upassword=vpassword)
        us.save()
        messages.success(request, 'Account created successfully')
        return render(request, 'user/profile.html')
    return redirect('signup')  # Redirect if not POST request

def loginuser(request):
   if request.method == 'POST':
        vemail = request.POST.get('email')
        vpassword = request.POST.get('password')
        
        try:
            # This assumes you've set up your User model correctly
            user = User.objects.get(uemail=vemail, upassword=vpassword)
            if user is None:
                login(request, user)
                return render(request, 'user/profile.html')
        except User.DoesNotExist:
            messages.error(request, 'Bad credentials')
        
        return render(request, 'register/signin.html')
   return redirect('login')
    
    
   """
   def loginuser(request):
    if request.method == 'POST':
        vemail = request.POST.get['email']
        vpassword = request.POST.get['password']
        
        # Use Django's authenticate
        user = authenticate(request, uemail=vemail, upassword=vpassword)
        user= True
        
        if user:
            login(request, user)
            return render(request, 'uprofile/profile.html')
        else:
            messages.error(request, 'Bad credentials')
            return render(request, 'register/signin.html')
    return redirect('login')
  """  
   
     