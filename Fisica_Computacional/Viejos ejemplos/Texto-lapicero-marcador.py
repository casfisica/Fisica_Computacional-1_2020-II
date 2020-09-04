# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:35:32 2016
Papel, lapiz y marcador
@author: camilo
"""

class Papel:
    tex=""
    def __init__(self, texto):
        self.tex=texto
        
    def __str__(self):
        return self.tex
        
    def __repr__(self):
        return self.tex
        
    def Escribir(self, Texto):
        self.tex =  self.tex + Texto
        return    
        
class Lapicero:
    tinta=0
    def __init__(self, tinta_inicial=0):
        self.tinta=tinta_inicial
        return        
        
    def escribir(self, Papel, Text):
        for i in Text:
            Papel.Escribir(i)       
            self.tinta-=1
            if self.tinta==0:
                print("La tinta se acabo")
                break
        return

class Marcador(Lapicero):
    def Recargas(self, extra):
        self.tinta= self.tinta +extra
        return
        
