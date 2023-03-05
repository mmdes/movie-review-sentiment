# -*- coding: utf-8 -*-

"""
Nome do Programa: Minha primeira rede neural em PLN
Autor: Matheus Matos de Souza
Data de criação: 03/03/2023
Descrição: análise de comentários na plataforma imdb em português
"""

from keras.datasets import imdb
from keras.preprocessing import sequence


decoded_statement = []

(x_train, y_train), (x_test, y_test) = imdb.load_data()

ltrain_x =  list(x_train)
ltrain_y =  list(y_train)
ltest_x = list(x_test)
ltest_y = list(y_test)

word_index = imdb.get_word_index()

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

decoded_statement = []

for j in range(0, len(x_train_list)):
    decoded_statement.append(' '.join([reverse_word_index.get(i - 3, '?') for i in x_train[j]]))



