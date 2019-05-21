from django.urls import path, include
from usuarios.views import RegistrarUsuarioView

urlpatterns = [ 
	path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
	#path('login', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
	#path('logout', 'django.contrib.auth.views.logout_then_login', {'login_url':'/login/'}, name='logout')

]