from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.
def list(request):
    return render(request, 'frontend/index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return render(request, 'frontend/index.html')
            else:
                return render(request, 'frontend/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'frontend/login.html', {'error_message': 'Invalid login'})
    return render(request, 'frontend/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return render(request, 'frontend/index.html')
    context = {
        "form": form,
    }
    return render(request, 'frontend/register.html', context)
