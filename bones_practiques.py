#!/usr/bin/env python
'''08 Bones pràctiques. Programa que realitza la divisió entera
entre dos nombres.
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Aquest programa demana dos nombres enters a l'usuari, i procedeix a fer
la divisió entera entre aquests dos nombres, mostrant el resultat i el
residu per pantalla.
'''
__author__ = "Oriol Mangues Rubia"
__authors__ = ["Oriol Mangues Rubia"]
__email__ = "omangues@instituticaria.cat"
__date__ = "2024/10/16"

print('Aquest programa realitza una divisió entera entre dos nombres')
Dividend = int(input("Introdueix el Dividend:"))
Divisor = int(input("Introdueix el Divisor:"))
Quocient = Dividend // Divisor
Residu = Dividend % Divisor
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
