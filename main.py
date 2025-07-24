from format import format_words, formats
from colors import BColors

print(f"{BColors.WARNING}==== FormatWordsFile Menu ===={BColors.RESET}")
print("1 - Formatar wordlist por padrão de serviço")
print("0 - Sair")

choice = input(f"{BColors.OK}Escolha uma opção:{BColors.RESET} ").strip()

if choice == "1":
    inputFile = input(f"{BColors.OK}Arquivo de entrada:{BColors.RESET} ").strip()
    newFile = input(f"{BColors.OK}Arquivo de saída:{BColors.RESET} ").strip()
    print("Escolha o padrão de serviço:")
    for key, (minlen, maxlen) in formats.items():
        print(f"{key} - Min {minlen} Max {maxlen}")
    option = input(f"{BColors.OK}Padrão:{BColors.RESET} ").strip()
    if option in formats:
        min_len, max_len = formats[option]
        format_words(inputFile, newFile, min_len, max_len)
        print(f"{BColors.OK}Arquivo formatado com sucesso!{BColors.RESET}")
    else:
        print(f"{BColors.FAIL}Opção inválida!{BColors.RESET}")
elif choice == "0":
    print(f"{BColors.WARNING}Saindo...{BColors.RESET}")
else:
    print(f"{BColors.FAIL}Opção inválida!{BColors.RESET}")
