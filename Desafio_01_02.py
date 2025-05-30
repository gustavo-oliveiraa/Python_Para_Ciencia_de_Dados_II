# -*- coding: utf-8 -*-
"""
Created on Thu May 29 12:30:53 2025

@author: PC
"""

# Desafio 01 - Parte 02 remedio

#.to_string(index=False)

"""
🧠 Desafio Prático: Análise de Dados de Livros 📚
Você é um analista de dados em uma livraria online.

Etapas do desafio:
    1. Leitura do Dataset
        
        Leia o arquivo CSV ou Excel contendo os dados dos livros.

    2. Exploração Inicial

        Mostre as 5 primeiras linhas do DataFrame.

        Mostre os nomes das colunas disponíveis.

        Mostre o número de linhas e colunas do dataset.

    3. Filtro de Livros com Preço Acima da Média

        Calcule a média de preço (coluna price) e filtre os livros com preço acima da média.

        Mostre apenas as colunas: title, price, author.

    4. Filtrar por Idioma e Avaliação

        Selecione os livros em espanhol(language == 'Spanish') que têm avaliação média (avg_reviews) acima de 4.5 (Faça isso em uma linha).

        Exiba as colunas: title, avg_reviews, language.

    5. Questão Desafio - Não Obrigatório

        Criação de Coluna Nova – Valor Total

        Crie uma nova coluna chamada valor_estimado, que é o produto de price × n_reviews (convertendo n_reviews para número inteiro antes).

        Exiba os livros com maior valor_estimado em ordem decrescente (mostre os 5 primeiros).
"""

import pandas as pd

# 1. Leitura do Dataset
df = pd.read_csv('book_dataset.csv')

# 2. Exploração Inicial
print(df.head())
print(df.columns)
print('Nº Linhas e Nº Colunas')
print(df.shape)

# 3. Filtro de Livros com Preço Acima da Média
media_livros = df['price'].mean()
filtro_acima_media = df[df['price'] > media_livros]
print('Livros com preço acima da média (title, price, author):')
print(filtro_acima_media[['title', 'price', 'author']]) # Perguntar sobre isso depois [[]]

# 4. Filtrar por Idioma e Avaliação
print('Livros em espanhol com Review > 4.5:')
print(df[(df['language'] == 'Spanish') & (df['avg_reviews'] > 4.5)][['title', 'avg_reviews', 'language']])

# 5. Questão Desafio - Não Obrigatório

df['n_reviews'] = pd.to_numeric(df['n_reviews'].str.replace(',', '', regex=False), errors='coerce')
media = df['n_reviews'].mean()
df['n_reviews'] = df['n_reviews'].fillna(media)

df['valor_estimado'] = df['price'] * df['n_reviews']

df_ordenado = df.sort_values(by='valor_estimado', ascending=False)

print(df_ordenado.head(5)[['title', 'price', 'n_reviews', 'valor_estimado']])




































