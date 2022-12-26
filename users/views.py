from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signUpPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect("HomePage")
        except:
            messages.error(request,"Password Mismatch or User Already Exists.")
            return redirect("RegisterPage")
        # try:
        #     if form.is_valid:
        #         form.save()
        #         return redirect('HomePage');
        # except:
            
        #     messages.error(request, "Invalid Credentials")
        #     return redirect("RegisterPage")
    context = {'form': form}
    return render(request, 'users/sign_up.html', context)
def logoutPage(request):
    logout(request)
    return redirect("HomePage")
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            # try:
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('HomePage')
                else:
                    messages.error(request,"Incorrect Password")
                    return redirect("LoginPage")
            # except:
            #     messages.error(request,"Incorrect Password")
            #     return redirect("LoginPage")
        else:
            messages.error(request,"User does not exists.")
            return redirect("LoginPage")
        
    return render(request, 'users/login.html')