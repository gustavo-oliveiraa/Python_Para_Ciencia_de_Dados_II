# -*- coding: utf-8 -*-
"""
Created on Sat May 24 09:36:35 2025

@author: gustavo.sousa
"""

"""
### 2. Encapsulamento – Desafio: Termômetro Digital
#### Contexto: Um sensor de temperatura não pode ter sua leitura ajustada manualmente.

#### Desafio:

Crie uma classe Termometro com atributo privado __temperatura.

Crie método registrar_temperatura(valor) e método ler_temperatura() para obter a leitura.

Tente alterar a temperatura diretamente fora da classe e comprove que não é possível.

Simule três registros diferentes e exiba os resultados.
"""

class Termometro:
    def __init__(self):
        self.__temperatura = None # atributo privado
        
    def registrar_temperatura(self, valor):
        self.__temperatura = valor
        
    def ler_temperatura(self):
        print(f'A temperatura atual é de {self.__temperatura}°')
    
termometro = Termometro()

termometro.registrar_temperatura(32)

termometro.ler_temperatura()


