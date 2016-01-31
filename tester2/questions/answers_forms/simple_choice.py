import json
from django import forms

# {
#   "answers":
#   [
#       {"text": "Первый ответ", "correct":false},
#       {"text": "Второй ответ", "correct":true},
#   ]
# }
# Все пункты должны быть правильными

class SimpleChoiceForm(forms.Form):
    def __init__(self, answers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answers = json.loads(answers)['answers']

        for k, answer in enumerate(self.answers):
            self.fields['answer_' + str(k)] = forms.BooleanField(required=False, label=answer['text'])

    # Этот метод вызывается из View, когда форма валидна для учёта ответов пользователя
    def check_answers(self, answers):
        data = self.cleaned_data
        for k, answer in enumerate(self.answers):
            try:
                if data['answer_' + str(k)] != answer['correct']:
                    return False
            except KeyError:
                return False
        return True

# На каждый тип вопроса нужно ещё сделать заменяемые формы для создания ответов, возможно нужно перегруппировать пакеты