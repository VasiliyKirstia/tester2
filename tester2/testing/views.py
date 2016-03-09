import datetime

from django.http.response import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from questions.settings import QuestionTypesManager
from testing.models import Question, Session, Test, Answer


class HomeView(TemplateView):
    template_name = 'testing/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tests_list'] = Test.objects.all()
        return context


class PassingTestView(LoginRequiredMixin, TemplateView):
    template_name = 'testing/passing_test.html'

    def get_context_data(self, **kwargs):
        context = super(PassingTestView, self).get_context_data(**kwargs)

        session = Session.objects.create(
            user=self.request.user,
            test=get_object_or_404(Test, pk=self.kwargs['test_pk']),
            start_time=datetime.datetime.now()
        )

        context['questions'] = [
            question.bind_answer_form() for question in Question.objects.filter(test=self.kwargs['test_pk'])
        ]

        context['session_pk'] = session.pk
        context['test_pk'] = self.kwargs['test_pk']
        return context


class AnswerProcessingView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            #todo нужно добавить какую-нибудь логику учитывающую истечение времени
            form_class = QuestionTypesManager.get_form_class_by_question_type(request.POST['question_type'])
            form = form_class(Question.objects.get(pk=request.POST['question_pk']).answers, request.POST)
            if form.is_valid():
                Answer.objects.create(
                    session=get_object_or_404(Session, pk=request.POST['session_pk']),
                    question=get_object_or_404(Question, pk=request.POST['question_pk']),
                    correct=form.check_answers(),
                )
                return JsonResponse({'text':'ваш ответ {0}'.format('верный.' if form.check_answers() else 'не верный.')})
            else:
                return JsonResponse({'text':'форма не валидна'})
        else:
            raise Http404()
