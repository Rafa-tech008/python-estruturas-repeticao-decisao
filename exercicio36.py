#EST.DEC_LT01.36
#Declaração de variáveis
x:int=0

#Início
soma=1
fat=1
x=int(input("O valor de x é igual a: "))
for i in range (1,x+1):
    fat=fat*i
    soma=soma+(1/fat)
print ("O valor equivale a:",soma)

#Fim
