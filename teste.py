# -*- coding: utf-8 -*-



from pymongo import MongoClient
from cliente import Cliente
from conexao import Conexao
from contato import Contato

NOME_BANCO = "bsistema"
HOST = "mongodb://localhost:27017/"


Conexao_banco_de_dados = MongoClient(HOST)
banco = Conexao_banco_de_dados[NOME_BANCO]
conexao = Conexao(banco=banco)

print("PASSOU NO TESTE 1")

cliente = Cliente(id_=None, cadastro=None, razao_nome="marcella",
                apelido="marc")

contato = Contato(id_=None, cadastro=None, nome="nana", email="nana@qqw", telefone="223344")
print("passou no teste 2")

# # inserir cliente no banco
# conexao.inserir(cliente)
# print("PASSOU NO TESTE 3")

#buscar cliente
conexao.buscar("5bb369a59dc6d60e87e8dcd6")
print("PASSOU NO TESTE 4")

# #atualizar cliente
# cliente.razao_nome = "mamama"
# conexao.atualizar(cliente.id_, cliente)
# print("PASSOU NO TESTE 5")

#listar clientes
conexao.listar()
print("PASSOU NO TESTE 6")

# #inserir contato para o cliente
# conexao.inserir_contato(cliente.id_, contato)
# print("PASSOU NO TESTE 7")

# #atualiza contato do cliente
# contato.email = "lilo"
# conexao.atualizar_contato(cliente.id_, contato)
# print("PASSOU NO TESTE 8")

#excluir contato
# conexao.excluir_contato(cliente.id_, contato.id_)
# print("PASSOU NO TESTE 9")

#excluir cliente
# conexao.excluir(cliente.id_)
# print("PASSOU NO ULTIMO TESTE")