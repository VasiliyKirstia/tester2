"""
    Здесь должны быть перечисленны все доступные типы вопросов.
"""

from .numeric.model_form import NumericModelForm
from .numeric.answer_form import NumericForm
from .simple_choice.model_form import SimpleChoiceModelForm
from .simple_choice.answer_form import SimpleChoiceForm


QUESTION_TYPES = {
    'SIMPLE_CHOICE': {
        'model_form': SimpleChoiceModelForm,
        'answer_form': SimpleChoiceForm,
        'verbose_name': "простой выбор"
    },

    'NUMERIC': {
        'model_form': NumericModelForm,
        'answer_form': NumericForm,
        'verbose_name': "числовой"
    }
}
