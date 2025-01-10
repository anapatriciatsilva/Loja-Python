class Venda:

    def __init__(self, produto, preco_venda, quantidade_vendida):
        self.produto = produto
        self.preco_venda = preco_venda
        self.quantidade_vendida = quantidade_vendida


    def calcular_valor_total(self):
        return self.preco_venda * self.quantidade_vendida
    
    def toString(self, id):
        valor_total = self.calcular_valor_total()
        print(f"Venda #{id + 1} - {self.produto} ({self.preco_venda:.2f} €) ({self.quantidade_vendida} uni.) = ({valor_total:.2f} €)")