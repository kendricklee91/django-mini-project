from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'accounts/password_change.html'), name = 'password_change'),
    path('password_chagne/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'), name = 'password_change_done')
]
