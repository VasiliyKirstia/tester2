import json
from django import forms

# {
#   "answer":"56",
#   "precision":"0.5",
# }
# Все пункты должны быть правильными



class NumericForm(forms.Form):
    def __init__(self, json_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = json.loads(json_data)
        self.answer = float(data['answer'])
        self.precision = float(data['precision'])

        self.fields['answer'] = forms.CharField(required=True, label='ответ', max_length=150)

    # Этот метод вызывается из View, когда форма валидна для учёта ответов пользователя
    def check_answers(self):
        data = self.cleaned_data
        try:
            answer = float( str(data['answer']).replace(',', '.') )
            if abs(answer - self.answer) > self.precision:
                return False
        except KeyError:
            return False
        except ValueError:
            return False
        return True