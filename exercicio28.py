#EST.DEC_LT01.28
#Declaração de variáveis
pat:int=0
vmen:int=0

#Início
pat=int(input("O valor do produto é igual a: "))
vmen=int(input("A média mensal de vendas do produto é igual a: "))
if(vmen<500 and pat<30):
    print ("O valor do produto é igual a:",pat+(pat*0.1))
elif(vmen>=500 and vmen<1000 and pat>=30 and pat<80):
    print ("O valor do produto é igual a:",pat+(pat*0.15))
elif(vmen>=1000 and pat>=80):
    print ("O valor do produto é igual a:",pat-(pat*0.05))
else:
    print ("O valor do produto se mantém igual")

#Fim
