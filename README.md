# Calculadora Python visual
Calculadora visual Python usando a biblioteca Tkinter
<br><br>
O código é uma implementação de uma calculadora simples usando a biblioteca <b>Tkinter</b> em Python.
<br><br>
A classe Calculadora é definida com um construtor que recebe um argumento "master", que é uma instância de Tk (uma janela). Dentro do construtor, são definidas variáveis de instância para guardar o primeiro número digitado, a operação a ser realizada e a entrada atual.
<br><br>
Em seguida, são definidos os widgets da calculadora, como os botões numéricos, botões de operação e campo de entrada. Os botões são criados usando a classe Button de Tkinter e são posicionados na janela usando o método grid.
<br><br>
A classe Calculadora também define métodos para tratar eventos dos botões, como o botão_clicado para os botões numéricos, <i>botao_operacao</i> para os botões de operação, botao_igual para o botão de igual e botao_limpar para o botão de limpar.
<br><br>
No método <i>botao_clicado</i>, o número do botão clicado é adicionado ao campo de entrada atual. No método botao_operacao, o primeiro número é armazenado e a operação a ser realizada é definida. No método botao_igual, o segundo número é lido e a operação é realizada com base na operação armazenada. O resultado é inserido no campo de entrada. No método botao_limpar, o campo de entrada é apagado e as variáveis de instância são redefinidas.
<br><br>
Finalmente, é criada uma instância da classe Calculadora e a janela é exibida usando o método mainloop de Tkinter.
