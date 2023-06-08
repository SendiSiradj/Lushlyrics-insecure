from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('change-password/<hashid:uid>/', views.change_password, name='change_password')
]