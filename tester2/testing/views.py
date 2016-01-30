from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView
from testing.models import Question, Session, User, Test
import datetime


class HomeView(TemplateView):
    template_name = 'testing/index.html'


class PassingTestView(ListView):
    context_object_name = 'context_object'
    template_name = 'testing/passing_test.html'

    def get_context_data(self, **kwargs):
        context = super(PassingTestView, self).get_context_data(**kwargs)
        test = get_object_or_404(Test, self.kwargs['test_id'])
        session = Session(self.request.user, test, datetime.datetime.now())
        session.save()
        context['questions'] = Question.objects.filter(test=self.kwargs['test_pk'])
        context['session_pk'] = session.pk
        return context


class AnswerProcessingView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            #todo доработать обработку ответов
            return JsonResponse({})