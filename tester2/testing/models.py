from django.contrib.auth.models import User
from django.db import models
from questions.settings import QuestionTypesManager


class Test(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', blank=True)
    time_limit = models.BooleanField(verbose_name='Ограничение по времени', default=False)
    duration = models.PositiveIntegerField(verbose_name='Продолжительность(мин.)')
    active = models.BooleanField(verbose_name='Тест активен')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'


class Question(models.Model):
    test = models.ForeignKey(verbose_name='Тест', to=Test)
    type = models.CharField(verbose_name='Тип теста', choices=QuestionTypesManager.get_question_types_choices(), max_length=250)
    text = models.TextField(verbose_name='Текст вопроса')
    answers = models.TextField(verbose_name='JSON с ответами') # Кодирование ответов зависит от типа вопроса

    def __str__(self):
        return self.text[:150]

    class Meta:
        verbose_name = 'вопрос теста'
        verbose_name_plural = 'вопросы теста'

    def bind_answer_form(self):
        self.answer_form = QuestionTypesManager.get_form_class_by_question_type(self.type)(self.answers)
        return self


class Session(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь', to=User)
    test = models.ForeignKey(verbose_name='Тест', to=Test)
    start_time = models.DateTimeField(verbose_name='Время начала')

    class Meta:
        verbose_name = 'сеанс тестирования'
        verbose_name_plural = 'сеанс тестирования'


class Answer(models.Model):
    session = models.ForeignKey(verbose_name='Сеанс', to=Session)
    question = models.ForeignKey(verbose_name='Тест', to=Question)
    correct = models.BooleanField(verbose_name='Ответ верный')

    def __str__(self):
        return "{user_name}: {question}".format(question=self.question.text[:150], user_name=self.session.user.username)

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'