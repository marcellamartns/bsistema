# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from cliente import Cliente
from contato import Contato

NOME_COLECAO = "clientes"

class Conexao(object):

    def __init__(self, banco):

        self._colecao = banco[NOME_COLECAO]

    def inserir(self, cliente):

        self._colecao.insert_one(cliente.retorna_dic)

    def buscar(self, codigo_cliente):

        qry = {"_id": ObjectId(codigo_cliente)}
        cliente = self._colecao.find_one(qry)

        lista_contatos = []

        for contato in cliente["contatos"]:

            novo_contato = Contato(contato["_id"], contato["cadastro"], contato["nome"], contato["email"], contato["telefone"])
            lista_contatos.append(novo_contato)

        novo_cliente = Cliente(cliente["_id"], cliente["cadastro"], cliente["razao_nome"], cliente["apelido"], lista_contatos)
        novo_cliente = Cliente(novo_cliente)

        return novo_cliente

    def atualizar(self, codigo_cliente, cliente):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {
            "$set": {
                "razao_nome": cliente.razao_nome,
                "apelido": cliente.apelido
            }
        }

        self._colecao.update_one(qry, fld)

    def listar(self):

        lista_retorno, lista_contato_retorno = [], []

        clientes = self._colecao.find()

        for cliente in clientes:
            for contato in cliente["contatos"]:
                novo_contato = Contato(contato["_id"], contato["cadastro"], contato["nome"], contato["email"], contato["telefone"])
                lista_contato_retorno.append(novo_contato)

            novo_cliente = Cliente(cliente["_id"], cliente["cadastro"], cliente["razao_nome"], cliente["apelido"], lista_contato_retorno)

            lista_retorno.append(novo_cliente)

        return lista_retorno

    def excluir(self, codigo_cliente):

        self._colecao.delete_one({"_id": ObjectId(codigo_cliente)})

    def inserir_contato(self, codigo_cliente, contato):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$push": {"contatos": contato.retorna_dic}}

        self._colecao.update_one(qry, fld)

    def atualizar_contato(self, codigo_cliente, contat):


        qry = {"_id": codigo_cliente, "contatos._id": contat.id_}

        fld = {
            "$set": {
                "contatos.$.nome": contat.nome,
                "contatos.$.email": contat.email,
                "contatos.$.telefone": contat.telefone
            }
        }

        self._colecao.update_one(qry, fld)

    def excluir_contato(self, codigo_cliente, codigo_contato):

        qry = {"_id": ObjectId(codigo_cliente)}
        fld = {"$pull": {"contatos": {"_id": ObjectId(codigo_contato)}}}

        self._colecao.update_one(qry, fld)