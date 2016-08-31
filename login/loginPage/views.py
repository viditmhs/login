from django.shortcuts import render

from django.http import HttpResponse

def start(request):
    return render(request, 'loginPage/loginPage.html', "")

def loginStart(request):
	print(request)
	return render(request, 'loginPage/loginSuccess.html', "")
