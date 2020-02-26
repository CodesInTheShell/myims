from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .models import *
from .forms import *


@require_http_methods(["POST"])
def user_login(request):

	context = {}

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print('user: ', user)
		if user:
			login(request, user)
			return redirect('dashboard')
		else:
			context['error'] = 'Invalid credentials!'
			return render(request, 'index.html', context=context)

def user_logout(request):
	logout(request)
	# return redirect('index')
	return HttpResponseRedirect(reverse('index'))




