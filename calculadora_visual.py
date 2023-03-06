from tkinter import *

class Calculadora:
    def __init__(self, master):
        self.primeiro_numero = None
        self.operacao = None

        master.title("Calculadora")

        # Criando os botões numéricos
        self.botao_1 = Button(master, text="1", padx=40, pady=20, command=lambda: self.botao_clicado(1))
        self.botao_2 = Button(master, text="2", padx=40, pady=20, command=lambda: self.botao_clicado(2))
        self.botao_3 = Button(master, text="3", padx=40, pady=20, command=lambda: self.botao_clicado(3))
        self.botao_4 = Button(master, text="4", padx=40, pady=20, command=lambda: self.botao_clicado(4))
        self.botao_5 = Button(master, text="5", padx=40, pady=20, command=lambda: self.botao_clicado(5))
        self.botao_6 = Button(master, text="6", padx=40, pady=20, command=lambda: self.botao_clicado(6))
        self.botao_7 = Button(master, text="7", padx=40, pady=20, command=lambda: self.botao_clicado(7))
        self.botao_8 = Button(master, text="8", padx=40, pady=20, command=lambda: self.botao_clicado(8))
        self.botao_9 = Button(master, text="9", padx=40, pady=20, command=lambda: self.botao_clicado(9))
        self.botao_0 = Button(master, text="0", padx=40, pady=20, command=lambda: self.botao_clicado(0))

        # Criando os botões de operação
        self.botao_soma = Button(master, text="+", padx=39, pady=20, command=lambda: self.botao_operacao("+"))
        self.botao_subtracao = Button(master, text="-", padx=41, pady=20, command=lambda: self.botao_operacao("-"))
        self.botao_multiplicacao = Button(master, text="*", padx=40, pady=20, command=lambda: self.botao_operacao("*"))
        self.botao_divisao = Button(master, text="/", padx=41, pady=20, command=lambda: self.botao_operacao("/"))
        self.botao_igual = Button(master, text="=", padx=91, pady=20, command=self.botao_igual)
        self.botao_limpar = Button(master, text="C", padx=91, pady=20, command=self.botao_limpar)

        # Posicionando os botões na janela
        self.botao_1.grid(row=3, column=0)
        self.botao_2.grid(row=3, column=1)
        self.botao_3.grid(row=3, column=2)

        self.botao_4.grid(row=2, column=0)
        self.botao_5.grid(row=2, column=1)
        self.botao_6.grid(row=2, column=2)

        self.botao_7.grid(row=1, column=0)
        self.botao_8.grid(row=1, column=1)
        self.botao_9.grid(row=1, column=2)
        self.botao_0.grid(row=4, column=0)
        self.botao_soma.grid(row=5, column=0)
        self.botao_subtracao.grid(row=6, column=0)
        self.botao_multiplicacao.grid(row=6, column=1)
        self.botao_divisao.grid(row=6, column=2)

        self.botao_igual.grid(row=5, column=1, columnspan=2)
        self.botao_limpar.grid(row=4, column=1, columnspan=2)

        # Criando o campo de entrada
        self.campo_entrada = Entry(master, width=35, borderwidth=5)
        self.campo_entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def botao_clicado(self, numero):
        valor_atual = self.campo_entrada.get()
        self.campo_entrada.delete(0, END)
        self.campo_entrada.insert(0, str(valor_atual) + str(numero))

    def botao_operacao(self, operacao):
        self.primeiro_numero = float(self.campo_entrada.get())
        self.operacao = operacao
        self.campo_entrada.delete(0, END)

    def botao_igual(self):
        segundo_numero = float(self.campo_entrada.get())
        self.campo_entrada.delete(0, END)

        if self.operacao == "+":
            resultado = self.primeiro_numero + segundo_numero
        elif self.operacao == "-":
            resultado = self.primeiro_numero - segundo_numero
        elif self.operacao == "*":
            resultado = self.primeiro_numero * segundo_numero
        else:
            resultado = self.primeiro_numero / segundo_numero

        self.campo_entrada.insert(0, resultado)

    def botao_limpar(self):
        self.campo_entrada.delete(0, END)
        self.primeiro_numero = None
        self.operacao = None

root = Tk()
calculadora = Calculadora(root)
root.mainloop()
