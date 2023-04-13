'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''


teste = 'pao'
nova = []
i = 0
lista = []

for c in teste:
    lista.append(c)

while i < len(teste):
    nova.insert(0, lista[i])
    i +=1
print(nova)