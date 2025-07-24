#!/usr/bin python3

__author__ = '@gsLukas'
__colaborator__ = '@zNairy'
__contact__ = 'Discord: gsLukao#6445 | zNairy#7181 || Github: https://github.com/gsLukas | https://github.com/zNairy/'
__version__ = '1.0'

from colors import BColors
from wordsFile import WordsFile
from time import sleep
from os import system
from subprocess import getoutput

system("clear")

print ("\t\t EN-US// Welcome to FormatWordFile \n\t\tPT-BR// Bem vindo ao FormatWordFile\n" )
print (f"\t\t      by {__author__} and {__colaborator__}" )

sleep(2)
system('clear')

print (f'{BColors.WARNING}EN-US// Enter name of the WordFile to format \nPT-BR// Inserir o nome do WordFile para formatar: {BColors.RESET}')
print (f"\nCurrent Directory: [{getoutput('pwd')}]")

inputFile = input(f"{BColors.OK}Path: {BColors.RESET}")

file = WordsFile(inputFile) # tentando abrindo arquivo

print (f'{BColors.WARNING}EN_US// Name for new WordFile\nPT_BR// Nome para novo WordFile {BColors.RESET}')
newFile = input(f'{BColors.OK}New Path:{BColors.RESET}')

#Menu choice

print (f"{BColors.WARNING}\nEN-US// Standard WIFI/wpa format \nPT_BR// Formato padrão WIFI/wpa (Min 8 Max 64): Press 1{BColors.RESET}")
print (f"{BColors.WARNING}\nEN-US// Standard SSH format \nPT_BR// Formato padrão SSH (Min 1 Max 256): Press 2{BColors.RESET}")
print (f"{BColors.WARNING}\nEN-US// Standard Windows format \nPT_BR// Formato padrão Windows (Min 1 Max 14): Press 3{BColors.RESET}")
print (f"{BColors.WARNING}\nEN-US// Standard AWS/SQL Server format \nPT_BR// Formato padrão AWS/SQL Server (Min 8 Max 128): Press 4{BColors.RESET}")

option = input(f"{BColors.OK}Select:{BColors.RESET} ").strip()


def format_words(input_file, output_file, min_len, max_len):
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}')
    with open(output_file, 'w') as out:
        for word in WordsFile(input_file):
            word = "".join(w for w in word.split())
            if min_len <= len(word) <= max_len:
                out.write(word + "\n")

formats = {
    "1": (8, 64),      # WIFI/wpa
    "2": (1, 256),     # SSH
    "3": (1, 14),      # Windows
    "4": (8, 128),     # AWS/SQL Server
}

if option in formats:
    min_len, max_len = formats[option]
    format_words(inputFile, newFile, min_len, max_len)
else:
    print(f"{BColors.FAIL}Invalid Option!{BColors.RESET}")
