valor_das_taxas = {
    "USD" : 1.00,
    "BRL" : 5.44,
    "EUR" : 0.92, 
    }

lista_de_moedas_existentes =[
    "BRL -> Real",
    "USD -> Dólar",
    "EUR-> Euro",
]

def converter_moeda(valor_de_entrada, valor_de_destino, quantia):
    #transformar em dolar para ficar mais fácil para outras conversões
    valor_dolar= quantia / valor_de_entrada
    valor_moeda_convertida = valor_dolar *valor_de_destino
    return valor_moeda_convertida    


while True:

    for i in lista_de_moedas_existentes:
        print(i)


    valor_entrada = input("Digite a moeda de entrada, exemplo(   [BRL] ->Real, [USD]-> Dólar, [EUR] -> Euro, etc...): ").upper()
    valor_taxa_entrada = valor_das_taxas[valor_entrada]

    quantia_para_conversão = float(input("digite a quantia que deseja converter: "))


    valor_destino = input("digite a moeda de destino para qual a conversão será feita, exemplo(   [BRL] ->Real, [USD]-> Dólar, [EUR] -> Euro, etc...): ").upper()
    valor_taxa_destino = valor_das_taxas[valor_destino]


    resultado= converter_moeda(valor_taxa_entrada, valor_taxa_destino, quantia_para_conversão)
    print(f"A quantia de {quantia_para_conversão:.2f} {valor_entrada} convertida é: {resultado:.2f} {valor_destino}")
    
    sair= input('Se desejar sair, digite (S) e se não quiser digite (n): ').upper()
    if sair == 'S':
        print('saindo do programa...')
        break
