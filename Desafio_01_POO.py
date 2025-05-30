# -*- coding: utf-8 -*-
"""
Created on Wed May 28 18:25:51 2025

@author: PC
"""

# Desafio 01 - Parte 01

"""
🧠 Desafio POO

Implemente as seguintes classes:

Etapas do desafio:

    1. Classe `Veiculo` com atributos `marca`, `modelo`, e `ano`. Método `descricao`.

    2. Subclasse `Carro` que herda de `Veiculo`, adiciona `porta_malas` e sobrescreve `descricao`.

    3. Crie uma função que receba uma lista de veículos (de tipos diferentes) e imprima suas descrições.

Teste seu código criando objetos reais e executando a função com eles.
"""


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def descricao(self):
        return f"{self.ano} {self.marca} {self.modelo}"
        
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, porta_malas):
        super().__init__(marca, modelo, ano)
        self.porta_malas = porta_malas
        
    def descricao(self):
        return f"{super().descricao()} com porta-malas de {self.porta_malas} litros"


def imprimir_veiculos(veiculos):
    for carro in veiculos:
        print(carro.descricao())
        
        
if __name__ == "__main__":        
    veiculo1 = Veiculo("Yamaha", "Fazer 250", 2020)
    carro1 = Carro("Toyota", "Corolla", 2023, 470)
    carro2 = Carro("Chevrolet", "Onix", 2022, 280)

lista_de_veiculos = [veiculo1, carro1, carro2]
imprimir_veiculos(lista_de_veiculos)

