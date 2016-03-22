from django import forms
from testing.models import Question


class NumericModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'text', 'answer', 'precision']

    answer = forms.FloatField(label='правильный ответ')
    precision = forms.FloatField(label='допустимая погрешность')

    def clean(self):
        super(NumericModelForm, self).clean()
        self.instance.answers = '{"answer":{answer},"precision":{precision}}'.format(
            answer=self.cleaned_data['answer'],
            precision=self.cleaned_data['precision']
        )

FORM_CLASS = NumericModelForm