# Importação de biblioteca
import os
from datetime import date
import time

# Entrada de dados
nome = input("Informe um nome: ")
idade = int(input("Informe sua idade: "))
data = f"{date.today().day}/{date.today().month}/{date.today().year}"

# Limpa console
os.system("cls")

# Inicio do loop
while True:
    print(f"{"*"*30} Lista de Filmes {"*"*30}")
    print(f"   Dia: {data}\n")
    print("Sala 1 - O Poderoso Chefão - 14 anos") 
    print("Sala 2 - Um Sonho de Liberdade - 16 anos") 
    print("Sala 3 - A Lista de Schindler - 16 anos") 
    print("Sala 4 - Forrest Gump - O Contador de Histórias - 14 anos") 
    print("Sala 5 - O Rei Leão - Livre") 

    # Escolha do usuário
    sala = input("\nSala desejada: ")

    # Limpa console
    os.system("cls")

    # Verifica a sala escolhida
    match sala:
        case "1":
            idade_minima = 14
            filme = "O Poderoso Chefão"
        case "2": 
            idade_minima = 16
            filme = "Um Sonho de Liberdade"
        case "3": 
            idade_minima = 16
            filme = "A Lista de Schindler"
        case "4": 
            idade_minima = 14
            filme = "Forrest Gump - O Contador de Histórias"
        case "5": 
            idade_minima = 0
            filme = "O Rei Leão"
        case _:
            print('Sala inexistente, favor selecionar outra opção.')
            continue

    # Verificação da idade
    if idade >= idade_minima:
        print(f"Ingresso impresso no dia: {data}.\n")
        print(f"Sala: {sala}.")
        print(f"Usuário: {nome}.")
        os.system("cls")
        print("\nCompra confirmada! Aguarde a impressão do ingresso.")
        time.sleep(3)
        print("Retire o Ingresso. Tenha um Ótimo Filme!")
        break
    else:
        print(f"Você não possui a idade minima para o filme {filme}")
        print("Favor selecionar outro filme!")
        continue