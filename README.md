[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XAjPVb7y)
# Exercício que testa idade

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

- Faça um programa que recebe um valor digitado pelo usuário.
- Esse valor deve ser convertido em inteiro.
- Se o usuário digitar um número negativo: o programa deve imprimir `Impossível!`
- Se o usuário digitar um número não negativo e menor que 18: o programa deve imprimir `Não precisa se alistar.`
- Se o usuário digitar um número maior que 18 e menor do que 65: o programa deve imprimir `Não esqueça de votar na próxima eleição.`
- Se o usuário digitar um número maior do que 65: o programa deve imprimir `Vá descansar.`
- Se nada disso acontecer, o programa deve imprimir `Eita!`

## 🧑‍💻 Exemplo de Execução 🧑‍💻

- Se o usuário digitar `-1`, o programa deve imprimir

  ```
  Impossível!
  ```

- Se o usuário digitar `18`, o programa deve imprimir

  ```
  Eita!
  ```

- Se o usuário digitar `65`, o programa deve imprimir

  ```
  Eita!
  ```

- Se o usuário digitar `64`, o programa deve imprimir

  ```
  Não esqueça de votar na próxima eleição.
  ```

## 🧪 Testes Automáticos 🧪

Para testar automaticamente o programa **antes** de fazer um commit e enviar o seu trabalho existem algumas formas de fazer isso.

1. executar o módulo `unittest` direto no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python -m unittest
```

2. executar o arquivo `test_main.py` no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python test_main.py
```

3. caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.
4. no seu editor de código, você pode executar o arquivo `test_main.py` e verificar o resultado dos testes no terminal.

## 🤖 Observações Importantes 🤖

- **Não altere o nome dos arquivos**. Os arquivos `test_main.py` e `main.py` precisam ter esses nomes para que os testes funcionem.
- **Não altere o nome das funções**. Os testes dependem que as funções tenham os nomes especificados no enunciado ou já escritos nos arquivos.
- **Não altere o nome dos parâmetros**. Os testes dependem que as funções tenham os parâmetros especificados no enunciado ou já escritos nos arquivos.
- **Antes de fazer um commit**, execute os testes usando um dos métodos acima para verificar se o seu programa está funcionando corretamente.
- **Caso não consiga corrigir os erros**, entre em contato com o professor ou monitores para que eles possam te ajudar.
  Para isso você deve fazer um commit com o seu trabalho incompleto e abrir uma **issue** no repositório do exercício explicando o seu problema.
