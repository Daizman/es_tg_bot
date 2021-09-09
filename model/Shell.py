from model.Memory import Memory
from model.Domain import Domain
from model.Var import Var
from model.Rule import Rule

from model.types.VarType import VarType


class ExpertSystem:
    def __init__(self, name):
        self.__name = name.upper().strip()
        self.__memory = Memory()

    @property
    def name(self):
        return self.__name

    @property
    def domains(self):
        return self.__memory.domains

    @property
    def rules(self):
        return self.__memory.rules

    @property
    def active_rules(self):
        return self.__memory.active_rules

    @property
    def vars(self):
        return self.__memory.vars

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Попытка установить пустое имя для ЭС")
        self.__name = name.upper().strip()

    def add_rule(self, name, description, reasons, conclusion):
        self.__memory.add_rule(Rule(name, description, reasons, conclusion))

    def add_var(self, name, domen, question="", var_type=VarType.REQUESTED):
        self.__memory.add_var(Var(name, domen, question, var_type))

    def add_domain(self, name, values):
        self.__memory.add_domain(Domain(name, values))

    def get_rule_index(self, name):
        return self.__memory.get_rule_index(name)

    def insert_rule(self, name, description, reasons, conclusion, pos):
        self.__memory.insert_rule(Rule(name, description, reasons, conclusion), pos)

    def swap_rules(self, pos_from, pos_to):
        self.__memory.swap_rules(pos_from, pos_to)

    def remove_rule(self, name):
        self.__memory.remove_rule(self.get_rule_by_name(name))

    def remove_var(self, name):
        self.__memory.remove_var(self.get_var_by_name(name))

    def remove_domain(self, name):
        self.__memory.remove_domain(self.get_domain_by_name(name))

    def get_rule_by_name(self, name):
        return self.__memory.get_rule_by_name(name)

    def get_var_by_name(self, name):
        return self.__memory.get_var_by_name(name)

    def get_domain_by_name(self, name):
        return self.__memory.get_domain_by_name(name)

    @active_rules.setter
    def active_rules(self, rule):
        self.__memory.active_rules = rule

    def add_active_rule(self, rule):
        self.__memory.add_active_rule(rule)

    def insert_active_rule(self, rule, pos):
        self.__memory.insert_active_rule(rule, pos)

    def remove_active_rule(self, rule):
        self.__memory.remove_active_rule(rule)

    def update_dicts(self):
        self.__memory.update_dicts()
