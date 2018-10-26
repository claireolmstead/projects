from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/home.html')
def sports(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/sports.html')
def politics(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/politics.html')
def business(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/business.html')
def profile(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/profile.html')
def makeAccount(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/make-account.html')
def signin(request):
	return render(request, '/Users/Dannyniquette/Desktop/mySite/myApp/templates/signin.html')
	
	
