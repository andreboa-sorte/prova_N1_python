'''
3- faça um programa que peça uma nota, entre zero e dez. mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido
'''

situacao=True

while situacao:
    num=int(input("digite um numero entre 0 e 10: "))

    if (num< 0 or num>10):
        print("numero invalido\n")

    else:
        print("você digitou: ",num)
        situacao=False
