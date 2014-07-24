#coding: utf-8

from pessoa import Pessoa

class Aluno(Pessoa):

    ID = 1

    def __init__(self, nome, nascimento):
        Pessoa.__init__(self, nome, nascimento, "aluno")
        self.id = self._ID; self.__class__._ID += 1
        self.periodo = 0
        self.disciplinas = []
        self.matricula = 1000 + self.id


