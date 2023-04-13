'''
3) Dado um vetor que guarda o valor de faturamento diário de 
uma distribuidora, faça um programa,
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior 
à média mensal.'''

from statistics import mean
import json

def MaiorQueAMedia(valor):
    precos = []
    dias = 0
    for valor in valores:
        precos.append(valor['valor'])
    print(f'a media dos preços é:{round(mean(precos),2)}')
    for valor in precos:
        if valor > mean(precos):
            dias += 1
    print(f'{dias} com o faturamento maior que a média mensal')

def MenorValor(valor):
    precos = []
    for valor in valores:
        precos.append(valor['valor'])
    print(f'menor valor: {round(min(precos),2)}')
    
def MaiorValor(valor):
    precos = []
    for valor in valores:
        precos.append(valor['valor'])
    print(f'maior valor: {round(max(precos),2)}')

def Ler(valores, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        Salvar(valores, caminho_arquivo)
    return dados

def Salvar(valores, caminho_arquivo):
    dados =  valores
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(valores, arquivo, indent=2, ensure_ascii=False)
    return dados
    
CAMINHO_ARQUIVO = 'dados.json'

valores = Ler([], CAMINHO_ARQUIVO)

while True:
    print('1 - maior valor')
    print('2 - menor valor')
    print('3 - dias com valores maiores que a média')
    print('4 - sair')
    comando = int(input('opção: '))
    
    if (comando == 1):
        MaiorValor(valores)
    elif(comando == 2):
        MenorValor(valores)
    elif(comando == 3):
        MaiorQueAMedia(valores)
    elif(comando == 4):
        break
    else:
        print('digite um numero dentro das opções listadas')
        
        