from django.conf.urls import url
from accounts.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
]