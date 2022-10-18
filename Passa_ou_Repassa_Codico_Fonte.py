from ast import Break
from operator import eq
import os
import time
import smtplib
import email.message
import pandas as pd
from Tools.scripts.dutree import display
time.sleep(2)
equipe_azul = int(0)
equipe_vermelha = int(0)
pergunta_1 = ('l')
pergunta_2 = ('l')
pergunta_3 = ('l')
pergunta_4 = ('l')
pergunta_5 = ('l')
pergunta_6 = ('l')
pergunta_7 = ('l')
pergunta_8 = ('l')
pergunta_9 = ('l')
pergunta_10 = ('l')
os.system('cls') or None


print('\033[1;33;40m -=-=-=-=-=-=-=-=-=-=-=-=ATENÇÃO!!!=-=-=-=-=-=-=-=-=-=-=-=- \033[m')

print('-=-'*35)
print('O 1° jogador será chamado de "EQUIPE AZUL" e o 2° jogador será chamado de "EQUIPE VERMELHA"')
print('''Ao acertar a resposta, a equipe ganha um (1) ponto. Ao passar a pergunta, a equipe adversária ganha,
caso acertem, dois (2) pontos.
Caso repassarem, a equipe que acerta a resposta ganha três (3) pontos
Se errarem, a equipe adversária ganha os pontos equivalentes. ''')
print('-=-'*35)
time.sleep(15)

email_des = str(input('Digite seu Email: '))

jogador_001 = str(input('Nome do 1° jogador: '))
jogador_002 = str(input('Nome do 2° jogador: '))
os.system('cls') or None


