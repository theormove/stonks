from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateFrom

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
	else:	
		form = UserRegisterForm()
	return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		form = ProfileUpdateFrom(request.POST, instance = request.user.profile)
		if form.is_valid():
			#profile  = form.save(commit = False)
			#profile.user  = request.user
			form.save()
			return redirect('profile')
	else:
		form = ProfileUpdateFrom(instance = request.user.profile)		
	return render(request, 'users/profile.html',{'form':form})