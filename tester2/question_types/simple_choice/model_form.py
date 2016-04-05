from django import forms
from testing.models import Question
import json


_VARIANTS_COUNT = 10


class SimpleChoiceModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(0, _VARIANTS_COUNT):
            self.fields['variant_' + str(i)] = forms.CharField(required=False)
            self.fields['is_correct_' + str(i)] = forms.BooleanField(required=False, label='вариант {0} верный'.format(i))

    def clean(self):
        super(SimpleChoiceModelForm, self).clean()

        data = {'answers': []}
        print(self.cleaned_data)
        for i in range(0, _VARIANTS_COUNT):
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
        exclude = ['type', 'answers']

FORM_CLASS = SimpleChoiceModelForm
