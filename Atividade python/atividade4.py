a = float(input("insira a primeira nota: "))
b = float(input("insira a segunda nota: "))
c = float(input("insira a terceira nota: "))
d = float(input("insira a quarta nota: "))
media = (a+b+c+d)/4
print("a media foi",media)
if media >=7:
    print("o aluno esta aprovado ")
else:
    print("o aluno foi reprovado")