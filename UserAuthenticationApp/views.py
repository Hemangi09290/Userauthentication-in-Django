from webbrowser import get
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import smtplib

# Create your views here.

# Initialising database,auth and firebase for further use
#firebase=pyrebase.initialize_app(config)
#authe = firebase.auth()
#database=firebase.database()
#user = User.objects.create_user('Pranali', 'Pranali@test.com', 'pranalipassword')
def signIn(request):
	return render(request,"Login.html")
def home(request):
	return render(request,"Home.html")

def postsignIn(request):
	email=request.POST.get('email')
	pasw=request.POST.get('pass')
	user = User.objects.get(email=email)
	#user = User.objects.all().filter(email=email)
	#user= authenticate(request, email=email, password=pasw)
    # user = authe.sign_in_with_email_and_password(email,pasw)
	if user is not None:
		login(request, user)
		print(request)
		#print(user('idToken'))
		session_id=str(user.id)
		request.session['uid']=str(session_id)
		return render(request,"Home.html",{"email":email})
	else:
		message="Invalid Credentials!!Please ChecK your Data"
		return render(request,"Login.html",{"message":message})
		

def logout(request):
	try:
		del request.session['uid']
	except:
		pass
	return render(request,"Login.html")

def signUp(request):
	return render(request,"Registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user=User.objects.create_user(name,email,passs)
        uid = user.id
        idtoken = request.session.get('uid', None)
        print(uid)
    except:
        return render(request, 'Registration.html')
    return render(request, 'Login.html')
	
def sendemail(request):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('barvehemangi09@gmail.com', 'Tkdir_9290')
	server.sendmail('barvehemangi09@gmail.com', 'mehtahemangi09@gmail.com', 'hello its msg from python code')
	print('Mail sent')
	return render(request,"sendEmail.html")
