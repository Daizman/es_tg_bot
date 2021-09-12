import json
import model.extensions.JsonEnumExtension as JsonEnum

import copy

from model.Memory import Memory
from model.Domain import Domain
from model.Var import Var
from model.Fact import Fact
from model.Rule import Rule

from model.types.VarType import VarType


class Shell:
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

    @active_rules.setter
    def active_rules(self, rule):
        self.__memory.active_rules = rule

    @property
    def vars(self):
        return self.__memory.vars

    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError('Попытка установить пустое имя для ЭС')
        self.__name = name.upper().strip()

    def add_rule(self, name, description, reasons, conclusion):
        self.__memory.add_rule(Rule(name, description, reasons, conclusion))

    def add_var(self, name, domain, question='', var_type=VarType.REQUESTED):
        self.__memory.add_var(Var(name, domain, question, var_type))

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

    def add_active_rule(self, rule):
        self.__memory.add_active_rule(rule)

    def insert_active_rule(self, rule, pos):
        self.__memory.insert_active_rule(rule, pos)

    def remove_active_rule(self, rule):
        self.__memory.remove_active_rule(rule)

    def update_dicts(self):
        self.__memory.update_dicts()

    def load(self, path):
        with open(path, 'r') as jsonDes:
            esDict = json.loads(jsonDes.readline())
            es = ExpertSystem(esDict['_ExpertSystem__name'])
            memoryDict = esDict['_ExpertSystem__memory']
            domensDict = memoryDict['_ExpertSystemMemory__domens']
            variablesDict = memoryDict['_ExpertSystemMemory__variables']
            rulesDict = memoryDict['_ExpertSystemMemory__rules']
            for dom in domensDict.values():
                es.addDomen(dom['_Domen__name'], dom['_Domen__vals'])

            for var in variablesDict.values():
                dom = es.getDomenByName(var['_Variable__domen']['_Domen__name'])
                vtName = var['_Variable__varType']['_name_']
                if vtName == 'REQUESTED':
                    vt = VarType.REQUESTED
                elif vtName == 'INFERRED':
                    vt = VarType.INFERRED
                else:
                    vt = VarType.OUTPUT_REQUESTED
                es.addVariable(var['_Variable__name'], dom, var['_Variable__question'], vt)

            for rul in rulesDict.values():
                rName = rul['_Rule__name']
                rDescr = rul['_Rule__description']
                rReasons = []
                for reas in rul['_Rule__reasons'].values():
                    var = es.getVariableByName(reas['_Fact__var']['_Variable__name'])
                    rReasons.append(Fact(var, reas['_Fact__val']))
                rConcl = []
                for conc in rul['_Rule__conclusions'].values():
                    var = es.getVariableByName(conc['_Fact__var']['_Variable__name'])
                    rConcl.append(Fact(var, conc['_Fact__val']))
                es.addRule(rName, rDescr, rReasons, rConcl)

    def backup(self, path):
        with open(path, 'w') as backup:
            self_copy = copy.deepcopy(self.__dict__)
            memory = copy.deepcopy(self.__memory.__dict__)
