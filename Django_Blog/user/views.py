from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.


def SignupView(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})





def Profile(request):

    return render(request, template_name='user/profile.html')