print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[1;32;40m INÍCIO \033[m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\033[4;36;40m EQUIPE AZUL \033[m')
while pergunta_1 not in 'ABCPR':
    print('Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?')
    print('A - Tem entre 2 a 4 litros. São retirados 450 mililitros ')
    print('B - Tem entre 4 a 6 litros. São retirados 450 mililitros')
    print('C - Tem 10 litros. São retirados 2 litros')
    print('P/R - Passa ou Repassa')
    pergunta_1 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_1 == 'B':
        equipe_azul = equipe_azul + 1
        print('Resposta Certa! Ponto para a equipe azul!')
        time.sleep(2)
    elif pergunta_1 in 'AC':
        print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
        equipe_vermelhac = equipe_vermelha + 1
        time.sleep(2)
    elif pergunta_1 in 'PR':
        os.system('cls') or None
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?')
        print('A - Tem entre 2 a 4 litros. São retirados 450 mililitros')
        print('B - Tem entre 4 a 6 litros. São retirados 450 mililitros')
        print('C - Tem 10 litros. São retirados 2 litros')
        print('P/R - Passa ou Repassa')
        pergunta_1 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_1 == 'B':
            equipe_vermelha = equipe_vermelha +2
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_1 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 2
        elif pergunta_1 in 'PR':
            os.system('cls') or None
    while pergunta_1 not in 'ABC':
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print('Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?')
        print('A - Tem entre 2 a 4 litros. São retirados 450 mililitros')
        print('B - Tem entre 4 a 6 litros. São retirados 450 mililitros')
        print('C - Tem 10 litros. São retirados 2 litros')
        pergunta_1 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_1 == 'B':
            equipe_azul = equipe_azul + 3
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_1 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            equipe_vermelhac = equipe_vermelha + 3
            time.sleep(2)
        
############################################################################################
os.system('cls') or None
print('\033[4;31;40m EQUIPE VERMELHA \033[m')
while pergunta_2 not in 'ABCPR':
    print('De quem é a famosa frase “Penso, logo existo”?')
    print('A - Descartes')
    print('B - Galileu Galilei')
    print('C - Platão')
    print('P/R - Passa ou Repassa')
    pergunta_2 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_2 == 'A':
        equipe_vermelha = equipe_vermelha + 1
        print('Resposta Certa! Ponto para a equipe vermelha!')
        time.sleep(2)
    elif pergunta_2 in 'BC':
        print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
        time.sleep(2)
        equipe_azul = equipe_azul + 1
    elif pergunta_2 in 'PR':
        os.system('cls') or None
        print(print('\033[4;36;40m EQUIPE AZUL \033[m'))
        print('De quem é a famosa frase “Penso, logo existo”?')
        print('De quem é a famosa frase “Penso, logo existo”?')
        print('A - Descartes')
        print('B - Galileu Galilei')
        print('C - Platão')
        print('P/R - Passa ou Repassa')
        pergunta_2 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_2 == 'A':
            equipe_azul = equipe_azul + 2
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_2 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelha = equipe_vermelha + 2
        elif pergunta_2 in 'PR':
            os.system('cls') or None
    while pergunta_1 not in 'ABC':
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('De quem é a famosa frase “Penso, logo existo”?')
        print('A - Descartes')
        print('B - Galileu Galilei')
        print('C - Platão')
        pergunta_2 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_2 == 'A':
            equipe_vermelha = equipe_vermelha + 3
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_1 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 3

#############################################################################################################
os.system('cls') or None
print('\033[4;36;40m EQUIPE AZUL \033[m')
while pergunta_3 not in 'ABCPR':
    print('De onde é a invenção do chuveiro elétrico?')
    print('A - França')
    print('B - Brasil')
    print('C - Inglaterra')
    print('P/R - Passa ou Repassa')
    pergunta_3 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_3 == 'B':
        equipe_azul = equipe_azul + 1
        print('Resposta Certa! Ponto para a equipe azul!')
        time.sleep(2)
    elif pergunta_3 in 'AC':
        print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
        time.sleep(2)
        equipe_vermelhac = equipe_vermelha + 1
    elif pergunta_3 in 'PR':
        os.system('cls') or None
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('De onde é a invenção do chuveiro elétrico?')
        print('A - França')
        print('B - Brasil')
        print('C - Inglaterra')
        print('P/R - Passa ou Repassa')
        pergunta_3 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_3 == 'B':
            equipe_vermelha = equipe_vermelha + 2
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_3 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 2
        elif pergunta_3 in 'PR':
            os.system('cls') or None
    while pergunta_3 not in 'ABC':
        print(print('\033[4;36;40m EQUIPE AZUL \033[m'))
        print('De onde é a invenção do chuveiro elétrico?')
        print('A - França')
        print('B - Brasil')
        print('C - Inglaterra')
        pergunta_3 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_3 == 'B':
            equipe_azul = equipe_azul + 3
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_3 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            equipe_vermelhac = equipe_vermelha + 3
            time.sleep(2)

########################################################################################################
os.system('cls') or None
print('\033[4;31;40m EQUIPE VERMELHA \033[m')
while pergunta_4 not in 'ABCPR':
    print(' Quais o menor e o maior país do mundo?')
    print('A - Nauru e China')
    print('B - Vaticano e Rússia ')
    print('C - Malta e Estados Unidos')
    print('P/R - Passa ou Repassa')
    pergunta_4 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_4 == 'B':
        equipe_vermelha = equipe_vermelha + 1
        print('Resposta Certa! Ponto para a equipe vermelha!')
        time.sleep(2)
    elif pergunta_4 in 'AC':
        print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
        time.sleep(2)
        equipe_azul = equipe_azul + 1
    elif pergunta_4 in 'PR':
        os.system('cls') or None
        print(print('\033[4;36;40m EQUIPE AZUL \033[m'))
        print(' Quais o menor e o maior país do mundo?')
        print('A - Nauru e China')
        print('B - Vaticano e Rússia ')
        print('C - Malta e Estados Unidos')
        print('P/R - Passa ou Repassa')
        pergunta_4 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_4 == 'B':
            equipe_azul = equipe_azul + 2
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_4 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelha = equipe_vermelha + 2 
        elif pergunta_4 in 'PR':
            os.system('cls') or None
    while pergunta_4 not in 'ABC':
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print(' Quais o menor e o maior país do mundo?')
        print('A - Nauru e China')
        print('B - Vaticano e Rússia ')
        print('C - Malta e Estados Unidos')
        pergunta_4 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_4 == 'B':
            equipe_vermelha = equipe_vermelha + 3
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_4 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 3

#################################################################################################
os.system('cls') or None
print('\033[4;36;40m EQUIPE AZUL \033[m')
while pergunta_5 not in 'ABCPR':
    print('Qual o nome do presidente do Brasil que ficou conhecido como Jango?')
    print('A - Jânio Quadros')
    print('B - Getúlio Vargas')
    print('C - João Goulart')
    print('P/R - Passa ou Repassa')
    pergunta_5 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_5 == 'C':
        equipe_azul = equipe_azul + 1
        print('Resposta Certa! Ponto para a equipe azul!')
        time.sleep(2)
    elif pergunta_5 in 'AB':
        print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
        time.sleep(2)
        equipe_vermelha = equipe_vermelha + 1
    elif pergunta_5 in 'PR':
        os.system('cls') or None
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Qual o nome do presidente do Brasil que ficou conhecido como Jango?')
        print('A - Jânio Quadros')
        print('B - Getúlio Vargas')
        print('C - João Goulart')
        print('P/R - Passa ou Repassa')
        pergunta_5 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_5 == 'C':
            equipe_vermelha = equipe_vermelha + 2
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_5 in 'AB':
            print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 2
        elif pergunta_5 in 'PR':
            os.system('cls') or None
    while pergunta_5 not in 'ABC':
        print(print('\033[4;36;40m EQUIPE AZUL \033[m'))
        print('Qual o nome do presidente do Brasil que ficou conhecido como Jango?')
        print('A - Jânio Quadros')
        print('B - Getúlio Vargas')
        print('C - João Goulart')
        pergunta_5 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_5 == 'B':
            equipe_azul = equipe_azul + 3
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_5 in 'AB':
            print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelhac = equipe_vermelha + 3

######################################################################################################
#####erro grave corrigido!!!
#################################################################################################
os.system('cls') or None
print('\033[4;31;40m EQUIPE VERMELHA \033[m')
while pergunta_7 not in 'ABCPR':
    print('Qual o grupo em que todas as palavras foram escritas corretamente?')
    print('A - Asterístico, beneficiente, metereologia, entretido')
    print('B - Asterisco, beneficiente, metereologia, entretido')
    print('C - Asterisco, beneficente, meteorologia, entretido')
    print('P/R - Passa ou Repassa')
    pergunta_7 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_7 == 'C':
        equipe_vermelha = equipe_vermelha + 1
        print('Resposta Certa! Ponto para a equipe vermelha!')
        time.sleep(2)
    elif pergunta_7 in 'AB':
        print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
        time.sleep(2)
        equipe_azul = equipe_azul + 1
    elif pergunta_7 in 'PR':
        os.system('cls') or None
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print('Qual o grupo em que todas as palavras foram escritas corretamente?')
        print('A - Asterístico, beneficiente, metereologia, entretido')
        print('B - Asterisco, beneficiente, metereologia, entretido')
        print('C - Asterisco, beneficente, meteorologia, entretido')
        print('P/R - Passa ou Repassa')
        pergunta_7 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_7 == 'C':
            equipe_azul = equipe_azul + 2
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_7 in 'AB':
            print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelha = equipe_vermelha + 2
        elif pergunta_7 in 'PR':
            os.system('cls') or None
    while pergunta_7 not in 'ABC':
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Qual o grupo em que todas as palavras foram escritas corretamente?')
        print('A - Asterístico, beneficiente, metereologia, entretido')
        print('B - Asterisco, beneficiente, metereologia, entretido')
        print('C - Asterisco, beneficente, meteorologia, entretido')
        pergunta_7 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_7 == 'C':
            equipe_vermelha = equipe_vermelha + 3
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_7 in 'AB':
            print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
            equipe_azul = equipe_azul + 3
            time.sleep(2)

##########################################################################################################
os.system('cls') or None
print('\033[4;36;40m EQUIPE AZUL \033[m')
while pergunta_8 not in 'ABCPR':
    print('Qual o livro mais vendido no mundo a seguir à Bíblia?')
    print('A - O Senhor dos Anéis')
    print('B - Dom Quixote')
    print('C - O Pequeno Príncipe')
    print('P/R - Passa ou Repassa')
    pergunta_8 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_8 == 'B':
        equipe_azul = equipe_azul + 1
        print('Resposta Certa! Ponto para a equipe azul!')
        time.sleep(2)
    elif pergunta_8 in 'AC':
        print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
        equipe_vermelhac = equipe_vermelha + 1
        time.sleep(2)
    elif pergunta_8 in 'PR':
        os.system('cls') or None
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Qual o livro mais vendido no mundo a seguir à Bíblia?')
        print('A - O Senhor dos Anéis')
        print('B - Dom Quixote')
        print('C - O Pequeno Príncipe')
        print('P/R - Passa ou Repassa')
        pergunta_8 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_8 == 'B':
            equipe_vermelha = equipe_vermelha + 2
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_8 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 2
        elif pergunta_8 in 'PR':
            os.system('cls') or None
    while pergunta_8 not in 'ABC':
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print('Qual o livro mais vendido no mundo a seguir à Bíblia?')
        print('A - O Senhor dos Anéis')
        print('B - Dom Quixote')
        print('C - O Pequeno Príncipe')
        pergunta_8 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_8 == 'B':
            equipe_azul = equipe_azul + 3
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_8 in 'AC':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelhac = equipe_vermelha + 3

#####################################################################################################
os.system('cls') or None
print('\033[4;31;40m EQUIPE VERMELHA \033[m')
while pergunta_9 not in 'ABCPR':
    print('Quantas casas decimais tem o número pi?')
    print('A - Infinitas')
    print('B - Milhares')
    print('C - Vinte')
    print('P/R - Passa ou Repassa')
    pergunta_9 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_9 == 'A':
        equipe_vermelha = equipe_vermelha+ 1
        print('Resposta Certa! Ponto para a equipe vermelha!')
        time.sleep(2)
    elif pergunta_9 in 'BC':
        print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
        time.sleep(2)
        equipe_azul = equipe_azul + 1
    elif pergunta_9 in 'PR':
        os.system('cls') or None
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print('Quantas casas decimais tem o número pi?')
        print('A - Infinitas')
        print('B - Milhares')
        print('C - Vinte')
        print('P/R - Passa ou Repassa')
        pergunta_9 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_9 == 'A':
            equipe_azul = equipe_azul + 2
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_9 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelha = equipe_vermelha + 2
        elif pergunta_9 in 'PR':
            os.system('cls') or None
    while pergunta_9 not in 'ABC':
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Quantas casas decimais tem o número pi?')
        print('A - Infinitas')
        print('B - Milhares')
        print('C - Vinte')
        pergunta_9 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_9 == 'A':
            equipe_vermelha = equipe_vermelha + 3
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_9 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 3

###############################################################################################
os.system('cls') or None
print('\033[4;36;40m EQUIPE AZUL \033[m')
while pergunta_10 not in 'ABCPR':
    print(' Atualmente, quantos elementos químicos a tabela periódica possui?')
    print('A - 113')
    print('B - 108')
    print('C - 118')
    print('P/R - Passa ou Repassa')
    pergunta_10 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_10 == 'C':
        equipe_azul = equipe_azul + 1
        print('Resposta Certa! Ponto para a equipe azul!')
        time.sleep(2)
    elif pergunta_10 in 'AB':
        print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
        time.sleep(2)
        equipe_vermelha = equipe_vermelha + 1
    elif pergunta_10 in 'PR':
        os.system('cls') or None
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print(' Atualmente, quantos elementos químicos a tabela periódica possui?')
        print('A - 113')
        print('B - 108')
        print('C - 118')
        print('P/R - Passa ou Repassa')
        pergunta_10 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_10 == 'C':
            equipe_vermelha = equipe_vermelha + 2
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_10 in 'AB':
            print('Errou! Resposta certa: letra C, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 2 
        elif pergunta_10 in 'PR':
            os.system('cls') or None
    while pergunta_10 not in 'ABC':
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print(' Atualmente, quantos elementos químicos a tabela periódica possui?')
        print('A - 113')
        print('B - 108')
        print('C - 118')
        pergunta_10 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_10 == 'C':
            equipe_azul = equipe_azul + 3
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_10 in 'AB':
            print('Errou! Resposta certa: letra B, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelhac = equipe_vermelha + 3
###################################################################################################
os.system('cls') or None
print('\033[4;31;40m EQUIPE VERMELHA \033[m')
while pergunta_6 not in 'ABCPR':
    print('Quais os países que têm a maior e a menor expectativa de vida do mundo?')
    print('A - Japão e Serra Leoa')
    print('B - Itália e Chade')
    print('C - Estados Unidos e Angola')
    print('P/R - Passa ou Repassa')
    pergunta_6 = str(input('Qual é a sua opção? ')).upper()
    if pergunta_6 == 'A':
        equipe_vermelha = equipe_vermelha + 1
        print('Resposta Certa! Ponto para a equipe vermelha!')
        time.sleep(2)
    elif pergunta_6 in 'BC':
        print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
        time.sleep(2)
        equipe_azul = equipe_azul + 1
    elif pergunta_6 in 'PR':
        os.system('cls') or None
        print('\033[4;36;40m EQUIPE AZUL \033[m')
        print('Quais os países que têm a maior e a menor expectativa de vida do mundo?')
        print('A - Japão e Serra Leoa')
        print('B - Itália e Chade')
        print('C - Estados Unidos e Angola')
        print('P/R - Passa ou Repassa')
        pergunta_6 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_6 == 'A':
            equipe_azul = equipe_azul + 2
            print('Resposta Certa! Ponto para a equipe azul!')
            time.sleep(2)
        elif pergunta_6 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_vermelha = equipe_vermelha + 2
        elif pergunta_6 in 'PR':
            os.system('cls') or None
    while pergunta_6 not in 'ABC':
        print('\033[4;31;40m EQUIPE VERMELHA \033[m')
        print('Quais os países que têm a maior e a menor expectativa de vida do mundo?')
        print('A - Japão e Serra Leoa')
        print('B - Itália e Chade')
        print('C - Estados Unidos e Angola')
        pergunta_6 = str(input('Qual é a sua opção? ')).upper()
        if pergunta_6 == 'A':
            equipe_vermelha = equipe_vermelha + 3
            print('Resposta Certa! Ponto para a equipe vermelha!')
            time.sleep(2)
        elif pergunta_6 in 'BC':
            print('Errou! Resposta certa: letra A, ponto para a equipe adversária')
            time.sleep(2)
            equipe_azul = equipe_azul + 3
os.system('cls') or None
################################################################################################
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[7;35;47m PLACAR \033[m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-=-'*20)
print(f'{jogador_001}: {equipe_azul} Pontos')
print('-=-'*20)
print(f'{jogador_002}: {equipe_vermelha} Pontos')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[1;32;40m FIM \033[m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

def enviar_email():
    corpo_email = """
    <p>Olá, muito obrigado por participar do nosso projeto! </p>
    <p>Equipe: Rafael Fassini, Davi Souza, Caio Alberto, Kawan Valente, Enrico Zivolo, Marco Antônio e Eduardo Honorio  </p>
    <p>Participação Especial: Mariana Fassini </p>
    <p>1° DS AMS </p>
    
    """

    msg = email.message.Message()
    msg['Subject'] = "Projeto Passa ou Repassa - Eletrô"
    msg['From'] = 'rafaelfassinimenoce@gmail.com'
    msg['To'] = email_des
    password = 'ptisjxdkyrgrkexz'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

enviar_email()
time.sleep(15)