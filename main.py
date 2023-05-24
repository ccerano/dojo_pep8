from codebreaker import Code_Breaker

intento = 0
INTENTOS_TOTALES = 10
codebreaker = Code_Breaker()

print('Jugar Codebreaker!')

while intento != INTENTOS_TOTALES:
    number = input("Numero: ")
    resolve = codebreaker.adivinar(number)
    print(resolve)

    if resolve is True:
        print("You win!!")
        break

    intento += 1
