# -*- coding: utf-8 -*-
"""
Created on Sat May 24 10:38:10 2025

@author: gustavo.sousa
"""

"""
3. Herança – Desafio: Sistema Escolar
Contexto: Uma escola precisa diferenciar alunos e professores.
Desafio:
Crie a classe Pessoa com atributos nome e idade.

Crie as subclasses Aluno (com serie) e Professor (com disciplina).

Implemente um método apresentar() em cada classe que exiba uma mensagem diferente.

Crie objetos de cada classe e chame o método apresentar().
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f'Olá sou o(a) {self.nome}, minha idade é {self.idade}')
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie
        
    def apresentar(self):
        print(f'Olá sou o(a) aluno(a) {self.nome}, minha idade é {self.idade} e estou na {self.serie}ª serie.')
    
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        
    def apresentar(self):
        print(f'Olá sou o(a) professor(a) {self.nome}, minha idade é {self.idade} e minha disciplina é {self.disciplina}.')
    
pessoa = Pessoa('Vitor', 29)
aluno = Aluno('Gustavo', 22, 5)
professor = Professor('Pedro', 42, 'Geografia')

pessoa.apresentar()    
aluno.apresentar()
professor.apresentar()
