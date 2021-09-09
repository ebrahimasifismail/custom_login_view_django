from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


from accounts.forms import LoginForm
# Create your views here.

def home(request):
    return HttpResponse("Hello, World!!!")

def nurse_view(request):
    return HttpResponse("Hello, Nurse!!!")

def doctor_view(request):
    return HttpResponse("Hello, Doctor!!!")

def login_failure_view(request):
    return HttpResponse("Hello, User!!!\n Please use user specific login pages ")


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # your template
    from_class = LoginForm # your form

    def get_success_url(self):
        '''Here the part where you can implement your login logic'''
        # import pdb; pdb.set_trace()

        auth_user = self.request.user 
        if auth_user.user_type == 'NURS':
            return reverse_lazy("accounts:nurse")
        elif auth_user.user_type == 'DOCT':
            return reverse_lazy("accounts:doctor")
        else:
            return reverse_lazy("accounts:failure")
        
