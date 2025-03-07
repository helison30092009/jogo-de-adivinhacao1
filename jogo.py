import random
def jogar ():
    print(**********)
    print("Bem-vindos ao jogo de Adivinhação!")
    print(**********)

    numero_secreto = random( random.random()*100)
    total_de_tentativas = 3
    pontos = 1000
    print(" qual o nivel de dificultade")
    print("(1) facil(2) medio(3) dificil")

    nivel = int(input("defina o nivel:"))

    if(nivel==):
        total_de_tentativas = 20
        elif(nivel==2):
            total_de_tentativas =10

else(nivel==3):
   total_de_tentativas =5
for rodada in range(1, total_de_tentativas +1):
print("tentativas {} de {}". format ( rodada,total_de_tentativas))
#entrada do usario 
chute_str = input (" digite um numero entre 1 a 100 ")
print("voce digitou", chute_str)
chute = int(chute_str)

#validação da entrada
if (chute<1 or> 100):
print("voce deve digitar um numero entre  um 1 e 100!")
continue 
acertou = chute == numero_secreto
maior=chute > numero_secreto
menor =chute < numero_secreto

if (acertou)
print "voce acertou e fez"