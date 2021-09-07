class Fact:
    def __init__(self, var, value):
        self.__var = var
        self.__value = value
        var.connect_fact(self)

    def __str__(self):
        if self.__var and self.value:
            return "{} = '{}'".format(self.var.name, self.value)
        return ""

    def __eq__(self, other):
        if other is not None and type(other) == "Fact":
            return self.var == other.var and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var):
        self.__var.remove_fact(self)
        if var is not None:
            self.__var = var
            var.connect_fact(self)
        else:
            raise ValueError("Попытка присвоить пустую переменную")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is not None:
            self.__value = value
        else:
            raise ValueError("Попытка присвоить пустое значение")

    @property
    def name(self):
        return self.__str__()
