import os
import time
import globais
from Produto import *
from Venda import *

#Funcoes
def mostrarMenu():
    animacao("Aguarde...")
    print("--- Loja Python---\n")
    print("1 - Registar Produto.")
    print("2 - Editar Produto.")
    print("3 - Apagar Produto.")
    print("4 - Listar Produtos.\n")
    print("5 - Vender.")
    print("6 - Listar as vendas. \n")
    print("0 - Sair. \n")
    return int(input("- Opção: "))

def registarProduto ():
    print("--- Registar Produto ---")
    print()
    nome = input("- Digite o nome do novo produto: ")
    if(nomeJaExiste(nome) == False):
        preco = float(input("- Digite o preço deste produto: "))
        quantidade = int(input("- Digite a quantidade deste produto: "))
        globais.produtos.append(Produto(nome, preco, quantidade))
        print("\n--- O produto foi registado com sucesso. ---")
    else:
        print("\n--- Este nome já se encontra associado a outro produto. ---")

def editarProduto ():
    print("--- Editar Produto ---")
    print()
    listarProdutos(False)
    print()
    id = int(input("- Digite o ID do produto que deseja editar: ")) - 1
    if(id >= 0 and id < len(globais.produtos)):
        print()
        globais.produtos[id].toString(id)
        print()

        print("---Menu de Edição ---\n")
        print("1 - Nome.")
        print("2 - Preço.")
        print("3 - Quantidade.\n")
        print("0 - Cancelar.\n")

        opcao = int(input("- Opção: "))
        print()

        if(opcao == 1):
            novo_nome = input(f"- Digite o nome para substituir ({globais.produtos[id].nome}): ")
            if(nomeJaExiste(novo_nome) == False):
                globais.produtos[id].setNome(novo_nome)
                print("\n--- Nome alterado com sucesso. ---")
            else:
                print("\n--- Este nome já se encontra associado a outro produto. ---")
        elif(opcao == 2):
            novo_preco = float(input(f"- Digite o novo preço para substituir o anterior ({globais.produtos[id].preco:.2f} €): "))
            globais.produtos[id].setPreco(novo_preco)
            print("\n--- Preço atualizado com sucesso. ---")
        elif(opcao == 3):
            nova_quantidade = int(input(f"- Digite a nova quantidade em stock que substituirá ({globais.produtos[id].quantidade} unidades): "))
            globais.produtos[id].setQuantidade(nova_quantidade)
            print("\n--- Quantidade de stock atualizado com sucesso. ---")
        else:
            print("--- A opção não é válida. ---")

    else:
        print("\n--- O ID nã é válido. ---")


def apagarProduto():
    print("--- Apagar Produto ---")
    print()
    listarProdutos(False)
    print()
    id = int(input("- Digite o ID do produto que deseja apagar: ")) - 1
    if(id >= 0 and id < len(globais.produtos)):
        print()
        produto_apagado = globais.produtos.pop(id)
        produto_apagado.toString(id)
        print("\n--- Produto apagado com sucesso. ---")
    else:
        print("\n--- O ID nã é válido. ---")

def listarProdutos(com_titulo):
    if(com_titulo):
        print("--- Lista de Produtos ---\n")
    for i in range(len(globais.produtos)): globais.produtos[i].toString(i)

def venderProduto():
    print("--- Vender Produto ---")
    print()
    listarProdutos(False)
    print()
    id = int(input("\n- Digite o ID do produto que deseja vender: ")) - 1
    if(id >= 0 and id < len (globais.produtos)):
        p = globais.produtos[id]
        quantidade_venda = int(input(f"\n- Digite a quantidade de ({p.nome}) que será vendida: "))
        print()
        if(quantidade_venda <= p.quantidade and quantidade_venda > 0):
            p.quantidade -= quantidade_venda
            venda = Venda(p.nome, p.preco, quantidade_venda)
            globais.vendas_realizadas.append(venda)
            venda.toString(len(globais.vendas_realizadas))
            print()
            print("\n--- Produto vendido com sucesso. ---")
        else:
            print("\n--- A quantidade não está disponível. ---")
    else:
        print("\n--- O ID nã é válido. ---")

def listarVendas(vendas):
    print("--- Lista das Vendas ---")
    print()
    total = 0
    for i in range(len(vendas)):
        vendas[i].toString(i)
        total += vendas[i].calcular_valor_total()
    print(f"\nValor total das vendas: ({total:.2f} €)")


# Auxiliadoras
def inicializacao():
    globais.produtos.append(Produto("Secretária", 139.90, 10))
    globais.produtos.append(Produto("Cadeira", 75.00, 15))
    globais.produtos.append(Produto("Candeeiro", 25.00, 30))
    globais.produtos.append(Produto("Suporte", 40.00, 20))
    globais.produtos.append(Produto("Protetor", 5.00, 50))

def nomeJaExiste(nome_a_verificar):
    for p in globais.produtos:
        if(p.nomeEIgual(nome_a_verificar)):
            return True
    return False

#Especiais
def limpa():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguarde(tempo):
    time.sleep(tempo)

def animacao(frase):
    tempo = 0.1
    limpa()
    print(frase, end="", flush=True)
    aguarde(tempo)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    limpa()

def carregueEnter(): input("\nCarregue <ENTER> para continuar...")