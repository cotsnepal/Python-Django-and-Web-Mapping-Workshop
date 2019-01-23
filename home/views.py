from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from . forms import ContactForm
def home(request):
	return render(request,'home/home.html')

def contact(request):
	if request.method== 'POST':
		form=ContactForm(request.POST)
		if form .is_valid():
			return HttpResponseRedirect(reverse('home'))
	else:
		form=ContactForm
	return render(request,'home/contact.html',{'form':form})

