from tkinter import*
import tkinter as tk
import tkinter.ttk as ttk
from heranca import heranca
from Banco import Banco


###################################### Criação da interface ######################################
#criação da classe - simples
class principal: 
    def __init__(self, master=None): 
        self.idgastos = 0

        #### Cabeçalho ####
        self.fonte = ("Arial", "10") # Cariável fonte
        self.Cabeçalho = Frame(master) # Tela principal
        self.Cabeçalho["pady"] = 10 # Posicionamento do Cabeçalho        
        self.Cabeçalho.pack() 

        #### Distância campos de insert ####
        self.id = Frame(master) 
        self.id["pady"] = 5
        self.id.pack() 

        self.tipo = Frame(master) 
        self.tipo["pady"] = 5 
        self.tipo.pack() 

        self.tipo_pgto = Frame(master) 
        self.tipo_pgto["pady"] = 5 
        self.tipo_pgto.pack() 

        self.valor = Frame(master) 
        self.valor["pady"] = 5 
        self.valor.pack() 

        self.descricao = Frame(master) 
        self.descricao["pady"] = 5
        self.descricao.pack() 

        # Botões
        self.botoes = Frame(master) 
        self.botoes["pady"] = 5
        self.botoes.pack() 

        self.campoDez = Frame(master) 
        self.campoDez["pady"] = 5
        self.campoDez.pack() 

        self.campoOnze = Frame(master) 
        self.campoOnze["pady"] = 5
        self.campoOnze.pack() 

        ###################################### INICIO - Label - criação de título ou nome de campo ######################################

        self.cabecalho = tk.Label(self.Cabeçalho, text="Cadastro") 
        self.cabecalho["font"] = ("Arial","10","bold")
        self.cabecalho.pack(side=LEFT)

        ##### ID #####
        self.lblidgastos = tk.Label(self.id, text="ID:", width="25", font=self.fonte)
        self.lblidgastos.pack(side=LEFT) # side especifica a inclusão da escrita e LEFT a esquerda

        self.idgastos = tk.Entry(self.id) 
        self.idgastos["width"] = 30
        self.idgastos["font"] = self.fonte
        self.idgastos.pack(side=LEFT)

        ##### TIPO #####
        self.lblnome = tk.Label(self.tipo, text="Tipo:", width="25", font=self.fonte)
        self.lblnome.pack(side=LEFT) # side especifica a inclusão da escrita e LEFT a esquerda

        self.tipo = tk.Entry(self.tipo) 
        self.tipo["width"] = 30
        self.tipo["font"] = self.fonte
        self.tipo.pack(side=LEFT)

        ##### TIPO_PGTO #####
        self.lbltipo_pgto = tk.Label(self.tipo_pgto, text="Tipo de Pagamento:", width="25", font=self.fonte)
        self.lbltipo_pgto.pack(side=LEFT) # side especifica a inclusão da escrita e LEFT a esquerda

        self.tipo_pgto = tk.Entry(self.tipo_pgto) 
        self.tipo_pgto["width"] = 30
        self.tipo_pgto["font"] = self.fonte
        self.tipo_pgto.pack(side=LEFT)

        ##### Valor #####
        self.lblvalor = tk.Label(self.valor, text="Valor:", width="25", font=self.fonte)
        self.lblvalor.pack(side=LEFT) # side especifica a inclusão da escrita e LEFT a esquerda

        self.valor = tk.Entry(self.valor) 
        self.valor["width"] = 30
        self.valor["font"] = self.fonte
        self.valor.pack(side=LEFT)

        ##### Descrição #####
        self.lbldescricao = tk.Label(self.descricao, text="Descrição:", width="25", font=self.fonte)
        self.lbldescricao.pack(side=LEFT) # side especifica a inclusão da escrita e LEFT a esquerda

        self.descrição = tk.Entry(self.descricao) 
        self.descrição["width"] = 30
        self.descrição["font"] = self.fonte
        self.descrição.pack(side=LEFT)
        
        ###################################### FIM - Label - criação de título ou nome de campo ######################################

        ################## INICIO - Botões ##################
        
        self.botaocadastrar = tk.Button(self.botoes)
        self.botaocadastrar["text"] = "Cadastrar"
        self.botaocadastrar["font"] = self.fonte
        self.botaocadastrar["width"] = 12
        self.botaocadastrar["command"] = self.inserircliente
        self.botaocadastrar.pack(side=LEFT)

        self.botaopesquisar = tk.Button(self.botoes)
        self.botaopesquisar["text"] = "Pesquisar"
        self.botaopesquisar["font"] = self.fonte
        self.botaopesquisar["width"] = 12
        self.botaopesquisar["command"] = self.consultarcliente
        self.botaopesquisar["command"] = self.mostratela
        self.botaopesquisar.pack(side=LEFT)

        self.botaoatualizar = tk.Button(self.botoes)
        self.botaoatualizar["text"] = "Atualizar"
        self.botaoatualizar["font"] = self.fonte
        self.botaoatualizar["width"] = 12
        self.botaoatualizar["command"] = self.atualizarusuario
        self.botaoatualizar.pack(side=LEFT)

        self.botaodeletar = tk.Button(self.botoes)
        self.botaodeletar["text"] = "Deletar"
        self.botaodeletar["font"] = self.fonte
        self.botaodeletar["width"] = 12
        self.botaodeletar["command"] = self.excluirusuario
        self.botaodeletar.pack(side=LEFT)

        self.botaosair = tk.Button(self.botoes)
        self.botaosair["text"] = "Sair"
        self.botaosair["font"] = self.fonte
        self.botaosair["width"] = 12
        self.botaosair["command"] = quit
        self.botaosair.pack(side=LEFT)

        ################## FIM - Botões ##################

        self.mensagem = Label(self.campoDez, text="")
        self.mensagem["font"] = ("Tahoma", "9", "italic")
        self.mensagem.pack(side=LEFT)
    
        self.scrollbary = Scrollbar(self.campoOnze, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.campoOnze, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.campoOnze, columns=("idgastos", "tipo", "tipo_pgto", "valor", "descrição"), selectmode="extended", height=20, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('idgastos', text="idgastos", anchor=W)
        self.tree.heading('tipo', text="tipo", anchor=W)
        self.tree.heading('tipo_pgto', text="tipo_pgto", anchor=W)
        self.tree.heading('valor', text="Endereço", anchor=W)
        self.tree.heading('descrição', text="descrição", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=30)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=200)
        self.tree.column('#5', stretch=NO, minwidth=0, width=80)
        self.tree.pack(side=LEFT)

    def inserircliente(self):
        usu = heranca()

        usu.tipo = self.tipo.get()
        usu.tipo_pgto = self.tipo_pgto.get()
        usu.valor = self.valor.get()
        usu.descrição = self.descrição.get()

        self.mensagem["text"] = usu.inserecliente()

        self.idgastos.delete(0, END)
        self.tipo.delete(0, END)
        self.tipo_pgto.delete(0, END)
        self.valor.delete(0, END)
        self.descrição.delete(0, END)

    def atualizarusuario(self):
        usu = heranca()

        usu.idgastos = self.idgastos.get()
        usu.tipo = self.tipo.get()
        usu.tipo_pgto = self.tipo_pgto.get()
        usu.valor = self.valor.get()
        usu.descrição = self.descrição.get()

        self.mensagem["text"] = usu.alteracliente()

        self.idgastos.delete(0, END)
        self.tipo.delete(0, END)
        self.tipo_pgto.delete(0, END)
        self.valor.delete(0, END)
        self.descrição.delete(0, END)

    def excluirusuario(self):
        usu = heranca()

        usu.idgastos = self.idgastos.get()

        self.mensagem["text"] = usu.deletacliente()

        self.idgastos.delete(0, END)
        self.tipo.delete(0, END)
        self.tipo_pgto.delete(0, END)
        self.valor.delete(0, END)
        self.descrição.delete(0, END)


    def consultarcliente(self):
        usu = heranca()

        idgastos = self.idgastos.get()

        self.mensagem["text"] = usu.consultacliente(idgastos)

        self.idgastos.delete(0, END)
        self.idgastos.insert(INSERT, usu.idgastos)

        self.tipo.delete(0, END)
        self.tipo.insert(INSERT, usu.tipo)

        self.tipo_pgto.delete(0, END)
        self.tipo_pgto.insert(INSERT,usu.tipo_pgto)

        self.valor.delete(0, END)
        self.valor.insert(INSERT, usu.valor)

        self.descrição.delete(0, END)
        self.descrição.insert(INSERT, usu.descrição)
    
    def mostratela(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            self.tree.delete(*self.tree.get_children())
           #c.Database()
            c.execute("SELECT * FROM usuarios")
            fetch = c.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            c.close()
            return "Consulta realizada com suecesso!"
        except:
            return "Erro de consulta!"

    def inserirmensagem(self): # Próxima Aula mudar MessageBox
        usuario = self.tipo.get()
        if usuario == "enio":
            self.mensagem["text"] = "Cadastrado!"
        else:
            self.mensagem["text"] = "Erro de Cadastro!"

tela = Tk() # Função tkinter para abertura da tela
tela.geometry("960x600")
tela.title('Cadastro de Pessoas') # título principal da barra
principal(tela) # termo utilizado para orientar ao objeto
tela.mainloop() # excecução do programa
