from django.shortcuts import render

def profile(request):
  profile = request.user.profile
  return render(request, 'User/profile.html', {'profile': profile})
