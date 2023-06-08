from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from youtify import settings

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    # path('forgot-password/', views.forgot_password, name='forgot_password'),
    # path('change-password/<hashid:uid>/', views.change_password, name='change_password')
]