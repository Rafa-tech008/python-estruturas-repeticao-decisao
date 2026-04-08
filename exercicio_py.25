#EST.DEC_LT01.25
#Declaração de variáveis
hori:int=0
horf:int=0
mini:int=0
minf:int=0

#Início
hori=int(input("Dê a hora inicial: "))
horf=int(input("Dê a hora final: "))
mini=int(input("Dê o minuto inicial: "))
minf=int(input("Dê o minuto final: "))
inicio=(hori*60)+mini
final=(horf*60)+minf
dur=final-inicio
if (dur <= 0):
    dur = dur + 1440 #somando 24h se for negativo ou zero
horf = dur // 60 # pega as horas cheias
minf = dur % 60 # pega o que sobrou da divisão por 60 (minutos)
print("A duração do jogo foi de:", horf, "hora(s) e", minf, "minuto(s).")
   
#Fim
