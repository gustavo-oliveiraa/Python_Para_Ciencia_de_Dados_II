# -*- coding: utf-8 -*-
"""
Created on Sat May 24 09:02:53 2025

@author: gustavo.sousa
"""

"""
### 1. Classes e Objetos – Desafio: Agendamento de Reuniões
#### Contexto: Um assistente virtual precisa registrar reuniões.

#### Desafio:

Crie uma classe Reuniao com os atributos titulo, data, hora, participantes (lista).

Crie um método resumo que retorne uma string formatada com todas as informações.

Crie duas reuniões e imprima o resumo delas.
"""

class Reuniao:
    def __init__(self, hora: str = '5'):
        self.pi = 3.14
        self.hora = hora
        self.data = None
        self.participantes = list()
        self.titulo = None
        
    def agendar_reuniao(self, hora, data, participantes, titulo):
        self.hora = hora
        self.data = data
        self.participantes = participantes
        self.titulo = titulo
    
    def resumo(self):
        print(f"""
A reunião {self.titulo} sera as {self.hora} e no dia {self.data}
Os participantes são:
{str(self.participantes).replace('[', '').replace(']', '')}     
        
""")

# pq aqui teve o nome  e o =
aula_python = Reuniao(hora='10')

# e aqui nao
aula_python.agendar_reuniao('8', '24/05/2025', ['Lucas Bitar', 'Gustavo Maxwel'], 'Aula Python')

aula_python.resumo()