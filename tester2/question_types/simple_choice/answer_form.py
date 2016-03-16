import json
from django import forms

# {
#   "answers":
#   [
#       {"text": "Первый ответ", "correct":false},
#       {"text": "Второй ответ", "correct":true},
#       ...
#   ]
# }
# Все пункты должны быть правильными


class SimpleChoiceForm(forms.Form):
    def __init__(self, json_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answers = json.loads(json_data)['answers']

        for k, answer in enumerate(self.answers):
            self.fields['answer_' + str(k)] = forms.BooleanField(required=False, label=answer['text'])

    # Этот метод вызывается из View, когда форма валидна для учёта ответов пользователя
    def check_answers(self):
        data = self.cleaned_data
        for k, answer in enumerate(self.answers):
            try:
                if data['answer_' + str(k)] != answer['correct']:
                    return False
            except KeyError:
                return False
        return True