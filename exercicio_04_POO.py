# -*- coding: utf-8 -*-
"""
Created on Sat May 24 11:31:18 2025

@author: gustavo.sousa
"""

"""
5. Métodos Especiais – Desafio: Carrinho de Compras
Contexto: Um e-commerce deseja manipular objetos de carrinho com mais naturalidade.
Desafio:
Crie a classe Carrinho com uma lista de itens e método adicionar_item(nome).

Implemente len para retornar a quantidade de itens.

Implemente str para retornar os itens separados por vírgula.

Teste imprimindo o carrinho e aplicando len(carrinho).
"""

class Carrinho:
    def __init__(self, lista_itens: list):
        self.lista_itens = lista_itens
        
    def adicionar_item(self, nome):
        self.lista_itens += nome
        
    def __str__(self):
        return f"Lista de produtos: {str(self.lista_itens).replace('[', '').replace(']', '')}"
    
    def __len__(self):
        return len(self.lista_itens)
    
carrinho = Carrinho(['maça', 'banana'])

carrinho.adicionar_item(['uva'])

print(carrinho)
print(len(carrinho))
