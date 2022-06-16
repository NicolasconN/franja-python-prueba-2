def buscar_palabra_larga(lista_palabras):  
    palabra_mas_larga =  max(lista_palabras, key=len)
    return palabra_mas_larga
    for palabras in lista_palabras:    
          print(palabras, len(palabras))  


palabras = input('Ingresa la frase: ')  
lista_palabras = palabras.split()  
buscar_palabra_larga(lista_palabras) 
