situacao=True

while situacao:
    num=int(input("digite um numero entre 0 e 10: "))

    if (num< 0 or num>10):
        print("numero invalido\n")

    else:
        print("você digitou: ",num)
        situacao=False
