from .settings import QUESTION_TYPES
import importlib


class UnknownTypeException(Exception):
    pass


class QuestionTypesManager:
    @classmethod
    def is_question_type_exist(cls, question_type):
        return question_type in QUESTION_TYPES.keys()

    @classmethod
    def get_model_form_class(cls, question_type):
        if cls.is_question_type_exist(question_type):
            try:
                model_form_module = importlib.import_module(
                    'question_types.{package_name}.model_form'.format(
                        package_name=QUESTION_TYPES[question_type]['package_name']
                    )
                )
                model_form_class = getattr(model_form_module, 'FORM_CLASS')
            except ImportError as error:
                print(error)
            else:
                return model_form_class
        else:
            raise UnknownTypeException()

    @classmethod
    def get_answer_form_class(cls, question_type):
        if cls.is_question_type_exist(question_type):
            try:
                model_form_module = importlib.import_module(
                    'question_types.{package_name}.answer_form'.format(
                        package_name=QUESTION_TYPES[question_type]['package_name']
                    )
                )
                model_form_class = getattr(model_form_module, 'FORM_CLASS')
            except ImportError as error:
                print(error)
            else:
                return model_form_class
        else:
            raise UnknownTypeException()

    @classmethod
    def get_question_types_choices(cls):
        return tuple([(question_type, QUESTION_TYPES[question_type]['verbose_name']) for question_type in QUESTION_TYPES.keys()])

    @classmethod
    def get_question_types_list(cls):
        return QUESTION_TYPES.keys()