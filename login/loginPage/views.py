from django.shortcuts import render

from django.http import HttpResponse

import Logger as log

from .models import UserDetail


def start(request):
    return render(request, 'loginPage/loginPage.html', "")

def loginStart(request):
	userLoginId = request.POST.get('loginId', '')
	userPass = request.POST.get('loginPass', '')

	# Check if this user exist in the data base
	users = UserDetail.objects.filter(login_id=userLoginId).values()
	if(len(users)>0 ):
		for u in users:
			print(u)
			if(u['login_challenge'] == userPass):
				return render(request, 'loginPage/loginSuccess.html', {'user_login_id' : userLoginId})
			else:
				return render(request, 'loginPage/loginUnsuccess.html', {'user_login_id' : userLoginId})

	else:
		return render(request, 'loginPage/loginUnsuccess.html', {'user_login_id' : userLoginId})
