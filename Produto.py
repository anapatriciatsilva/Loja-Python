class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    
    def toString(self, id):
        print(f"#{id + 1} - (Nome: {self.nome}) (Preço: {self.preco:.2f} €) (Quantidade: {self.quantidade}).")

    def nomeEIgual(self, nome_a_comparar):
        if(self.nome.lower() == nome_a_comparar.lower()):
            return True
        else: 
            return False

    def setNome(self, novo_nome): self.nome = novo_nome

    def setPreco(self, novo_preco): self.preco = novo_preco
    
    def setQuantidade(self, nova_quantidade): self.quantidade = nova_quantidade