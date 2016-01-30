from django.contrib.auth.views import AuthenticationForm
from django.views.generic.edit import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = '/'