from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .models import *
from .forms import *

# Create your views here.
def index(request):

	if request.user.is_authenticated:
		return redirect('dashboard')

	return render(request, 'index.html')

@login_required(login_url='/') #
def dashboard(request):
	context = {}

	user = request.user

	items = Item.objects.all()

	context = {
		'items': items,
		'user': user,
	}

	return render(request, 'dashboard.html', context)

@login_required(login_url='/')
def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)

		if form.is_valid():

			if not Item.objects.filter(sku=form.cleaned_data['sku']).exists():
				form.save()
				messages.add_message(request, messages.SUCCESS, 'Added new item {}'.format(form.cleaned_data['sku']))
				return render(request, 'add_new.html', {'form': form})
			else:
				messages.add_message(request, messages.ERROR, 'Error adding {}'.format(form.cleaned_data['sku']))
				return render(request, 'add_new.html', {'form': form})
		else:
			messages.add_message(request, messages.ERROR, 'Error adding {}, please check if sku already exist.'.format(form.data.get('sku', None)), extra_tags='danger')
			return render(request, 'add_new.html', {'form': form})
	else:
		form = ItemForm()
		return render(request, 'add_new.html', {'form': form})

@login_required(login_url='/')
def edit_item(request, pk):
	item = get_object_or_404(Item, pk=pk) #select from database

	if request.method == 'POST':
		form = ItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Saved')
			return render(request, 'edit_item.html', {'form': form})
	else:
		form = ItemForm(instance=item)
		return render(request, 'edit_item.html', {'form': form})

@login_required(login_url='/')
def delete_item(request, pk):

	Item.objects.filter(id=pk).delete()

	return redirect('dashboard')

@login_required(login_url='/')
def items(request):
	context = {}

	user = request.user

	items = Item.objects.all()

	context = {
		'items': items,
		'user': user,
	}

	return render(request, 'items.html', context)

def outgoing_item(request):
	return render(request, 'incoming_items.html', context)

def incoming_item(request):
	form = IncomingItemForm()
	return render(request, 'incoming_items.html', {'form': form})

