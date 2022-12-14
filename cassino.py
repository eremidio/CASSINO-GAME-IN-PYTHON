#Vamos criar um jogo simples que usa um gerador de números aleatórios para realizar uma simulação de banco.

#***********************************************************************************************************************************************************************************************
#
#
#
#0: Importando as bibliotecas necessárias
import random
import time

#***********************************************************************************************************************************************************************************************
#
#
#
#1: Apresentação e explicação do jogo:
print('\n')
print('$$$$   $$$$   $       $    $           $  $    $      $  $$$$$      $$$$')
print('$   $  $      $ $   $ $     $         $   $    $ $    $  $    $    $    $')
print('$    $ $      $  $ $  $      $       $    $    $  $   $  $     $  $      $')
print('$$$$$  $$$$   $   $   $       $     $     $    $   $  $  $     $  $      $')
print('$    $ $      $       $        $   $      $    $    $ $  $     $  $      $') 
print('$   $  $      $       $         $ $       $    $     $$  $    $    $    $')
print('$$$$   $$$$$  $       $          $        $    $      $  $$$$$      $$$$  \n\n')

print('Vamos jogar o jogo de apostas.\nQue simula um cassino onde você aposta créditos (dinheiro virtual).\nEspero que você se divirta com este jogo.\nA seguir daremos as instruções de como jogar este jogo.\n\n')

print('Eis as instruções para o jogo:\n')
print('1: O presente jogo pode ser jogado com 1 ou 2 jogadores.\n2: Cada jogador deve inserir seu nome quando solicitado.\n3: Neste jogo cada jogador começa com $5000 créditos.\n4: Seus créditos podem ser apostados durante cada rodada em dois jogos: o 21(blackjack) ou no jackpot (caça níqueis).\nO Jogo blackjack (21) está disponível apenas no modo de dois players.\n5: Todas as apostas feitas devem ser múltiplos de $100 créditos.\nAssim você pode apostar $100, $200, $1000, por exemplo, mas é irregular apostar $350, por exemplo.\nVocê será punido caso faça uma aposta irregular.\n6:Quando aparecer a mensagem ":::" na tela do computador você deve pressionar a tecla enter caso você queira continuar o jogo ou "desisto" caso você queira desistir do jogo.\n7: Para inserir uma aposta você deve inserir o número correspondente ao valor apostado.\nAssim se você quiser apostar $500 créditos você dever inserir 500, quando lhe for solicitado a aposta.\n9: Quando lhe for solicitado alguma informação siga as instruções na tela.\nA entrada de dados tem que ser condizente com a informação solicitada ou poderão ocorrer erros na execução do jogo.\n10: No jogo do jackpot você deve realizar uma aposta em um número de 5 a 10.\n Três números serão sorteados caso você acerte o resultado você será premiado, do contrário você perderá uma quantia igual ao valor apostado.\n11: No jogo do blackjack ou 21, você aposta uma quantia contra seu oponente.\nCartas numeradas de 1 a 10 serão baixadas para os dois jogadores quem chegar mais próximo de 21 na soma dos valores das cartas ganha a aposta.\n12:O jogo termina quando o jogador (ou jogadores no modo de dois players) negativar (negativarem) seus créditos ou quando um dos jogadores desistir.\n')


#***********************************************************************************************************************************************************************************************
#
#
#
#2: Funções úteis ao programa
def numeros(num:int):
 '''Função que escreve os números de 1 a 10 de forma estilizada'''
 if(num==1):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|A.--. |')
  print('\033[33m'+'| (\/) |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- A|')
  print('\033[33m'+'`------´')
 if(num==2):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|2 --. |')
  print('\033[33m'+'| (\/) |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- 2|')
  print('\033[33m'+'`------´')
 if(num==3):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|3.--. |')
  print('\033[33m'+'| :(): |')
  print('\033[33m'+'| ()() |')
  print('\033[33m'+'|  -- 3|')
  print('\033[33m'+'`------´')
 if(num==4):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|4.--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- 4|')
  print('\033[33m'+'`------´')
 if (num==5):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|5.--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| (__) |')
  print('\033[33m'+'|  -- 5|')
  print('\033[33m'+'`------´')
 if(num==6):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|6.--. |')
  print('\033[33m'+'| (\/) |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- 6|')
  print('\033[33m'+'`------´')
 if(num==7):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|7.--. |')
  print('\033[33m'+'| :(): |')
  print('\033[33m'+'| ()() |')
  print('\033[33m'+'|  -- 7|')
  print('\033[33m'+'`------´')
 if(num==8):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|8.--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- 8|')
  print('\033[33m'+'`------´')
 if(num==9):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|9.--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| (__) |')
  print('\033[33m'+'|  -- 9|')
  print('\033[33m'+'`------´')
 if(num==10):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|10--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  --10|')
  print('\033[33m'+'`------´')
 if(num==11):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|J.--. |')
  print('\033[33m'+'| :(): |')
  print('\033[33m'+'| ()() |')
  print('\033[33m'+'|  -- J|')
  print('\033[33m'+'`------´')
 if(num==12):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|Q.--. |')
  print('\033[33m'+'| (\/) |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- Q|')
  print('\033[33m'+'`------´')
 if(num==13):
  print('\033[33m'+'.------.')
  print('\033[33m'+'|K.--. |')
  print('\033[33m'+'| :/\: |')
  print('\033[33m'+'| :\/: |')
  print('\033[33m'+'|  -- K|')
  print('\033[33m'+'`------´')
 print('\033[0;0m')


