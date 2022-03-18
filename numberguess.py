from ast import While
from pickle import TRUE
import random
guesses = 0
guess = ""

while True:
    secret_number = random.randrange(10)
    print("--------\nBoa sorte!\n")
    while guess != secret_number:
        guess = float(input("Realize seu chute: "))
        guesses += 1
        if guess < secret_number:
            print("O nome secreto é maior que o número que escolheu.\n")
        elif guess > secret_number:
            print("O nome secreto é menor que o número que escolheu.\n")
        else:
            print("Parabéns, você acertou o número em " + str(guesses) + " tentativas.\n")

