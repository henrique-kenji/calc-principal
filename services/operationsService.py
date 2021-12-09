import math

def elementarFunction (var_1, var_2, operacao):
    if(operacao == '+'):
        result = float(var_1 + var_2)
        operacao_especifica = 'ADICAO'
    elif(operacao == '-'):
        result = float(var_1 - var_2)
        operacao_especifica = 'SUBTRACAO'
    elif(operacao == '*'):
        result = float(var_1 * var_2)
        operacao_especifica = 'MULTIPLICACAO'
    elif(operacao == '/'):
        result = float(var_1 / var_2)
        operacao_especifica = 'DIVISAO'
    else:
        result = 'Resultado inválido'
    resultado = [result, operacao_especifica, "ELEMENTAR"]
    return resultado

def transcendentFunction (var_1, operacao):
    if(operacao == 'LOG'):
            result = float(math.log(var_1))
            op_especifica = 'LOG'
    elif(operacao == '1/X'):
        result = float(1/var_1)
        op_especifica = '1/X'
    else:
        result = 'Resultado inválido'
    resultado = [result, op_especifica, "TRANSCENDENTE"]
    return resultado
