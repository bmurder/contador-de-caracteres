import os

p = '\033[1;30m'
fb = '\033[1;107m'
fob = '\033[1;97m'
fp = '\033[1;40m'
print()
print(f'{fb}{p}leitor de caracteres{fp}')
print(f'{fob}')

caracteres = input('texto: ')

ler = len(caracteres)
print()
print()
print(f'{ler} caracteres')