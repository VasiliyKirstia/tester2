from django import forms
from testing.models import Question


class SimpleChoiceModelForm(forms.ModelForm):
    class Meta:
        model=Question
        fields = ['test', 'text']


FORM_CLASS = SimpleChoiceModelForm
