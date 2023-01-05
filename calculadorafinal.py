import tkinter as tk

class Calculadora:
  def __init__(self):
    self.janela = tk.Tk()
    self.janela.title("Calculadora")

    # Criar os botões para os números
    self.botao_0 = tk.Button(self.janela, text="0", command=lambda: self.inserir_numero("0"))
    self.botao_1 = tk.Button(self.janela, text="1", command=lambda: self.inserir_numero("1"))
    self.botao_2 = tk.Button(self.janela, text="2", command=lambda: self.inserir_numero("2"))
    self.botao_3 = tk.Button(self.janela, text="3", command=lambda: self.inserir_numero("3"))
    self.botao_4 = tk.Button(self.janela, text="4", command=lambda: self.inserir_numero("4"))
    self.botao_5 = tk.Button(self.janela, text="5", command=lambda: self.inserir_numero("5"))
    self.botao_6 = tk.Button(self.janela, text="6", command=lambda: self.inserir_numero("6"))
    self.botao_7 = tk.Button(self.janela, text="7", command=lambda: self.inserir_numero("7"))
    self.botao_8 = tk.Button(self.janela, text="8", command=lambda: self.inserir_numero("8"))
    self.botao_9 = tk.Button(self.janela, text="9", command=lambda: self.inserir_numero("9"))
    self.botao_ponto = tk.Button(self.janela, text=".", command=lambda: self.inserir_numero("."))

    # Criar os botões para os sinais de operação
    self.botao_soma = tk.Button(self.janela, text="+", command=lambda: self.inserir_operador("+"))
    self.botao_subtracao = tk.Button(self.janela, text="-", command=lambda: self.inserir_operador("-"))
    self.botao_multiplicacao = tk.Button(self.janela, text="*", command=lambda: self.inserir_operador("*"))
    self.botao_divisao = tk.Button(self.janela, text="/", command=lambda: self.inserir_operador("/"))

    # Criar o botão de igualdade e o botão de limpar
    self.botao_igualdade = tk.Button(self.janela, text="=", command=self.calcular)
    self.botao_limpar = tk.Button(self.janela, text="Limpar", command=self.limpar)

    # Criar a área de entrada para exibir o resultado
    self.entrada = tk.Entry(self.janela)

    # Empacotar os widgets
    self.botao_0.grid(row=4, column=1, sticky="nsew")
    self.botao_0.config(font=("Arial"))
    self.botao_1.grid(row=3, column=0, sticky="nsew")
    self.botao_1.config(font=("Arial"))
    self.botao_2.grid(row=3, column=1, sticky="nsew")
    self.botao_2.config(font=("Arial"))
    self.botao_3.grid(row=3, column=2, sticky="nsew")
    self.botao_3.config(font=("Arial"))
    self.botao_4.grid(row=2, column=0, sticky="nsew")
    self.botao_4.config(font=("Arial"))
    self.botao_5.grid(row=2, column=1, sticky="nsew")
    self.botao_5.config(font=("Arial"))
    self.botao_6.grid(row=2, column=2, sticky="nsew")
    self.botao_6.config(font=("Arial"))
    self.botao_7.grid(row=1, column=0, sticky="nsew")
    self.botao_7.config(font=("Arial"))
    self.botao_8.grid(row=1, column=1, sticky="nsew")
    self.botao_8.config(font=("Arial"))
    self.botao_9.grid(row=1, column=2, sticky="nsew")
    self.botao_9.config(font=("Arial"))
    self.botao_ponto.grid(row=4, column=0, sticky="nsew")
    self.botao_ponto.config(font=("Arial"))
    self.botao_soma.grid(row=1, column=3, sticky="nsew")
    self.botao_soma.config(font=("Arial"))
    self.botao_subtracao.grid(row=2, column=3, sticky="nsew")
    self.botao_subtracao.config(font=("Arial"))
    self.botao_multiplicacao.grid(row=3, column=3, sticky="nsew")
    self.botao_multiplicacao.config(font=("Arial"))
    self.botao_divisao.grid(row=4, column=3, sticky="nsew")
    self.botao_divisao.config(font=("Arial"))
    self.botao_igualdade.grid(row=4, column=2, sticky="nsew")
    self.botao_igualdade.config(font=("Arial"))
    self.botao_limpar.grid(row=5, column=0, columnspan=2, sticky="nsew")
    self.botao_limpar.config(font=("Arial"))
    self.entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")
    self.entrada.config(font=("Arial"))
    
    for i in range(4):
     self.janela.columnconfigure(i, weight=1)

    for i in range(6):
      self.janela.rowconfigure(i, weight=1)
      

  # Função para inserir um número
  def inserir_numero(self, numero):
    self.entrada.insert(tk.END, numero)
    
  def inserir_operador(self, operador):
    self.entrada.insert(tk.END, operador)

  # Função para limpar a entrada
  def limpar(self):
    self.entrada.delete(0, "end")

  # Função para calcular o resultado
  def calcular(self):
    # Obter a expressão da entrada
    expressao = self.entrada.get()

    # Tentar calcular o resultado e tratar exceções
    try:
      resultado = eval(expressao)
      self.entrada.delete(0, "end")
      self.entrada.insert("end", resultado)
    except ZeroDivisionError:
      self.entrada.delete(0, "end")
      self.entrada.insert("end", "Erro de divisão por zero")
    except SyntaxError:
      self.entrada.delete(0, "end")
      self.entrada.insert("end", "Erro de sintaxe")
      calculadora.janela.mainloop()

# Crie uma instância da classe Calculadora
calculadora = Calculadora()
calculadora.janela.mainloop()
