from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdate, UserUpdate
from django.contrib.auth.decorators import login_required

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




@login_required
def Profile(request):

    return render(request, 'user/profile.html')




@login_required
def Edit_Profile(request):
    if request.method == "POST":
        p_form = ProfileUpdate(request.POST, instance=request.user.profile)
        u_form = UserUpdate(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('profile')

    else:
        p_form = ProfileUpdate(instance=request.user.profile)
        u_form = UserUpdate(instance=request.user)

        print(request.user.username)
        print(request.user.profile.bio)

    context = {
        'p_form': p_form,
        'u_form': u_form
    }

    return render(request, 'user/profileedit.html', context)



