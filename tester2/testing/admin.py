from django.contrib import admin
from testing.models import Answer, Question, Session, Test
from question_types.answers_forms.numeric import NumericModelForm

class QuestionAdmin(admin.ModelAdmin):
    form = NumericModelForm

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Session)
admin.site.register(Test)