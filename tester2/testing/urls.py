from django.conf.urls import url
from testing.views import HomeView, PassingTestView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^passing_test/(?P<test_pk>\d+)/$', PassingTestView.as_view(), name='passing_test'),
]