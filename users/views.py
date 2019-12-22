from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm ....it is inherited to UserRegisterForm in forms.py to add more field..so it is useless now
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.You can now login !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    messages.info(request, f'You must login first!')
    return render(request, 'users/profile.html')  # for decorator to redirect login path
