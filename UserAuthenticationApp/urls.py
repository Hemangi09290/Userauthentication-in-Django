
from django.urls import path
from . import views

urlpatterns = [
	
	# Here we are assigning the path of our url
	path('', views.signIn, name="login"),
	path('postsignIn/', views.postsignIn),
	path('signUp/', views.signUp, name="signup"),
	path('logout/', views.logout, name="log"),
	path('postsignUp/', views.postsignUp),
]
