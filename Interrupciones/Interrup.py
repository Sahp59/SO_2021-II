# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:29:14 2021

@author: sahp
"""

import time
import sys

def main():
   f = open('Texto.txt','r')
   mensaje = f.read()
   f.close()

   acomodador = []
   acomodador = mensaje.split()
   
   print("Para PAUSAR presione Ctrl+c, si no presiona Ctrl+c en 3 segundos el programa se detendra")
   print("Para REINICIAR presione de nuevo Ctrl+c\n")
   
   imprimirLento(acomodador)
   
      
def imprimirLento(texto):
   try:
      for palabra in texto:
         for lento in palabra:
            print(lento,end=(""))
            time.sleep(0.1)
         print(end=(" "))
   except KeyboardInterrupt:
      try:
         print("\nSe ha PAUSADO")
         if (time.sleep(3)):
            print("\nSe ha DETENIDO")
            sys.exit()
      except KeyboardInterrupt:
         print("\nSe ha REINICIADO")
         imprimirLento(texto)
main()