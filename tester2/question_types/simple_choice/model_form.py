from django import forms
from testing.models import Question
import json


class SimpleChoiceModelForm(forms.ModelForm):
    VARIANTS_COUNT = 10

    def __init__(self):
        for i in range(0, self.VARIANTS_COUNT):
            self.fields['variant_' + str(i)] = forms.CharField()
            self.fields['is_correct_' + str(i)] = forms.BooleanField(required=False, label='вариант {0} верный'.format(i))

    def clean(self):
        super(SimpleChoiceModelForm, self).clean()

        data = {'answers': []}
        for i in range(0,self.VARIANTS_COUNT):
            if self.cleaned_data['variant_' + str(i)] is not None:
                striped_string = str.strip(self.cleaned_data['variant_' + str(i)])
                if striped_string != "":
                    data['answers'].append({
                        "text": striped_string,
                        "correct": self.cleaned_data['is_correct_' + str(i)]
                    })

        self.instance.type = 'SIMPLE_CHOICE'
        self.instance.test = self.cleaned_data['test']
        self.instance.text = self.cleaned_data['text']
        self.instance.answers = json.dumps(data)

    class Meta:
        model=Question
        fields = ['test', 'text'] +\
                 ['variant_' + str(i) for i in range(0,SimpleChoiceModelForm.VARIANTS_COUNT)] +\
                 ['is_correct_' + str(i) for i in range(0, SimpleChoiceModelForm.VARIANTS_COUNT)]


FORM_CLASS = SimpleChoiceModelForm
