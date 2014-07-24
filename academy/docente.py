#coding: utf-8

from academy.pessoa import Pessoa

class Docente(Pessoa):

    ID = 1

    def __init__(self, nome, nascimento):
        Pessoa.__init__(self, nome, nascimento, "docente")
        self.id = self.__ID; self.__class__._ID += 1