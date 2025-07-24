from colors import BColors

class WordsFile(object):
    """ evita sobrecarga de memoria e possibilita usar arquivos grandes de palavras
        avoids memory overload and makes it possible to use large word files """
    
    def __init__(self, namefile):
        self.namefile = namefile
        # Tenta abrir e ler uma linha para validar se é texto
        try:
            with open(namefile, 'r', errors='strict') as testfile:
                testline = testfile.readline()
        except UnicodeDecodeError:
            print(f'{BColors.FAIL}O arquivo informado não é um arquivo de texto válido (problema de codificação)!{BColors.RESET}')
            exit(1)
        except Exception as e:
            print(f'{BColors.FAIL}Erro ao abrir o arquivo: {e}{BColors.RESET}')
            exit(1)
        self.wordlist = self.loadContent()
        self.currentLine = ''

    def __iter__(self):
        return self

    def __next__(self):
        import re
        while True:
            self.currentLine = self.wordlist.readline()
            if not self.currentLine:
                raise StopIteration
            self.currentLine = self.currentLine.strip()
            # Ignorar linhas vazias ou só com espaços
            if not self.currentLine:
                continue
            # Ignorar linhas com caracteres inválidos (apenas letras, números e símbolos comuns)
            if not re.match(r'^[\w\d\-\_\!@#\$%\^&\*\(\)\[\]\{\}\.,;:\'"/\\]+$', self.currentLine):
                continue
            # Ignorar linhas sem nenhuma letra
            if not any(w.isalpha() for w in self.currentLine):
                continue
            return self.currentLine

    def loadContent(self):
        try:
            return open(self.namefile, 'r', errors='ignore')

        except FileNotFoundError:
            print(f'{BColors.FAIL}File {BColors.WARNING}"{self.namefile}" {BColors.FAIL}not found.{BColors.RESET}')
            exit(1)
            
        except PermissionError:
            print(f'{BColors.FAIL}Failed to open file {BColors.WARNING}"{self.namefile}", {BColors.FAIL}permission denied!{BColors.RESET}')
            exit(1)