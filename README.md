https://www.youtube.com/embed/EXt5x-1ZlGE

🚀 FormatWordFile
▶️ Veja o vídeo no YouTube
version = '2.0'


# 🚀 FormatWordFile

<details>
  <summary>▶️ Clique para ver o vídeo de demonstração</summary>
  
  <p align="center">
    <a href="https://www.youtube.com/watch?v=EXt5x-1ZlGE">
      <img src="https://img.youtube.com/vi/EXt5x-1ZlGE/0.jpg" alt="Demo Video" width="480"/>
    </a>
  </p>
</details>

---

__version__ = '1.0'

---

## ✨ Funcionalidades

- 🔒 Formatação por padrões de serviço (ex: SSH, WIFI/WPA, SQL Server, AWS, Windows)
- 🧹 Remoção de caracteres especiais e espaços em branco
- 📏 Filtragem por tamanho mínimo e máximo conforme o serviço escolhido
- 🖥️ Menu interativo para facilitar o uso

---

## ⚙️ Como funciona

1. O usuário inicia o script principal (`main.py`).
2. Um menu interativo é exibido, permitindo escolher a ação desejada.
3. Ao escolher "Formatar wordlist por padrão de serviço", o usuário informa o arquivo de entrada, o arquivo de saída e o padrão de serviço.
4. O script filtra e formata as palavras do arquivo conforme o padrão escolhido (tamanho mínimo/máximo, remoção de caracteres especiais e espaços).
5. O resultado é salvo no arquivo de saída.

---

## 🧩 Lógica do Projeto

- O menu principal chama funções dos outros scripts para realizar a formatação.
- Cada padrão de serviço possui regras de tamanho específicas.
- O processamento é feito linha a linha, evitando sobrecarga de memória.
- O código é modular e fácil de expandir para novos padrões.

---

## 🇧🇷 Exemplo de uso

```bash
python main.py
```

- Escolha a opção desejada no menu.
- Informe os arquivos e o padrão de serviço.
- O arquivo formatado será gerado conforme as regras escolhidas.

---

## 👤 Autor: [@gsLukas](https://github.com/gsLukas)
## 🤝 Colaborador: [@zNairy](https://github.com/zNairy)

---

## 📺 Demonstração

[![Demo Video](https://img.youtube.com/vi/EXt5x-1ZlGE/0.jpg)](https://www.youtube.com/watch?v=EXt5x-1ZlGE)

---

> 💡 Dica: Para adicionar novos padrões de serviço, basta editar o dicionário `formats` em `format.py` e o menu em `main.py`.
