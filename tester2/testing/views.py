import datetime
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.http.response import JsonResponse, Http404, HttpResponse
from django.shortcuts import render_to_response, render
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from question_types.types_manager import QuestionTypesManager
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

        context['question_types'] = [
            question.bind_answer_form() for question in Question.objects.filter(test=self.kwargs['test_pk'])
        ]

        context['session_pk'] = session.pk
        context['test_pk'] = self.kwargs['test_pk']
        return context


class AnswerProcessingView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            #todo нужно добавить какую-нибудь логику учитывающую истечение времени
            form_class = QuestionTypesManager.get_answer_form_class(request.POST['question_type'])
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


@method_decorator(csrf_exempt, name='dispatch')
class QuestionCreateView(View):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get('question_type', None) is None:
            return render_to_response(
                'testing/question_type_select.html',
                {'types_list': QuestionTypesManager.get_question_types_list()}
            )
        elif QuestionTypesManager.is_question_type_exist(self.kwargs.get('question_type')):
            form = QuestionTypesManager.get_model_form_class(self.kwargs.get('question_type'))()
            return render_to_response(
                'testing/question_create.html',
                {
                    'form': form,
                    'question_type': self.kwargs.get('question_type')
                }
            )
        else:
            raise Http404()

    def post(self, request, *args, **kwargs):
        if self.kwargs.get('question_type', None) is None:
            raise Http404()

        form = QuestionTypesManager.get_model_form_class(self.kwargs.get('question_type'))(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Вопрос добавлен успешно.")
        else:
            return render_to_response(
                'testing/question_create.html',
                {
                    'form': form,
                    'question_type': self.kwargs.get('question_type')
                }
            )
