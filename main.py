from funcoes import *
from Produto import *
from Venda import *

limpa()

inicializacao()

while(True):

    opcao = mostrarMenu()

    limpa()

    if(opcao == 1): registarProduto()
    elif(opcao == 2): editarProduto()
    elif(opcao == 3): apagarProduto()
    elif(opcao == 4): listarProdutos(True)

    elif(opcao == 5): venderProduto()
    elif(opcao == 6): listarVendas(globais.vendas_realizadas)

    elif(opcao == 0):
        animacao("A sair")
        break
    else:
        print("--- A opção não é válida. ---")

    carregueEnter()

print("\n")