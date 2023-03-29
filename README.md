[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/XAjPVb7y)
# Exercício que testa idade

O script principal de vocês deve estar no arquivo `main.py`.

O testador automático vai rodar o comando `python main.py` para rodar o script.

## 📝 Instruções

- Faça um programa que recebe um valor digitado pelo usuário.
- Esse valor deve ser convertido em inteiro.
- Se o usuário digitar um número negativo: o programa deve imprimir `impossível!`
- Se o usuário digitar um número menor que 18: o programa deve imprimir `não precisa se alistar.`
- Se o usuário digitar um número maior que 18 e menor do que 65: o programa deve imprimir `Não esqueça de votar na próxima eleição.`
- Se o usuário digitar um número maior do que 65: o programa deve imprimir `Vá descansar.`
- Se nada disso acontecer, o programa deve imprimir `eita!`

Exemplos:

- Se o usuário digitar `-1`, o programa deve imprimir

  ```
  impossível!
  não precisa se alistar.
  ```

- Se o usuário digitar `18`, o programa deve imprimir

  ```
  eita!
  ```

- Se o usuário digitar `65`, o programa deve imprimir

  ```
  eita!
  ```

- Se o usuário digitar `64`, o programa deve imprimir

  ```
  Não esqueça de votar na próxima eleição.
  ```
