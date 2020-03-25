from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateFrom
from django.forms.models import model_to_dict

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
		if form.is_valid() and request.user.profile.subscription_plan == "CATEGORIES":
			form.save()
			return redirect('profile')
		else:
			messages.add_message(request, messages.ERROR, 'Change your subscription plan to do that')
			return redirect('profile')
	else:
		form = ProfileUpdateFrom(instance = request.user.profile)		
	return render(request, 'users/profile.html',{'form':form})


@login_required
def subscriptions(request):
	if request.user.profile.subscription_plan == 'NONE':
		btn = "Subscribe"
	else:		
		btn = "Cancel"	
	if request.method == 'POST':
		if "Subscribe" in request.POST:
			request.user.profile.subscription_plan = "CATEGORIES"
			request.user.profile.save()
		else:
			request.user.profile.subscription_plan = "NONE"
			data = model_to_dict(request.user.profile)
			for field in data:
				if data[field] == False:
					setattr(request.user.profile, field, True)
			request.user.profile.save()	
		return redirect('subscriptions')
	buttons = {'btn':btn}	
	return render(request, 'users/subscriptions.html', buttons)
			