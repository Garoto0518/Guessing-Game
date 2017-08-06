# This is a guess the number game.
import random
guessesTaken = 0

print('Whatsabiiiii! What is your name/ Como te llamas?')
myName = input("")

x = random.randint(1, 100)
print('Interesting, ' + myName + ', Garoto as they call me is thinking of a number between 1 and 100. Can you guess what the number?')

while guessesTaken < 10:
    # print('Take a guess / Adivina el numero ') 
    y = int(input("Guess a number? / Adivina el numero. "))
    guessesTaken = guessesTaken + 1
    if y < x:
        print('Your guess is too low. /  Su respuesta es muy bajita ') 
        print("You have / Tienes " + str(10 - guessesTaken) + " chance left / turnos restantes")
    elif y > x:
        print('Your guess is too high. / Su respuesta es muy alta ')
        print("You have / Tienes " + str(10 - guessesTaken) + " chance left / turnos restantes")
    elif y == x:
        print("You Win / Ganaste")
        guessesTaken = str(guessesTaken)
        print('Good job, / Bien Hecho' + myName + '! You guessed my number in / Adivinaste mi numero' + guessesTaken + ' guesses!/ respuestas')
        break

if y != x:
    x = str(x)
    print('Nope. The number I was thinking of was/ No. El numero que estaba pensando era ' + x)
