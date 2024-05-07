#Variables
nome = "Isa Ramos"
nivel = 10000

#Decision
if nivel < 1000: 
    nivel = "Ferro"
elif 1001 <= nivel <= 2000:
    nivel = "Bronze"
elif 2001 <= nivel <= 5000:
    nivel = "Prata"
elif 5001 <= nivel <= 7000:
    nivel = "Ouro"
elif 7001 <= nivel <= 8000:
    nivel = "Platina"
elif 8001 <= nivel <= 9000:
    nivel = "Ascendente"
elif 9001 <= nivel <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

#Output
print(f"O Herói de nome {nome} está no nível de {nivel}.")