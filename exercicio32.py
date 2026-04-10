#EST.DEC_LT01.32
#Declaração de variáveis
x:int=0

#Início
x=int(input("Dê um valor para X: "))
fat=1
while x>1:
    fat=fat*x
    x= x-1
print("O fatorial da questão é:",fat)

#Fim
