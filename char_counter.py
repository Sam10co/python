def contar_caracteres(s):
    contagem = {}
    for char in s:
        if char.isalpha():
            if char not in contagem:
                contagem[char] = 1
            else:
                contagem[char] += 1
    return contagem
texto = input('digite uma string:') 
resultado =contar_caracteres(texto)

print(resultado)           