from django.contrib import messages
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.




def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'Your Registration Complete')
            return redirect('account:login')
        
        else:
            messages.warning(request, 'Registration Failed.')
            return redirect('account:register')


    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'account/register.html', context)



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Logged in successfully as {user}')
                return redirect('todo:todo-list')
            else:
                messages.warning(request, 'Wrong Username or Password!')
                return redirect('account:login')
    
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'account/login.html', context)
    


def user_logout(request):
    logout(request)
    messages.success(request, "you logged out")
    return redirect('todo:todo-list')
    

def user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        if request.method == 'GET':
            form = ProfileForm(instance=user)
            return render(request, 'account/user_profile.html', {'user': user, 'form': form})
        
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('account:profile')
        
    else:
        return redirect('home:home')