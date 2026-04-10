#EST.DEC_LT01.20
#Declaração de variáveis
a: int=0
b: int=0
c: int=0

#Início
a=int(input("O valor de A é: "))
b=int(input("O valor de B é: "))
c=int(input("O valor de C é: "))
delta=((b**2)-4*a*c)
if (delta<0):
    print("Não existem raízes reais")
else:
    print ("O valor de delta é:", delta)
    x1=(-(-b) + (delta**0.5))/2*a
    x2=(-(-b) - (delta**0.5))/2*a
    print("O valor de x1 é igual a", x1)
    print("Não há raiz x1")
    print("O valor de x2 é igual:", x2)

#Fim
