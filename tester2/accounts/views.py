from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        print(self.kwargs)  # todo разобраться как получать параметр next
        if self.kwargs is not None and hasattr(self.kwargs, 'next'):
            return reverse_lazy(self.kwargs['next'])
        else: return reverse_lazy('testing:home')


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:login')
