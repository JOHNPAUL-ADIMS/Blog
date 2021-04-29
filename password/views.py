from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django. urls import reverse_lazy

# Create your views here.


class PasswordChangeView(PasswordChangeView):
    template_name = 'password/password_change.html'
    success_url = reverse_lazy('password:password_change_done_view')


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password/password_reset_done.html'
