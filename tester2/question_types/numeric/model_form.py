import json
from django import forms
from testing.models import Question


class NumericModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'text', 'answer', 'precision']

    answer = forms.FloatField(label='правильный ответ', required=True)
    precision = forms.FloatField(label='допустимая погрешность', required=True)

    def clean(self):
        super(NumericModelForm, self).clean()
        self.instance.type = 'NUMERIC'
        data = {}

        try:
            data['answer'] = self.cleaned_data['answer']
        except KeyError:
            pass

        try:
            data['precision'] = self.cleaned_data['precision']
        except KeyError:
            pass

        self.instance.answers = json.dumps(data)


FORM_CLASS = NumericModelForm