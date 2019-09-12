msg=[]
resposta=""
resp=[]
menu=True

while menu:
    op=int(input("1- adicionar um numero da mensaguem\n"
                 "2- sair\n"
                 "opção: "))
    if op==1:
        num_tep=int(input("digite o numero da mensaguem: "))

        msg.append(num_tep)

    elif op==2:
        menu=False

for i in range(len(msg)):
    if msg[i]==0:
        resposta+=" "

    elif msg[i]==1:
        resposta+="a"

    elif msg[i]==2:
        resposta+="b"

    elif msg[i]==3:
        resposta+="c"

    elif msg[i]==4:
        resposta+="d"

    elif msg[i]==5:
        resposta+="e"

    elif msg[i] ==6:
        resposta+='f'

    elif msg[i] ==7:
        resposta+="g"

    elif msg[i] ==8:
        resposta+="h"

    elif msg[i] ==9:
        resposta+="i"

    elif msg[i] ==10:
        resposta+="j"

    elif msg[i] ==11:
        resposta+="k"

    elif msg[i] ==12:
        resposta+="l"

    elif msg[i] ==13:
        resposta+="m"

    elif msg[i] ==14:
        resposta+='n'

    elif msg[i] ==15:
        resposta+="o"

    elif msg[i] ==16:
        resposta+="p"

    elif msg[i] ==17:
        resposta+="q"

    elif msg[i] ==18:
        resposta+="r"

    elif msg[i] ==19:
        resposta+="s"

    elif msg[i] ==20:
        resposta+="t"

    elif msg[i] ==21:
        resposta+="u"

    elif msg[i] ==22:
        resposta+="v"

    elif msg[i] ==23:
        resposta+="w"

    elif msg[i] ==24:
        resposta+="x"

    elif msg[i] ==25:
        resposta+="y"

    elif msg[i] ==26:
        resposta+="z"

print(resposta)
