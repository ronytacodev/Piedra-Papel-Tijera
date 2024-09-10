import random
from traceback import print_tb

lista = ['piedra','papel','tijera']

while True:
    computador = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('piedra,papel o tijera ? : ').lower()

        if jugador == computador:
            print('Jugador: ' + jugador)
            print('Computador: ' + computador)
            print('Empate!')

        elif jugador == 'papel':
            if computador == 'tijera':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Perdiste!')

            if computador == 'piedra':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Ganaste!')

        elif jugador == 'tijera':
            if computador == 'piedra':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Perdiste!')

            if computador == 'papel':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Ganaste!')

        elif jugador == 'piedra':
            if computador == 'papel':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Perdiste!')

            if computador == 'tijera':
                print('Jugador: ' + jugador)
                print('Computador: ' + computador)
                print('Ganaste!')

    jugar_nuevo = input('quieres seguir jugando? (si /no) : ').lower()

    if jugar_nuevo != 'si':
        break

print('Adiós')