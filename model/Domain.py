from model.exceptions.UsedDomainError import UsedDomainError
from model.Var import Var
from model.types.VarType import VarType


class Domain:
    def __init__(self, name, values=None):
        self.__name = name.upper().strip()
        self.__values = values[:] if values else []
        self.__connected_vars = []

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        other_values = other.getValues()
        domain_size = len(self.name)
        if domain_size != len(other_values):
            return False
        for i in range(other_values):
            if other_values[i] != self.values[i]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name + ":\n" + "\n".join(map(str, self.values))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is not None and name != "":
            if name != self.name and self.used:
                raise UsedDomainError("Домен уже используется, поэтому его нельзя изменять")
            self.__name = name.upper().strip()
        else:
            raise ValueError("Необходимо указать имя домена")

    @property
    def connected_vars(self):
        return self.__connected_vars

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    @property
    def used(self):
        return len(self.connected_vars) != 0

    def add_value(self, value):
        value = str(value).upper().strip()
        res = value in self.values
        if not res:
            if self.used:
                raise UsedDomainError("Домен уже используется, поэтому его нельзя изменять")
            self.values.append(value)
        return res

    def remove_value(self, value):
        value = str(value).upper().strip()
        value_exist = value in self.values
        if value_exist:
            if self.used:
                raise UsedDomainError("Домен уже используется, поэтому его нельзя изменять")
            self.values.remove(value)
        return value_exist

    def connect_var(self, var):
        if var is not None and var.name != "":
            self.connected_vars.append(var)
        else:
            raise ValueError("Необходимо указать имя переменной")

    def remove_var(self, var):
        if var is not None and var.name != "":
            if var in self.connected_vars:
                self.connected_vars.remove(var)
                var.domain = []
            else:
                raise ValueError("Попытка удалить переменную, которая не связана с доменом")
        else:
            raise ValueError("Необходимо указать имя переменной")
