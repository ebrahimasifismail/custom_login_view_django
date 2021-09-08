from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


from accounts.forms import LoginForm
# Create your views here.

def home(request):
    return HttpResponse("Hello, World!!!")


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # your template
    from_class = LoginForm # your form

    def get_success_url(self):
        '''Here the part where you can implement your login logic'''
        import pdb; pdb.set_trace()
        # now = timezone.now()
        # # Get current day date object
        # # like: 12/02/2019 00:00:00
        # today = now.replace(minute=0).replace(second=0).replace(microsecond=0)
        # # Get the client from the user object
        # client = self.request.user.cli
        # # Get all the user today's logins and count them
        # client_logins = models.ClientLogins.objects.filter(
        #     client=client,
        #     date__gte=today,
        #     date__lte=today + timedelta(days=1)
        # ).count()
        # if client_logins < 1:  # Or: if not client_logins:
        #     # create a login tracker record
        #     models.ClientLogins.objects.create(
        #         client=client,
        #         date=now  # Store the date where the user logged in the website
        #     )
        #     return reverse_lazy('FIRST_LOGIN_REDIRECT_URL')
        # Or redirect to: settings.LOGIN_REDIRECT_URL
        return reverse_lazy("accounts:home")
