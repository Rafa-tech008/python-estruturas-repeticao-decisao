#EST.REP_LT01.45
#Declaração de variáveis
soma=0

#Início
for i in range (1,16):
    if i % 2 == 0:
        soma=soma-(i/i**2)
    else:
        soma=soma+(i/i**2)
    print (i,"/",i**2)

#Fim
