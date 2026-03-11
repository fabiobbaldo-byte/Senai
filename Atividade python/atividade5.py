contador=0
soma=0
while contador < 4:
    contador+=1
    nota = float(input(f"insira a {contador} nota: "))
    soma+=nota

media= soma/contador
print("a media foi",media)
if media >=7:
    print("o aluno esta aprovado ")
else:
    print("o aluno foi reprovado")