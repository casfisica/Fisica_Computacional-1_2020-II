# -*- coding: utf-8 -*-
"""
@author: camilo
"""

def count(ADN,Base):
    """Funcion que cuenta cuantas letras Base hay en ADN"""
    i=0 #Contador
    for n in ADN:
        if n == Base:
            i+=1
    return i
    
    
def pos_V1(ADN, Base):
    """Analizá la cadena de caracteres ADN en busca de la letra Base
    y entrega una lista de booleanos POS donde  POS[i]= TRUE es que 
    encontró la Base en la posición i de ADN, y POS[i]= FALSE
    lo contrario"""
    POS = []   # matches for base in dna: m[i]=True if dna[i]==base
    for n in ADN:
        if n == Base:
            POS.append(True)
        else:
            POS.append(False)
    return POS
    
    
def pos_V2(ADN, Base):
    """Reciba una cadena de caracteres ADN y una letra Base, 
    y devuelve una lista de las posiciones donde están las 
    concordancias"""
    POS=[]
    for i in range(len(ADN)):
        if ADN[i] == Base:
          POS.append(i)  
    return POS
    

def GenADN(N,bases):
    """genere una cadena de ADN de una longitud específica N, 
    desde una cadena de caracteres que contenga las bases"""
    import random #Importo la libreria random
    ADN=[]    
    for i in range(N):
        ADN.append(random.choice(bases)) #Lista de aleatorios 
        
    ADNp=''.join(ADN) #Pego la lista usando nada'' para separar
    
    return ADNp
    
def Lista_Frec(listas_ADNs):
    """Función que dada una lista de cadenas de 
    ADN (igual tamaño), entregue una lista de las 
    listas de frecuencias"""
    
    MatFre=[[0 for v in listas_ADNs[0]] for x in range(4)]

    for adn in listas_ADNs:
      for indice, base in enumerate(adn):
          if base == 'A':
              MatFre[0][indice] +=1
          elif base == 'C':
              MatFre[1][indice] +=1
          elif base == 'G':
              MatFre[2][indice] +=1
          elif base == 'T':
              MatFre[3][indice] +=1

    return MatFre
    
    
def Dict_Frec(listas_ADNs):
    """Función que dada una lista de cadenas de 
    ADN (diferente tamaño), entregue una diccionario de las 
    listas de frecuencias"""
    #Numero maximo de elementos de las listas
    n = max([len(adn) for adn in listas_ADNs])
    MatFre = {
        'A': [0]*n,
        'C': [0]*n,
        'G': [0]*n,
        'T': [0]*n,
        }
    for adn in listas_ADNs:
        for indice, base in enumerate(adn):
            MatFre[base][indice] += 1

    return MatFre
