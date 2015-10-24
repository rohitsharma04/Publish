from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render,HttpResponseRedirect
from userauths.forms import LoginForm,SignupForm


def login_view(request):
	form = LoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		print form.cleaned_data['username']
		user = authenticate(username=username, password=password)
		login(request,user)
		return HttpResponseRedirect(reverse("user_home"))

	context = {'form':form}
	template = "userauths/login.html"
	return render(request,template,context)

def signup_view(request):
	form = SignupForm(request.POST or None)

	if form.is_valid():
		new_user = form.save(commit=False)
		new_user.save()
		return HttpResponseRedirect(reverse("login_view"))
	
	context = {'form':form}
	template = "userauths/signup.html"
	return render(request,template,context)	

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect(reverse('home'))