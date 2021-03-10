from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def hello(request):
	msg = "Hello World"
	return HttpResponse(msg)

def Login(request):
	return render(request,'Login.html')

@csrf_exempt
def submit(request):
	name = request.POST.get('name')
	pas = request.POST.get('pass')
	if name == 'Gaurang' and pas == '1234':
		return render(request,'index.html')
def email(request):
	return render(request,'email1.html')


@csrf_exempt
def sendmail(request):
	a = request.POST.get('semail')
	b = request.POST.get('ssubject')
	c = request.POST.get('message')

	rec_list = [a,]
	email_from = settings.EMAIL_HOST_USER
	send_mail(b,c,email_from,rec_list)
	res = 'MailSend'
	return HttpResponse(res)