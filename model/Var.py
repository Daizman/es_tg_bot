from model.types.VarType import VarType
from model.exceptions.UsedVarError import UsedVarError


class Var:
    def __init__(self, name, domain, question="", var_type=VarType.REQUESTED):
        self.__name = name.upper().strip()
        self.__question = question if question else self.__name + "?"
        self.__var_type = var_type
        self.__facts = []
        self.__domain = domain
        self.__domain.connect_var(self)

    def __eq__(self, other):
        return other.name == self.name \
               and other.domain == self.domain \
               and other.question == self.question \
               and other.var_type == self.var_type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Name: {self.name};\nDomain: {self.domain};\nQuestion: {self.question};\nType: {self.var_type_str}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and name != "":
            if name != self.name and self.used:
                raise UsedVarError("Переменная уже используется, поэтому ее нельзя изменять")
            self.__name = name.upper().strip()
            self.question = self.__name + "?"
        else:
            raise ValueError("Переменной нельзя присвоить пустое имя")

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, domain):
        if domain is not None and domain != "":
            if domain != self.domain and self.used:
                raise UsedVarError("Переменная уже используется, поэтому ее нельзя изменять")
            self.__domain = domain
        else:
            raise ValueError("Переменной нельзя присвоить пустой домен")

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, question):
        if question is not None and question != "":
            if question != self.question and self.used:
                raise UsedVarError("Переменная уже используется, поэтому ее нельзя изменять")
            self.__question = question
        else:
            raise ValueError("Нельзя установить пустой вопрос")

    @property
    def facts(self):
        return self.__facts

    @property
    def var_type(self):
        return self.__var_type

    @var_type.setter
    def var_type(self, var_type):
        if var_type is not None and isinstance(var_type, VarType):
            if self.used:
                raise UsedVarError("Переменная уже используется, поэтому ее нельзя изменять")
            self.__var_type = var_type
            if var_type != VarType.INFERRED:
                self.question = self.__name + "?"
        else:
            raise ValueError("Попытка присвоить неверный тип переменной")

    @property
    def var_type_str(self):
        if self.var_type == VarType.REQUESTED:
            return "Запрашиваемая"
        elif self.var_type == VarType.INFERRED:
            return "Выводимая"
        else:
            return "Запрашиваемо-выводимая"

    @property
    def used(self):
        return len(self.__facts) != 0

    def used_in_fact(self, fact):
        return fact in self.__facts

    def connect_fact(self, fact):
        if fact is not None and fact not in self.__facts:
            self.__facts.append(fact)

    def remove_fact(self, fact):
        if fact is not None:
            if fact in self.__facts:
                self.__facts.remove(fact)
            else:
                raise ValueError("Попытка удаления не связанного факта")
