# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from datetime import datetime

class Cliente(object):

    def __init__(self, id_=None, cadastro=None, razao_nome=None, apelido=None, contatos=None):

        self._id = id_ if id_ else ObjectId(id_)
        self._cadastro = cadastro if cadastro else datetime.now()
        self._razao_nome = razao_nome
        self._apelido = apelido
        self._contatos = contatos if contatos else []

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        self._id = value

    @property
    def cadastro(self):
        return self._cadastro

    @property
    def razao_nome(self):
        return self._razao_nome

    @razao_nome.setter
    def razao_nome(self, value):
        self._razao_nome = value

    @property
    def apelido(self):
        return self._apelido

    @apelido.setter
    def apelido(self, value):
        self._apelido = value

    @property
    def contatos(self):
        return self._contatos

    @property
    def retorna_dic(self):
        return {
            "_id": self._id,
            "cadastro": self._cadastro,
            "razao_nome": self._razao_nome,
            "apelido": self._apelido,
            "contatos": self._contatos
        }


