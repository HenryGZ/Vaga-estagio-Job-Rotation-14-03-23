'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por 
estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o 
percentual de representação que cada estado teve dentro do valor total 
mensal da distribuidora.
'''

def Porcentagem(estado, total):
    porcentagem = (estado*100)/total
    return porcentagem

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
total = sp + rj + mg + es
estados = [sp, rj, mg, es]


for estado in estados:
    print(f'porcentagem de {estado} foi de: {round(Porcentagem(estado, total),2)}')
    



