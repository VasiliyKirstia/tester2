from django.conf.urls import url
from testing.views import HomeView, PassingTestView, AnswerProcessingView, QuestionCreateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^passing_test/(?P<test_pk>\d+)/$', PassingTestView.as_view(), name='passing_test'),
    url(r'^answer_processing/$', AnswerProcessingView.as_view(), name='answer_processing'),
    url(r'^question_type_selection/$', QuestionCreateView.get, name='question_type_selection'),
    url(r'^question_create/(?P<question_type>["A"-"Z",0-9,"_"]+)/$', QuestionCreateView.as_view(), name='question_create'),
]