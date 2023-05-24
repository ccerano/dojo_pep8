TRUE_NUMBER = "1010"


class Code_Breaker:

    def adivinar(self, numero=None):

        if TRUE_NUMBER == '':
            return 'Number is not defined'

        if numero is None or len(numero) != 4:
            return "error"

        if numero == TRUE_NUMBER:
            return True

        resultadoX = ''
        resultado_ = ''
        numero = list(numero)

        for index in range(len(numero)):
            
            print(index, numero[index])

            if TRUE_NUMBER[index] == numero[index]:
                resultadoX += 'X'

            elif numero[index] in TRUE_NUMBER:
                resultado_ += '_'

        return resultadoX+resultado_
