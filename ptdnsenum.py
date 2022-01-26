#!/usr/bin/python3

from colorama import init
from termcolor import colored
from lolpython import lol_py

init()

nome_programa = 'PT DNS Enum'
lol_py(nome_programa)

print(colored('__versao__ = 1.0.0', 'green'))
print(colored('__autor__ = pwdRoot\n','green'))

import socket
dominio = input("Digite o dominio: ")
print('\n===============================\n')
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

for nome in nomes:
        DNS = nome + "." + dominio
        try:
                print(DNS + " : " + socket.gethostbyname(DNS))
        except socket.gaierror:
                pass
