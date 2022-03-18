from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from . forms import CustomUserCreationForm
# Create your views here.
def signUpPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('HomePage');
    context = {'form': form}
    return render(request, 'users/sign_up.html', context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        return redirect('HomePage')
    return render(request, 'users/login.html')