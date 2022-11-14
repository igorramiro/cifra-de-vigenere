import string
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cont=True

def ordenar_palavra_chave(chave,texto):#ordena para que a palavra chave tenha o mesmo comprimento que o texto
    '''if len(palavra_chave)!=len(texto_criptografar):#verifica se a palavra chave tem o mesmo tamanho que a criptografar
        while len(palavra_chave)<len(texto_criptografar):
            palavra_chave+=palavra_chave
        if len(palavra_chave)>len(texto_criptografar):
            palavra_chave=palavra_chave[0:len(texto_criptografar)]'''
    if len(chave)!=len(texto):
        while len(chave)<len(texto):
            chave+=chave
        if len(chave)>len(texto):
            chave=chave[0:len(texto)]
    return chave

def criptografia(texto,chave):
    controle=0
    texto_criptografado=''
    '''for i in range(0,len(texto_criptografar)):
        if texto_criptografar[i]!='_':
            letras_trocadas=list(string.ascii_lowercase)
            for x in range(0,ord(palavra_chave[i-controle])-97):
                letras_trocadas.append(letras[x])
                letras_trocadas.pop(0)
            texto_criptografado+=letras_trocadas[ord(texto_criptografar[i])-97]
        else:
            controle+=1#caso aja espaço
            #palavra_chave=palavra_chave[0:len(palavra_chave)-1]
            texto_criptografado+=' '
    print('Texto criptografado:',texto_criptografado)'''
    for i in range(0,len(texto)):
        if texto[i]!='_':
            letras_trocadas=list(string.ascii_lowercase)
            for x in range(0,ord(chave[i-controle])-97):
                letras_trocadas.append(letras[x])
                letras_trocadas.pop(0)
            texto_criptografado+=letras_trocadas[ord(texto[i])-97]
        else:
            controle+=1#caso aja espaço, essa variavel realiza um controle para manter a palavra chave
            texto_criptografado+=' '
    print('Texto criptografado:',texto_criptografado)

def descriptografia(texto,chave):
    controle=0
    texto_criptografado=''
    for i in range(0,len(texto)):
        if texto[i]!='_':
            letras_trocadas=list(string.ascii_lowercase)
            for x in range(0,ord(chave[i-controle])-97):
                letras_trocadas.append(letras[x])
                letras_trocadas.pop(0)
            texto_criptografado+=letras[letras_trocadas.index(texto[i])]
        else:
            controle+=1#caso aja espaço, essa variavel realiza um controle para manter a palavra chave
            texto_criptografado+=' '
    print('Texto descriptografado:',texto_criptografado)

while cont:
    texto_criptografar=input('Texto:')
    palavra_chave=input('Palavra chave:')
    acao=input('1-Criptografar\n2-Descriptografar\nAção:')
    texto_criptografar=texto_criptografar.replace(' ','_')
    palavra_chave=ordenar_palavra_chave(palavra_chave,texto_criptografar)
    if acao=='1':
        criptografia(texto_criptografar,palavra_chave)
    elif acao=='2':
        descriptografia(texto_criptografar,palavra_chave)
    else:
        print('Ação invalida')
    cont=True if input('Deseja continuar?S/N: ').lower()=='s' else False#verifica se o usuario deseja continuar