import tkinter as tk
from tkinter import ttk
from logica import Logica
from tkinter import Scrollbar, Label, Frame, Button, Tk, LEFT, RIGHT, BOTTOM, VERTICAL, HORIZONTAL, X, Y

class Interface:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Arial", "10")
        self.logica = Logica()  # Instância da classe de lógica de dados
        
        # Criação dos Frames
        self.create_frames()

        # Criação dos campos
        self.create_widgets()

    def create_frames(self):
        self.campo1 = Frame(self.master, pady=10)
        self.campo1.pack()
        self.campo2 = Frame(self.master, pady=5)
        self.campo2.pack()
        # Adicione os outros campos aqui (campo3, campo4, ...)

    def create_widgets(self):
        # Campos para input
        self.lblidgastos = tk.Label(self.campo2, text="idusuário:", width="25", font=self.fonte)
        self.lblidgastos.pack(side=LEFT)

        self.idgastos = tk.Entry(self.campo2, width=30, font=self.fonte)
        self.idgastos.pack(side=LEFT)
        # Adicionar outros campos como nome, tipo_pgto, etc.

        # Botões de ação
        self.botaocadastrar = Button(self.campo9, text="Cadastrar", font=self.fonte, width=12, command=self.logica.inserircliente)
        self.botaocadastrar.pack(side=LEFT)

        self.botaopesquisar = Button(self.campo9, text="Pesquisar", font=self.fonte, width=12, command=self.logica.consultarcliente)
        self.botaopesquisar.pack(side=LEFT)
        # Adicione os outros botões aqui
        
    def atualizar_mensagem(self, mensagem):
        self.mensagem["text"] = mensagem
