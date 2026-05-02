# Inicialização das variáveis de controle

somaTemp = 0
qtdMesesEscal = 0
mesMaisEscal = 0
mesMenosQuente = 0
maiorTemp = 0
menorTemp = 50
totalMeses = 12

# Entrada e validação dos dados (mês e temperatura)

meses = []
for num in range (1,13):
  while True:
    mes = int(input("Informe o número do mês de (1 a 12):"))
    if mes < 1 or mes > 12:
      print("Mês informado é inválido. Digite novamente.")
    elif mes in meses:
      print("Mês já informado. Digite novamente.")
    else:
      meses.append(mes)
      break
  while True:
    temperatura = float(input(f"Informe a temperatura máxima registrada para o mês {mes} (entre -60ºC a 50ºC):"))
    if temperatura < -60 or temperatura > 50:
      print("Temperatura informada é inválida. Digite novamente.")
    else:
      break

# Conversão do número do mês para nome por extenso

  if mes == 1: nomeMes = "Janeiro"
  if mes == 2: nomeMes = "Fevereiro"
  if mes == 3: nomeMes = "Março"
  if mes == 4: nomeMes = "Abril"
  if mes == 5: nomeMes = "Maio"
  if mes == 6: nomeMes = "Junho"
  if mes == 7: nomeMes = "Julho"
  if mes == 8: nomeMes = "Agosto"
  if mes == 9: nomeMes = "Setembro"
  if mes == 10: nomeMes = "Outubro"
  if mes == 11: nomeMes = "Novembro"
  if mes == 12: nomeMes = "Dezembro"

# Cálculo da média anual das temperaturas máximas

  somaTemp += temperatura
  mediaTemp = somaTemp / totalMeses

# Identificação de meses escaldantes (>33°C)

  if temperatura > 33:
    qtdMesesEscal += 1

# Idenfificação do mês mais quente

  if temperatura > maiorTemp:
    maiorTemp = temperatura
    mesMaisEscal = nomeMes

# Idenfificação do mês menos quente

  if temperatura < menorTemp:
    menorTemp = temperatura
    mesMenosQuente = nomeMes

# Exibição dos resultados

print(f"Temperatura média máxima anual: {mediaTemp:.1f}ºC")

if qtdMesesEscal > 0:
  print(f"Quantidade de meses escaldantes: {qtdMesesEscal}.")
else:
 print(f"Quantidade de meses escaldantes: Nenhum.")

if mesMaisEscal in ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]:
  print(f"O mês mais escaldante do ano foi {mesMaisEscal}. A temperatura foi de {maiorTemp}ºC")
else:
  print(f"Não há mês escaldante registrado.")

if mesMenosQuente in ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]:
  print(f"O mês menos quente do ano foi {mesMenosQuente}. A temperatura foi de {menorTemp}ºC")
else:
  print(f"Não há mês menos quente registrado.")

