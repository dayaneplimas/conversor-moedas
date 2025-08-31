## 💱 Conversor de Moedas

### 📋 Sobre o projeto

Este é um conversor simples de moedas feito em Python, que permite converter valores entre **Real, Dólar e Euro** diretamente no terminal.

---

### ⚙️ O programa oferece um menu interativo onde o usuário escolhe a conversão desejada, informa o valor, e recebe o resultado formatado.

- 🐍 O programa é um **conversor simples de moedas** feito em Python, que roda no terminal.
- 📜 Ele usa uma função chamada `mostrar_menu()` para mostrar as opções de conversão para o usuário.
- 🔢 Outra função chamada `converter(valor, taxa)` faz a conta da conversão, multiplicando o valor pelo câmbio (taxa).
- 🔄 O programa usa um **loop infinito** (`while True`) para continuar rodando até o usuário escolher sair.
- 🎯 O usuário escolhe a operação (por exemplo, Real para Dólar) digitando um número.
- 💵 Depois, o programa pede para o usuário digitar o valor a ser convertido.
- 🔍 Dependendo da escolha, ele chama a função `converter()` com o valor e a taxa de câmbio correspondente:
  
  - 🇧🇷 Real para Dólar usa taxa **0.19** (ou seja, 1 Real = 0.19 Dólar)
  - 🇧🇷 Real para Euro usa taxa **0.16**
  - 🇺🇸 Dólar para Real usa taxa **5.3**
  - 🇪🇺 Euro para Real usa taxa **6.2**
  
- 📊 O resultado da conversão é mostrado na tela formatado com duas casas decimais.
- ⚠️ Se o usuário digitar uma opção inválida, o programa avisa e pede para tentar de novo.
- ❌ Quando o usuário digita "0", o programa encerra mostrando uma mensagem de despedida.

---

### 🧩 O que cada parte do código faz

1. 🖥️ **Função `mostrar_menu()`**:  
   Exibe as opções para o usuário escolher a conversão.

2. 🧮 **Função `converter(valor, taxa)`**:  
   Multiplica o valor pelo câmbio para fazer a conversão.

3. 🔄 **Loop `while True`:**  
   Mantém o programa rodando até o usuário decidir sair.

4. ⌨️ **Entrada `input()`**:  
   Recebe a opção do menu e o valor a ser convertido.

5. 🔀 **Estrutura condicional `if/elif/else`**:  
   Decide qual taxa usar e o que mostrar com base na opção escolhida.

---

### 🚀 Como usar este programa

1. 🖥️ Abra o terminal no seu computador.
2. 📂 Navegue até a pasta onde o arquivo `conversor.py` está salvo.
3. ▶️ Execute o programa digitando:

```

python conversor.py

```
4. 📋 Veja o menu que aparece e digite o número da conversão desejada (ex: 1 para Real para Dólar).
5. 🔢 Digite o valor que quer converter (apenas números).
6. 💡 O programa mostrará o resultado da conversão.
7. ❌ Para sair, digite 0.

---

