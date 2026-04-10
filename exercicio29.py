#EST.DEC_LT01.29
#Declaração de variáveis
poup1:int=0
rfix1:int=0
inv:int=0

#Início
poup1=int(input("O valor na poupança: "))
rfix1=int(input("O valor em renda fixa: "))
inv=int(input("O valor investido: "))
poup2=(poup1+(poup1*0.03)+inv)
rfix2=(rfix1+(rfix1*0.05)+inv)
print("O novo valor na poupança é:",poup2)
print("O novo valor em renda fixa é:",rfix2)

#Fim
