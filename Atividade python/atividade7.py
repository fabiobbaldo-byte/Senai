maior = float()
menor = float()

soma = 0
acima_100 = 0

for cont in range(10):
    temperatura = float(input(f"Digite a {cont + 1} temperatura: "))
    soma += temperatura

    if cont == 0:
        maior = temperatura
        menor = temperatura

    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura

    soma += temperatura 

    if temperatura > 100:
        acima_100 += 1

media = soma / 10

print("Resultados")
print(f"Maior temperatura é {maior}")
print(f"Menor temperatura é {menor}")
print(f"A média das temperaturas é {media}")
print(f"A temperatura ultrapassou 100 {acima_100} vezes")
maior_15 = float()
alerta = 0
soma = 0
acima_20 = float()


for cont in range (8):
    corrente = float(input(f"Digite a {cont + 1}° correntes elétricas: "))
    soma += corrente

    if corrente > maior_15:
       maior_15 = corrente


    if corrente > 20:
      acima_20 += 1 

      if corrente > 200:
         alerta += 1

    media = soma / 10

print(f"{maior_15} correntes foram maiores que 15.")
print(f"Houve {acima_20} sobrecargas")
print(f"A média das correntes é {media}")
print(f"ALERTA! A corrente ultrapassou 200A {alerta} vezes.")