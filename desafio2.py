#Solicitar o número de vitórias e derrotas ao usuário
vitorias = int(input("Digite o seu número de vitórias: "))
derrotas = int(input("Digite o seu número de derrotas: "))

#Calculadora de partidas
def calcularSaldoRankeadas(vitorias,derrotas):
  
  saldo = vitorias - derrotas
  nivel = "Imortal"

  if saldo < 10:
    nivel = "Ferro"
    
  elif saldo <= 20:
    nivel = "Bronze"

  elif saldo <= 50:
    nivel = "Prata"

  elif saldo <=80:
    nivel = "Ouro"

  elif saldo <= 90:
    nivel = "Diamante"

  elif saldo <= 100:
    nivel = "Lendário"

  return f"O Herói tem saldo de {saldo} e está no nível de {nivel}."
  
#Chamar função	
resultado = calcularSaldoRankeadas(vitorias,derrotas)
print(resultado)