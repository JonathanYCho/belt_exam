from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
	print User.objects.all()
	context = {
		'all_users': User.objects.all()
	}
	return render(request, 'first_app/index.html', context)

def create(request):
	if request.method == "POST":
		print request.POST
		users = User.objects.create(username = request.POST['username'], password = request.POST['password'])
		
	return render(request, 'first_app/travels.html')
