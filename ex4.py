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