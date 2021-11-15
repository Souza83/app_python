# O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma} '
      '\nSubtracao: {subtracao} '
      '\nMultiplicaçao: {multiplicacao} '
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
print(resultado)