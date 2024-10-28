from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

login_required
def profile(request):
  profile = request.user.profile
  return render(request, 'User/profile.html', {'profile': profile})

login_required
def edit_profile(request):
  profile = request.user.profile
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      form.save()
      return redirect('profile')
  else:
    form = ProfileForm(instance=profile)
  return render(request, 'User/edit_profile.html', {'form': form})
