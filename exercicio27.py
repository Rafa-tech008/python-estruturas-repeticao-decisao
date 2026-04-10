#EST.DEC_LT01.27
#Declaração de variáveis
t:int=0
v:int=0
d:int=0

#Início
t=int(input("O tempo que durou o trajeto em minutos: "))
v=int(input("Quantas voltas você fez: "))
d=int(input("A distância percorrida no trajeto em metros: "))
vm=(((d/1000)*v)/(t/60))
print("A velocidade média equivale a",vm)

#Fim
