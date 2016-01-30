from django.conf.urls import url
from testing.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view()),
]