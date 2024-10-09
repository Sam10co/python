def converter_temperatura(temperaturas, origem, destino):
    if origem == 'C'and destino == 'F':
        return [( temp * 9 / 5) + 32 for temp in temperaturas]
    elif origem == 'F' and destino == 'C':
        return [( temp - 32) * 5 / 9 for temp in temperaturas ]
    else:
        print('escalas invalidas')
        
lista_temperaturas = list(map(float, input("digite aas temperaturas separadas por virgula:").split(',')))
escala_origem = input("digite a escala de origem(C ou F): ").upper()
escala_destino = input("Digite a escala de destino (C ou F)").upper()

resultado = converter_temperatura(lista_temperaturas, escala_origem, escala_destino)

print(resultado)
    