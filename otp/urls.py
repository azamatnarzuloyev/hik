from django.urls import path
from .views import (SendPhoneOTP, 
					ValidateOTP, 
					Register, 
					LoginAPI, 
				
				
					UserView,
					ValidatePhoneLogin,
					ValidateloginOtp,
					)
from knox import views as knox_views

urlpatterns = [

	path('sendotp/', SendPhoneOTP.as_view()),
	path('validateotp/', ValidateOTP.as_view()),
	path('register/', Register.as_view()),

	path('login/', LoginAPI.as_view()),
	# path('logout/', knox_views.LogoutView.as_view()),
	# path('change_password/<int:pk>/', ChangePasswordView.as_view()),

	path('user_profile/', UserView.as_view()),
	# path('update_profile/<int:pk>/', UpdateProfileView.as_view()),

	path('ValidatePhoneLogin/', ValidatePhoneLogin.as_view()),
	path('alidateloginOtp/', ValidateloginOtp.as_view()),
	# path('change_forgot_password/', ForgotPasswordChange.as_view())

]