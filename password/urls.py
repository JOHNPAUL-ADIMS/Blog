from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from .views import PasswordChangeView, PasswordResetDoneView
from django. urls import reverse_lazy
#from django .contrib.auth import views as auth_views


urlpatterns = [
    path('password', PasswordChangeView.as_view(), name='password_change'),
    path('password/done/',PasswordResetDoneView.as_view(), name='password_reset'),
]
