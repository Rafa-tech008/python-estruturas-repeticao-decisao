#EST.REP_LT01.42
#Declaração de variáveis
soma=0
div=1

#Início
for i in range (1,51):
    soma=soma+(i/div)
    div=div+2
    print (i,"/",div)
print ("Valor final é igual a:",soma)

#Fim
