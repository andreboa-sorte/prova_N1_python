'''
desenvolva um gerador , capaz de gerar a tabuada de qualquer inteiro entre 1 a 10. o usuário deve informar de qual
número ele deseja ver a tabuada. a sauda ser conforme o exemplo
°tabuada de 5:
°5x1=5
°5x2=10
°...
°5x10=50
'''

lista_aux=[1,2,3,4,5,6,7,8,9,10]
lista_tabuada=[]


num=int(input("digite um numero que se deseja ver a tabuada: "))

for i in range(len(lista_aux)):
    aux=num*lista_aux[i]
    lista_tabuada.append(aux)
i=1

for j in range(len(lista_tabuada)):
    print(num, " x ", i ,' = ',lista_tabuada[j])
    i=i+1