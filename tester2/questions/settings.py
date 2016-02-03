from .answers_forms.simple_choice import SimpleChoiceForm
from .answers_forms.numeric import NumericForm


class UnknownTypeException(Exception):
    pass


class QuestionTypesManager:

    @classmethod
    def is_question_type_exist(cls, question_type):
        return question_type in cls.__question_types.keys()

    @classmethod
    def get_form_class_by_question_type(cls, question_type):
        if cls.is_question_type_exist(question_type):
            return cls.__question_types[question_type]['form_class']
        else:
            raise UnknownTypeException()

    @classmethod
    def get_question_types_choices(cls):
        return tuple([(question_type, cls.__question_types[question_type]['verbose_name']) for question_type in cls.__question_types.keys()])

    __question_types = {
        'SIMPLE_CHOICE': {
            'verbose_name': 'простой выбор',
            'form_class': SimpleChoiceForm
        },
        'NUMERIC' : {
            'verbose_name': 'числовой',
            'form_class': NumericForm
        }
    }
