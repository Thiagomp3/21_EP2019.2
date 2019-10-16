#BlackJack_Insper
import random


deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
cartas = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":10,"12":10,"13":10,"14":11}



#Iniciando o jogo

game = True
entrar=input("Este é o BlackJack Insper!!! Deseja entrar na mesa? (s/n): ")
carteira = 100
print("Carteira: R${0}".format(carteira))
if entrar=="s":
    rodada = 1

    while game == True:

        recebe_valores=[]
        recebe_valores_pc = []

        print("rodada:{0}".format(rodada))
        aposta_l=[]
        aposta = input("Digite o quanto quer apostar: ")

        if aposta=="fim":
            print("Foi bom jogar com você, volte sempre!!!")
            break
        
        aposta=float(aposta)
        #Feature 1
        while aposta>carteira:
            print("Você não pode apostar mais dinheiro do que tem, aposte um valor adequado")
            aposta = float(input("Digite o quanto quer apostar: "))
        #fim feature 1

        aposta_l.append(aposta)
        carteira-=aposta
        print("Carteira: R${0} ".format(carteira))

        primeira_carta = random.randint(2,14)

        segunda_carta = random.randint(2,14)

        valor_1 = cartas["{0}".format(primeira_carta)]
        valor_2 = cartas["{0}".format(segunda_carta)]
        recebe_valores.append(valor_1)
        recebe_valores.append(valor_2)

        print ("Valor das suas Cartas: ",recebe_valores)
  
        if sum(recebe_valores)==21:
            ganho = sum(aposta_l) + 1.5*sum(aposta_l)
            carteira+=ganho
            print("Você fez BlackJack, PARABENS!!!!, você ganhou {0}".format(ganho),"agora você tem: R${0}".format(carteira))
  
       
        elif sum(recebe_valores) < 21:
            p = str(input("Você não fez um Blackjack, deseja continuar?(s/n): "))

            if p=="n":
                
                primeira_carta_pc = random.randint(2,14)
                segunda_carta_pc = random.randint(2,14)

                valor_1_pc = cartas["{0}".format(primeira_carta_pc)]
                recebe_valores_pc.append(valor_1_pc)

                valor_2_pc = cartas["{0}".format(segunda_carta_pc)]
                recebe_valores_pc.append(valor_2_pc)

                if sum(recebe_valores)>sum(recebe_valores_pc):
                    print("Você chegou mais próximo que a IA, ganhou!!!")
                    print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                    ganho =  sum(aposta_l)*2
                    carteira+=ganho
                    print("Carteira: R${0}".format(carteira))

                elif sum(recebe_valores_pc)>sum(recebe_valores):
                    print("Perdeu!!! A IA chegou mais proximo de um BlackJack que você, mais sorte na próxima vez")
                    print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                    print("Carteira: R${0}".format(carteira))
                
                elif sum(recebe_valores)==sum(recebe_valores_pc):
                    print("Você empatou com a IA!!! Mais sorte na proxima vez")
                    print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                    carteira+=sum(aposta_l)
                    print("Carteira: R${0}".format(carteira))
                
            elif p=="s":

                primeira_carta_pc = random.randint(2,14)
                segunda_carta_pc = random.randint(2,14)

                valor_1_pc = cartas["{0}".format(primeira_carta_pc)]
                recebe_valores_pc.append(valor_1_pc)

                valor_2_pc = cartas["{0}".format(segunda_carta_pc)]
                recebe_valores_pc.append(valor_2_pc)

                while sum(recebe_valores_pc)<17:

                    primeira_carta_pc = random.randint(2,14)
                    valor_1_pc = cartas["{0}".format(primeira_carta_pc)]
                    recebe_valores_pc.append(valor_1_pc)

                    if sum(recebe_valores_pc)>21:
                        print("A IA estourou os 21 pontos!!! Você ganhou!!!")
                        print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                        ganho = sum(aposta_l)+sum(aposta_l)
                        carteira += ganho 
                        print("Carteira: R$ {0}".format(carteira))
                        
                    elif sum(recebe_valores_pc)==21:
                        print("A IA fez um BlackJack!!! Mais sorte na próxima!")
                        print("Carteira: R$ {0}".format(carteira))

                print("Soma Cartas IA:{0}".format(sum(recebe_valores_pc)))
                print("Soma das suas cartas: {0}".format(sum(recebe_valores)))

            
                if sum(recebe_valores_pc)<21:
                    p2 = str(input("Deseja parar com essas cartas?(s/n): "))

                    if p2 == "s":
                        if sum(recebe_valores)>sum(recebe_valores_pc):
                            print("Parabens!!! Você ganhou da IA, muito bem!!!")
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            ganho = sum(aposta_l)*2
                            carteira+=ganho
                            print("Carteira: R$ {0}".format(carteira))
                        
                        elif sum(recebe_valores)==sum(recebe_valores_pc):
                            print("Você empatou com a IA!!! Mais sorte na próxima!")
                            carteira+=sum(aposta_l)
                            print("Carteira: R$ {0}".format(carteira))
                        
                        else:
                            print("Você perdeu da IA!!! Mais sorte na próxima!")
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            print("Carteira: R$ {0}".format(carteira))

                    elif p2 == "n":

                        primeira_carta = random.randint(2,14)
                        valor_1 = cartas["{0}".format(primeira_carta)]
                        recebe_valores.append(valor_1)
                        print("Sua soma: {0}" .format(sum(recebe_valores)))

                        #regra do Ás:
                        if sum(recebe_valores)>21:
                            for a in range(len(recebe_valores)):
                                if recebe_valores[a]==11:
                                    recebe_valores[a]=1

                        if sum(recebe_valores)>21:
                            print("Você estourou os 21 pontos, mais sorte na próxima!!!")
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            print("Carteira: R$ {0}".format(carteira))
                            p3 = "n"

                        else:
                            p3 = str(input("Deseja continuar?(s/n): "))

                        while p3 == "s":
                            primeira_carta = random.randint(2,14)
                            valor_1 = cartas["{0}".format(primeira_carta)]
                            recebe_valores.append(valor_1)
                            print("Sua soma: {0}" .format(sum(recebe_valores)))

                            if sum(recebe_valores)>21:
                                print("Você estourou os 21 pontos, mais sorte na próxima!!!")
                                print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                                print("Carteira: R$ {0}".format(carteira))
                                p3 = "n"

                            else:
                                p3 = str(input("Deseja continuar?(s/n): "))
                                
                        if sum(recebe_valores)>sum(recebe_valores_pc) and sum(recebe_valores)<21:
                            print("PARABÉNS você ganhou da IA!!!!")
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            ganho = sum(aposta_l)*2
                            carteira+=ganho 
                            print("Carteira: R$ {0}".format(carteira))
                        
                        elif sum(recebe_valores)<sum(recebe_valores_pc) and sum(recebe_valores)<21:
                            print("Você perdeu!!! Mais sorte na próxima tentativa ")
                            print ("Soma IA: {0} ".format(sum(recebe_valores_pc)))
                            print("Carteira: R$ {0}".format(carteira))

                        elif  sum(recebe_valores)==sum(recebe_valores_pc):
                            print("Você empatou com a IA !!! Mais sorte na próxima!")
                            print("Carteira: R$ {0}".format(carteira))
        #Feature 2
        if carteira<=0:
            print("Você ficou sem dinheiro para apostar!!! Volte quando conseguir mais!")
            game = False
        
        rodada+=1

else:
    print("Volte quando quiser jogar!!")



            
