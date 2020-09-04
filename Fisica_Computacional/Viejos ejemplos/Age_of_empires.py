# -*- coding: utf-8 -*-
"""
Created on Sun Sep 8 21:20:42 2016

@author: camilo
"""

class Personaje:
    '''Clase contenga los atributos vida, 
    posición y velocidad, y los métodos 
    recibir_ataque, que reduzca la vida 
    según una cantidad recibida y lance 
    una advertencia si la vida pasa a ser 
    menor o igual que cero, y mover que
    reciba una dirección y se mueva en 
    esa dirección la cantidad indicada 
    por velocidad'''
    
    vida=0
    posicion=[0,0] #primera coordenada x horizontal, segunda y vertical
    velocidad=[0,0]
    
    def __init__(self, vida=0, posicion=[0,0], velocidad=[0,0]):
         self.vida=vida
         self.posicion=posicion
         self.velocidad=velocidad
         
    def recibir_ataque(self,ataque):
        self.vida= self.vida-ataque
        if self.vida <= 0:
            print("Se murio!!")
        return
        
    def mover(self, direccion):
        '''1: arriva, 2: derecha, 3: abajo, 4:Izquierda'''
        if direccion==1:
            self.posicion[1]=self.posicion[1]+self.velocidad[1]
        elif direccion==2:
            self.posicion[0]=self.posicion[0]+self.velocidad[0]
        elif direccion==3:
            self.posicion[1]=self.posicion[1]-self.velocidad[1]
        elif direccion==4:
            self.posicion[0]=self.posicion[0]-self.velocidad[0]
        else:
            print('Solo admite direcciones del 1 al 4')
            
class Soldado(Personaje):
    '''Clase Soldado que herede de Personaje, y agregue el 
    atributo ataque y el método atacar'''
    
    ataque=0

    def __init__(self, vida=0, posicion=[0,0], velocidad=[0,0],ataque=0):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad   
        self.ataque=ataque    
        
    def atacar(self, other):
        '''el método atacar (usar random), que 
        reciba otro personaje, al que le debe hacer el daño 
        indicado por el atributo ataque'''
        other.recibir_ataque(self.ataque)
        
class Campesino(Personaje):
    '''Escribir una clase Campesino que herede de Personaje, y 
    agregue el atributo cosecha y el método cosechar, que devuelva 
    la cantidad cosechada.'''
    
    cosecha=0
    
    def __init__(self, vida=0, posicion=[0,0], velocidad=[0,0],cosecha=0):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad   
        self.cosecha=cosecha  
        
    def cosechar(self):
        return self.cosecha