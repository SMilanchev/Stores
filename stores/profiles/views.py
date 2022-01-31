from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from stores.profiles.forms import EditProfileFrom
from stores.profiles.models import Profile


@login_required
def details_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/details_profile.html', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EditProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileFrom(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)