#***********************************************************************************************************************************************************************************************
#
#
#
#3: Definindo a classe de jogadores 

class jogador(object):
 #Vamos instanciar os atributos da classe
 def __init__(self, nome:str, dinheiro:int, numero:int):
  '''Instanciando os atributos da classe jogador'''
  self.nome=nome
  self.dinheiro=dinheiro
  self.numero=numero #Essa variável será usada para o jogo de black jack (também conhecido como 21)

 #Destruidor da classe
 def __del__(self):
  '''Destruidor da classe'''
  print('{}  encerrou sua participação no jogo'.format(self.nome))

 #Definindo os métodos da classe
 
 #Exibindo um jogador
 def exibindo_jogador(self):
  '''Função que exibe os dados de um jogador'''
  print('\033[01m'+'\033[34m'+'Jogador {0} você tem ${1} créditos'.format(self.nome, self.dinheiro)+'\033[0;0m')

 #Definindo os jogos de black jack (ou 21)e jogo de jackpot (caça-níqueis)
 def jackpot(self):
  '''Jogo de apostas em que o jogador aposta uma quantia na tentativa de obter três números iguais'''
  #Entrando a sua aposta e sorteando três números aleátórios
  valor:int=int(input('Qual a quantia você deseja aposta nesta rodada no jackpot?\n'))
  aposta:int=int(input('Aposte em um número de 5 até 12:\n'))
  if((valor%100)!=0):
   print('Você apostou uma quantia inválida!!!\nPerdeu metade do seus créditos.\n')
   self.dinheiro=self.dinheiro/2
   self.exibindo_jogador()
  if(valor==self.dinheiro):
   print('   $    $    $     $ $  $ ')
   print('  $ $   $    $     $ $$ $ ')
   print(' $$$$$  $    $     $ $ $$ ')
   print('$     $ $$$$ $$$$  $ $  $ ')
   print('\n')
  jackpot1:int=random.randint(5,12)
  jackpot2:int=random.randint(5,12)
  jackpot3:int=random.randint(5,12)
  time.sleep(2)
  numeros(jackpot1)
  print('\n')
  time.sleep(2)
  numeros(jackpot2)
  print('\n')
  time.sleep(2)
  numeros(jackpot3)
  print('\n')
  #Resultado da jogada
  if(jackpot1==aposta and jackpot2==aposta and jackpot3==aposta):
   self.dinheiro=self.dinheiro+10*valor
   print('$   $  $$$   $   $   $   $  $ $$$$$   $$$$$  $  $ $$$$       $     $      $$$$   $  $  $$$$   $$$  $$$$$')
   print(' $ $  $   $  $   $   $   $  $   $       $    $  $ $          $    $ $    $    $  $ $   $   $ $   $   $ ')
   print('  $   $   $  $   $   $$$$$  $   $       $    $$$$ $$$$       $   $$$$$   $       $$    $   $ $   $   $ ')
   print('  $   $   $  $   $   $   $  $   $       $    $  $ $      $   $  $     $  $    $  $ $   $$$$  $   $   $ ')
   print('  $    $$$    $$$    $   $  $   $       $    $  $ $$$$    $$$  $       $  $$$$   $  $  $      $$$    $ ')
  elif (jackpot1== aposta and jackpot2==aposta and jackpot3!=aposta):
   print('\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+2*valor
  elif (jackpot1== aposta and jackpot2!=aposta and jackpot3==aposta):
   print('\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+2*valor
  elif (jackpot1!= aposta and jackpot2==aposta and jackpot3==aposta):
   print('\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+2*valor
  elif(jackpot1==aposta and jackpot2!=aposta and jackpot3!=aposta):
   print('\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+valor
  elif(jackpot1!=aposta and jackpot2==aposta and jackpot3!=aposta):
   print('\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+valor
  elif(jackpot1!=aposta and jackpot2!=aposta and jackpot3==aposta):
   print('\033[94m'+'\033[94m'+'Congratulações você ganhou!!!\n'+ '\033[0m')
   self.dinheiro=self.dinheiro+valor
  elif(jackpot1!=aposta and jackpot2!=aposta and jackpot3!=aposta):
   print('\033[31m'+'Voce perdeu!!!'+ '\033[0m')
   self.dinheiro=self.dinheiro-2*valor



 def blackjack(self):
  '''Função que define o método black para o jogador'''
  #O atributo numero deve ser zerado antes de cada rodada de black jack
  soma_parcial=0
  self.numero=0
  #inciando a partida de black jack
  print('Vamos baixar cartas numeradas de 1 a 13.\n Baixando a primeira carta {}.\n'.format(self.nome))
  carta1:int=random.randint(1,13)
  time.sleep(2)
  numeros(carta1)
  soma_parcial=carta1
  print('Até agora você tem {}.'.format(soma_parcial))
  password:str=str(input('Deseja baixar outra carta? (digite "sim" para continuar e "não" para encerrar seu turno):'))
  print('Baixando mais uma carta.\n')
  while(password=='sim'):
   carta2:int=random.randint(1,13)
   time.sleep(2)
   numeros(carta2)
   soma_parcial=soma_parcial+carta2
   print('Até agora você tem {}.'.format(soma_parcial))
   if(soma_parcial>21):
    break
   password=str(input('Deseja baixar outra carta? (digite "sim" para continuar e "não" para encerrar seu turno):'))
  self.numero=abs(21-soma_parcial)

#***********************************************************************************************************************************************************************************************
#
#
#
#4: Criando os jogadores da partida e selcionando o modo de jogo

#variável que definirá o estilio do jogo
modo:int=int(input('Digite "1" para jogar este jogo com uma pessoa somente ou "2" para jogar com dois jogadores: '))

#Criando os jogdores 
if(modo==1):
 a1:str=str(input("Jogador número 1 digite o seu nome:"))
 jogador1=jogador(a1, 5000, 0)
if(modo==2):
 a1:str=str(input("Jogador número 1 digite o seu nome:"))
 jogador1=jogador(a1, 5000, 0)
 a2:str=str(input("Jogador número 2 digite o seu nome:"))
 jogador2=jogador(a2, 5000, 0)
if(modo!=1 and modo!=2):
 print('Programa encerrou, entrada inválida.')
 quit()

#***********************************************************************************************************************************************************************************************
#
#
#
#5: Inciando o jogo
#Exibindo o status dos jogadores
if(modo==1):
 jogador1.exibindo_jogador()
if(modo==2):
 jogador1.exibindo_jogador()
 jogador2.exibindo_jogador()

#Introduziremos uma variável que permite que o jogador encerre o jogo quando ele quiser 
#desistencia:str=str(input(':::'))


#Boas vindas
if modo==1:
 print('Vamos começar a partida!!!!\n Boa sorte jogador número 1.\n')
if  modo==2:
 print('Vamos começar a partida!!!!\n Boa sorte jogador número 1 e jogador número 2.\n')

#Definindo o rumo do jogo

#Jogo de 1 só jogador
if (modo==1): 
 while(jogador1.dinheiro>0):
  #Quando o jogador desistir o jogo é encerrado
  desistencia:str=str(input(':::'))
  if(desistencia=="desisto"):
   break
  #Na modalidade com apenas um jogador apenas o jogo de jackpot é pemitido
  print('Vamos jogar o jackpot!!!\n Preparado {}?!\n'.format(jogador1.nome))
  jogador1.jackpot()
  jogador1.exibindo_jogador()


#Jogo com dois jogadores
if (modo==2):
 while(jogador1.dinheiro>0 and jogador2.dinheiro>0):
  #Jogada do jogador número 1
  #Desistinddo do jogo
  desistencia:str=str(input(':::'))
  if(desistencia=="desisto"):
   print('{0} desistiu parabéns {1}. Você é o campeão!!!\n'.format(jogador1.nome, jogador2.nome))
   break
  #Caso o jogador1 não desista, jogo segue normalmente
  print('{} é a sua vez de jogar!!!\n'.format(jogador1.nome))
  #Escolhendo qual jogo jogar
  jogada1:str=str(input('Digite "21" para jogar blackjack ou "jackpot" para jogar jackpot: '))
  #Jogando jackpot
  if(jogada1=='jackpot'):
   jogador1.jackpot()
   jogador1.exibindo_jogador()
  #Jogando blackjack
  if(jogada1=='21'):
   print('{0} prepare-se!!!!\n {1} te desafiou para uma partida de black jack.\n'.format(jogador2.nome, jogador1.nome))
   aposta1:int=int(input('{} faça a sua aposta\n'.format(jogador1.nome)))
   #Punição caso o jogador 1 faça uma aposta irregular
   if((aposta1%100)!=0):
    jogador1.dinheiro=jogador1.dinheiro-2*aposta1
    print('{} você fez uma aposta inválida!!!\n'.format(jogador1.nome))
    jogador1.exibindo_jogador()
   if(jogador2.dinheiro>=aposta1):
    jogador1.blackjack()
    jogador2.blackjack()
    if(jogador1.numero<jogador2.numero):
     jogador1.dinheiro=jogador1.dinheiro+aposta1
     jogador2.dinheiro=jogador2.dinheiro-aposta1
     print('{} venceu esta rodada de black jack!!!\n'.format(jogador1.nome))
     jogador1.exibindo_jogador()
     jogador2.exibindo_jogador()
    elif(jogador1.numero>jogador2.numero):
     jogador1.dinheiro=jogador1.dinheiro-aposta1
     jogador2.dinheiro=jogador2.dinheiro+aposta1
     print('{} venceu esta rodada de black jack!!!\n'.format(jogador2.nome))
     jogador1.exibindo_jogador()
     jogador2.exibindo_jogador()
    elif(jogador1.numero==jogador2.numero):
     print('Esta rodada de blackjack empatou!!!\n')
   elif(jogador1.dinheiro<aposta2):
    jogador2.dinheiro=jogador2.dinheiro-100
    jogador2.exibindo_jogador()
   
  #Jogada do jogador número 2
  #Desistindo do jogo
  desistencia:str=str(input(':::'))
  if(desistencia=="desisto"):
   print('{0} desistiu parabéns {1}. Você é o campeão!!!\n'.format(jogador2.nome, jogador1.nome))
   break
  #Caso o jogador1 não desista, jogo segue normalmente
  print('{} é a sua vez de jogar!!!\n'.format(jogador2.nome))
  #Escolhendo qual jogo jogar
  jogada2:str=str(input('Digite "21" para jogar blackjack ou "jackpot" para jogar jackpot: '))
  #Jogando jackpot
  if(jogada2=='jackpot'):
   jogador2.jackpot()
   jogador2.exibindo_jogador()
  #Jogando blackjack
  if(jogada2=='21'):
   print('{0} prepare-se!!!!\n {1} te desafiou para uma partida de black jack.\n'.format(jogador1.nome, jogador2.nome))
   aposta2:int=int(input('{} faça a sua aposta\n'.format(jogador2.nome)))
   #Punição caso o jogador 1 faça uma aposta irregular
   if((aposta2%100)!=0):
    jogador2.dinheiro=jogador2.dinheiro-2*aposta
    print('{} você fez uma aposta inválida!!!\n'.format(jogador2.nome))
    jogador2.exibindo_jogador()
   if(jogador1.dinheiro>=aposta2):
    jogador2.blackjack()
    jogador1.blackjack()
    if(jogador1.numero<jogador2.numero):
     jogador1.dinheiro=jogador1.dinheiro+aposta2
     jogador2.dinheiro=jogador2.dinheiro-aposta2
     print('{} venceu esta rodada de black jack!!!\n'.format(jogador1.nome))
     jogador1.exibindo_jogador()
     jogador2.exibindo_jogador()
    elif(jogador1.numero>jogador2.numero):
     jogador1.dinheiro=jogador1.dinheiro-aposta2
     jogador2.dinheiro=jogador2.dinheiro+aposta2
     print('{} venceu esta rodada de black jack!!!\n'.format(jogador2.nome))
     jogador1.exibindo_jogador()
     jogador2.exibindo_jogador()
    elif(jogador1.numero==jogador2.numero):
     print('Esta rodada de blackjack empatou!!!\n')
   elif(jogador1.dinheiro<aposta2):
    jogador1.dinheiro=jogador1.dinheiro-100
    jogador1.exibindo_jogador()


#***********************************************************************************************************************************************************************************************
#
#
#
#6.Despedida
print('Esperamos que tenha se divertido!!!')
print(' ')
print(' ')
print(' $$$  $$$$   $$$$    $   $$$       $      $$$$    $$$     * * *')
print('$   $ $   $  $   $   $  $   $     $ $     $   $  $   $    * * *')
print('$   $ $$$$   $$$$    $  $        $$$$$    $   $  $   $    * * *')
print('$   $ $   $  $   $   $  $ $$$   $     $   $   $  $   $         ')
print(' $$$  $$$$   $    $  $   $$$   $       $  $$$$    $$$     * * *')
