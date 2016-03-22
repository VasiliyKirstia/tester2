from django import forms
from testing.models import Question


class SimpleChoiceModelForm(forms.ModelForm):
    class Meta:
        model=Question
        fields = [
            'test', 'text',
            'variant_1', 'is_correct_1',
            'variant_2', 'is_correct_2',
            'variant_3', 'is_correct_3',
            'variant_4', 'is_correct_4',
            'variant_5', 'is_correct_5',
            'variant_6', 'is_correct_6'
        ]

    variant_1 = forms.CharField()
    is_correct_1 = forms.BooleanField(required=False)

    variant_2 = forms.TextInput()
    is_correct_2 = forms.BooleanField(required=False)

    variant_3 = forms.TextInput()
    is_correct_3 = forms.BooleanField(required=False)

    variant_4 = forms.TextInput()
    is_correct_4 = forms.BooleanField(required=False)

    variant_5 = forms.TextInput()
    is_correct_5 = forms.BooleanField(required=False)

    variant_6 = forms.TextInput()
    is_correct_6 = forms.BooleanField(required=False)

    def clean(self):
        super(SimpleChoiceModelForm,self).clean()
        self.instance.type = 'SIMPLE_CHOICE'
        #todo добавить обработку остальных полей и сохранение в базу


FORM_CLASS = SimpleChoiceModelForm
