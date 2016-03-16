class UnknownTypeException(Exception):
    pass

#todo переделать класс под паттерн одиночка и сделать импортирование новых типов вопросов динамическим.

class QuestionTypesManager:
    """Подгружает доступные типы вопросов и предоставляет набор методов для работы с ними. Выпонен в виде синглтона."""

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
        #todo добавить еще типов вопросов
    }
