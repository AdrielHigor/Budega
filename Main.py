import tkinter
from tkinter import ttk
from tkinter import*
import sqlite3

class Application(Frame):
    def __init__(self, master=None):
        Frame. __init__(self,master)
        self.sc1 = Login()
        self.sc1.inicio()
        self.bd = BancoDados()

class Login():
    def inicio(self):    
        self.msg = Label(text="Sistema De Login", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=300, y=100)

        self.Quit = Button(text="Sair")
        self.Quit.place(bordermode=OUTSIDE, height=30, width=100, x=440, y=210)

        self.cadastrar = Button(text="cadastrar", command= self.registrando)
        self.cadastrar.place(bordermode=OUTSIDE, height=30, width=100, x=340, y=210)

        self.logar = Button(text="Entrar", command=self.Logar)
        self.logar.place(bordermode=OUTSIDE, height=30, width=100, x=240, y=210)

        self.login = Entry()
        self.login.place(bordermode=OUTSIDE, height=25, width=200, x=300, y=150)

        self.loginLabel = Label(text="Login")
        self.loginLabel.place(bordermode=OUTSIDE, height=20, width=50, x=240, y=150)

        self.senhaLabel = Label(text="Senha")
        self.senhaLabel.place(bordermode=OUTSIDE, height=20, width=50, x=240, y=180)

        self.senha = Entry()
        self.senha["show"] = "*"
        self.senha.place(bordermode=OUTSIDE, height=25, width=200, x=300, y=180)

        self.msg2 = Message(text="", font="Arial, 12")
        self.msg2.place(bordermode=OUTSIDE, height=None, width=199, x=300, y=250)

        self.msg3 = Label(text="All copyright to Adriel, the god of programmation")
        self.msg3.place(bordermode=OUTSIDE, height=None, width=None, x=420, y=380)

    def Logar(self):
        login = self.login.get()
        senha = self.senha.get()

        self.connection = sqlite3.connect('Loja.db')
        self.c = self.connection.cursor()
        self.c.execute('SELECT * FROM Caixa WHERE Email = ? AND Senha = ?', (login,senha))
        test = self.c.fetchall()

        for x in test:
            if senha and login in x:
                self.logado()
            else:
                self.msg2["text"] = "Error"

    def logado(self):
        self.msg.place_forget()
        self.Quit.place_forget()
        self.cadastrar.place_forget()
        self.logar.place_forget()
        self.login.place_forget()
        self.loginLabel.place_forget()
        self.senhaLabel.place_forget()
        self.senha.place_forget()
        self.msg2.place_forget()

        self.sc2 = Loja()
        self.sc2.lojaInicio()

    def registrando(self):
        self.msg.place_forget()
        self.Quit.place_forget()
        self.cadastrar.place_forget()
        self.logar.place_forget()
        self.login.place_forget()
        self.loginLabel.place_forget()
        self.senhaLabel.place_forget()
        self.senha.place_forget()
        self.msg2.place_forget()
        
        self.sc3 = Registrar()
        self.sc3.regisInicio()

class Registrar():
    def __init__(self):
        self.sc1 = Login()
        self.bd = BancoDados()

    def regisInicio(self):
        self.msg = Label(text="Registrar-se", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=300, y=100)

        self.voltar = Button(text="Cancelar", command=self.voltar)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=400, y=240)

        self.registrar = Button(text="Registrar", command=self.registro)
        self.registrar.place(bordermode=OUTSIDE, height=30, width=100, x=300, y=240)

        self.mostrar = Button(text="Mostrar", command=self.Mostrar)
        self.mostrar.place(bordermode=OUTSIDE, height=30, width=100, x=500, y=208)

        self.nome = Entry()
        self.nome.place(bordermode=OUTSIDE, height=25, width=200, x=300, y=150)

        self.nomeLabel = Label(text="Nome:")
        self.nomeLabel.place(bordermode=OUTSIDE, height=20, width=50, x=240, y=150)

        self.emailLabel = Label(text="Email:")
        self.emailLabel.place(bordermode=OUTSIDE, height=20, width=50, x=240, y=180)

        self.senhaLabel = Label(text="Senha:")
        self.senhaLabel.place(bordermode=OUTSIDE, height=20, width=50, x=240, y=210)

        self.email = Entry()
        self.email.place(bordermode=OUTSIDE, height=25, width=200, x=300, y=180)

        self.senha = Entry()
        self.senha["show"] = "*"
        self.senha.place(bordermode=OUTSIDE, height=25, width=200, x=300, y=210)

        self.msg2 = Label(text="", font="Arial, 12")
        self.msg2.place(bordermode=OUTSIDE, height=None, width=200, x=300, y=275) 


    def voltar(self):
        self.msg.place_forget()
        self.voltar.place_forget()
        self.registrar.place_forget()
        self.mostrar.place_forget()
        self.nome.place_forget()
        self.nomeLabel.place_forget()
        self.emailLabel.place_forget()
        self.senhaLabel.place_forget()
        self.email.place_forget()
        self.senha.place_forget()
        self.msg2.place_forget()
        self.sc1.inicio()

    def registro(self):
        nome = self.nome.get()
        email = self.email.get()
        senha = self.senha.get()

        if nome == "":
            self.msg2["text"] = "Nome Inválido"
        elif email == "":
            self.msg2["text"] = "Email Inválido"
        elif senha == "":
            self.msg2["text"] = "Senha Inválido"
        else:
            try:
                self.bd.cadastrarCaixa(nome, email, senha)
                self.msg2["text"] = "Registrado"
            except sqlite3.IntegrityError:
                self.msg2["text"] = "Usuário ja registrado"


    def Mostrar(self):
        if self.senha["show"] == "*":
            self.senha["show"] = ""
            self.mostrar["text"] = "Ocultar"
        else:
            self.senha["show"] = "*"
            self.mostrar["text"] = "Mostrar"

class Loja():
    def __init__(self):
        self.sc1 = Login()
        self.sc2 = Vendas()
        self.sc3 = CadastrarProd()
        self.sc4 = Estoque()
        self.sc5 = Cliente()

    def lojaInicio(self):
        self.cadastrar = Button(text="Cadastrar Produto", command=self.cadastrar)
        self.cadastrar.place(bordermode=OUTSIDE, height=40, width=152, x= 152, y=0)

        self.estoque = Button(text="Estoque", command=self.estoque)
        self.estoque.place(bordermode=OUTSIDE, height=40, width=152, x=304, y=0)

        self.vender = Button(text="Vender", command=self.venda)
        self.vender.place(bordermode=OUTSIDE, height=40, width=152, x=0, y=0)

        self.cliente = Button(text='Cliente', command=self.clientes)
        self.cliente.place(bordermode=OUTSIDE, height=40, width=152, x=456, y=0)

        self.sair = Button(text="Sair", command=self.logOut)
        self.sair.place(bordermode=OUTSIDE, height=40, width=152, x=608, y=0)

    def esquecer(self):
        self.cadastrar.place_forget()
        self.estoque.place_forget()
        self.vender.place_forget()
        self.cliente.place_forget()
        self.sair.place_forget()

    def venda(self):
        self.esquecer()
        self.sc2.vendaInicio()

    def logOut(self):
        self.esquecer()
        self.sc1.inicio()

    def cadastrar(self):
        self.esquecer()
        self.sc3.cadastro()

    def estoque(self):
        self.esquecer()
        self.sc4.estoqueInicio()

    def clientes(self):
        self.esquecer()
        self.sc5.clienteInicio()

class Vendas():
    def __init__(self):
        pass

    def vendaInicio(self):
        self.msg = Label(text="Vender Produto", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=10, y=10)

        self.separador = ttk.Separator(orient=HORIZONTAL)
        self.separador.place(bordermode=OUTSIDE, height=None, width=10000, x=0, y=50)

        self.voltar = Button(text="Voltar", command=self.volta)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=115, y=280)

        self.vender = Button(text="Vender", command=self.venda)
        self.vender.place(bordermode=OUTSIDE, height=30, width=100, x=15, y=280)

        self.nome = Entry()
        self.nome.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=90)

        self.nomeLabel = Label(text="Nome do produto:")
        self.nomeLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=70)

        self.descontoLabel = Label(text="Desconto:")
        self.descontoLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=170)

        self.quantLabel = Label(text="Quantidade:")
        self.quantLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=120)

        self.pagoLabel = Label(text="Valor pago:")
        self.pagoLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=220)

        self.pago = Entry()
        self.pago.place(bordermode=OUTSIDE, height=25, width=50, x=20, y=240)

        self.desconto = Entry()
        self.desconto.place(bordermode=OUTSIDE, height=25, width=50, x=20, y=190)

        self.quant = Entry()
        self.quant.place(bordermode=OUTSIDE, height=25, width=50, x=20, y=140)

        self.msg2 = Label(text="", font="Arial, 12")
        self.msg2.place(bordermode=OUTSIDE, height=None, width=200, x=30, y=320)

    def volta(self):
        self.msg.place_forget()
        self.separador.place_forget()
        self.voltar.place_forget()
        self.vender.place_forget()
        self.nome.place_forget()
        self.nomeLabel.place_forget()
        self.descontoLabel.place_forget()
        self.quantLabel.place_forget()
        self.pagoLabel.place_forget()
        self.pago.place_forget()
        self.desconto.place_forget()
        self.quant.place_forget()
        self.msg2.place_forget()

        self.sc1 = Loja()
        self.sc1.lojaInicio()

    def venda(self):
        produto = self.nome.get()
        pago = self.pago.get()
        desconto = self.desconto.get()
        quant = self.quant.get()

        if produto == "":
            self.msg2["text"] = "Produto Inválido"
        elif pago == "":
            self.msg2["text"] = "Pagamento Inválido"
        elif quant == "":
            self.msg2["text"] = "Quantidade Inválida"
        else:
            self.connection = sqlite3.connect('Loja.db')
            self.c = self.connection.cursor()
            self.c.execute('SELECT * FROM produtos')
            self.test = self.c.fetchall() 

            for dados in self.test:
                if dados[2] == produto:
                    if dados[1] < (int(quant)):
                        self.msg2["text"] = "Estoque Insuficiente"
                    else:
                        aux = dados[1] - (int(pago))
                        aux = (str(aux))
                        self.c.execute('UPDATE produtos SET Quantidade = ?', [aux])
                        print("sucesso")
                        self.listas = self.c.fetchall()

                        for x in self.listas:
                            self.tabela.insert("", tkinter.END, values=x)

             #   self.bd.inserirproduto(codigo, quantidade, nome, preco)
              #  self.msg2["text"] = "Produto cadastrado"
            #except sqlite3.IntegrityError:
                #self.msg2["text"] = "Produto já cadastrado"



class CadastrarProd():
    def __init__(self):
        self.bd = BancoDados()

    def cadastro(self):

        self.msg = Label(text="Cadastrar Produto", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=10, y=10)

        self.separador = ttk.Separator(orient=HORIZONTAL)
        self.separador.place(bordermode=OUTSIDE,height=None,width=10000 , x=0, y=50)

        self.voltar = Button(text="Voltar", command=self.volta)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=115, y=280)

        self.cadastrar = Button(text="Cadastrar", command=self.cadastrado)
        self.cadastrar.place(bordermode=OUTSIDE, height=30, width=100, x=15, y=280)

        self.cod = Entry()
        self.cod.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=90)

        self.codLabel = Label(text="Código do produto:")
        self.codLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=70)

        self.produtoLabel = Label(text="Nome do produto:")
        self.produtoLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=170)

        self.quantLabel = Label(text="Quantidade:")
        self.quantLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=120)

        self.precoLabel = Label(text="Preço de venda:")
        self.precoLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=220)

        self.preco = Entry()
        self.preco.place(bordermode=OUTSIDE, height=25, width=50, x=20, y=240)

        self.produto = Entry()
        self.produto.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=190)

        self.quant = Entry()
        self.quant.place(bordermode=OUTSIDE, height=25, width=50, x=20, y=140)

        self.msg2 = Label(text="", font="Arial, 12")
        self.msg2.place(bordermode=OUTSIDE, height=None, width=200, x=30, y=320)

    def cadastrado(self):
        codigo = self.cod.get()
        quantidade = self.quant.get()
        nome = self.produto.get()
        preco = self.preco.get()

        if codigo == "":
            self.msg2["text"] = "Código Inválido"
        elif quantidade == "":
            self.msg2["text"] = "Quantidade Inválida"
        elif nome == "":
            self.msg2["text"] = "Nome Inválido"
        elif preco == "":
            self.msg2["text"] = "Preço Inválido"
        else:
            try:
                self.bd.inserirproduto(codigo, quantidade, nome, preco)
                self.msg2["text"] = "Produto cadastrado"
            except sqlite3.IntegrityError:
                self.msg2["text"] = "Produto já cadastrado"

    def volta(self):
        self.msg.place_forget()
        self.separador.place_forget()
        self.voltar.place_forget()
        self.cadastrar.place_forget()
        self.cod.place_forget()
        self.codLabel.place_forget()
        self.preco.place_forget()
        self.precoLabel.place_forget()
        self.produto.place_forget()
        self.produtoLabel.place_forget()
        self.quant.place_forget()
        self.quantLabel.place_forget()
        self.msg2.place_forget()

        self.sc1 = Loja()
        self.sc1.lojaInicio()

class Estoque():
    def estoqueInicio(self):
        self.voltar = Button(text="Voltar", command=self.volta)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=650, y=10)

        self.msg = Label(text="Estoque de Produtos", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=10, y=10)

        self.separador = ttk.Separator(orient=HORIZONTAL)
        self.separador.place(bordermode=OUTSIDE, height=None, width=500, x=0, y=50)

        self.tabela = ttk.Treeview(height=20,columns=("cod", "quant", "nome", "quant"))
        self.tabela["show"] = 'headings'
        self.tabela.place(bordermode=OUTSIDE, height=350, width=740, x=0, y=50)
        self.tabela.heading("#1", text='Código do Produto', anchor=W)
        self.tabela.heading("#2", text='Quantidade Produto', anchor=W)
        self.tabela.heading("#3", text='Nome Produto', anchor=W)
        self.tabela.heading("#4", text='Preço', anchor=W)

        self.verticalBar = Scrollbar(orient='vertical', command=self.tabela.yview)
        self.verticalBar.place(bordermode=OUTSIDE, height=350, width=20, x=739, y=50)
        self.tabela.configure(yscroll=self.verticalBar.set)

        self.listar()

    def listar(self):
        self.connection = sqlite3.connect('Loja.db')
        self.c = self.connection.cursor()
        self.c.execute('SELECT * FROM Produtos')
        self.listas = self.c.fetchall()

        for x in self.listas:
            self.tabela.insert("", tkinter.END, values=x)

    def volta(self):
        self.voltar.place_forget()
        self.separador.place_forget()
        self.msg.place_forget()
        self.tabela.place_forget()
        self.verticalBar.place_forget()

        self.sc1 = Loja()
        self.sc1.lojaInicio()


class Cliente():
    def clienteInicio(self):
        self.registrar = Button(text="Novo Cliente", command=self.registrar)
        self.registrar.place(bordermode=OUTSIDE, height=30, width=100, x=550, y=10)

        self.voltar = Button(text="Voltar", command=self.volta)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=650, y=10)

        self.msg = Label(text="Clientes", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=10, y=10)

        self.separador = ttk.Separator(orient=HORIZONTAL)
        self.separador.place(bordermode=OUTSIDE, height=None, width=500, x=0, y=50)

        self.tabelaClientes = ttk.Treeview(height=20,columns=("NomeCliente", "CPF", "telefone", "Endereco"))
        self.tabelaClientes["show"] = 'headings'
        self.tabelaClientes.place(bordermode=OUTSIDE, height=350, width=740, x=0, y=50)
        self.tabelaClientes.heading("NomeCliente", text='Nome do cliente', anchor=W)
        self.tabelaClientes.heading("CPF", text='CPF', anchor=W)
        self.tabelaClientes.heading("telefone", text='Telefone', anchor=W)
        self.tabelaClientes.heading("Endereco", text='Endereço', anchor=W)

        self.verticalBar = Scrollbar(orient='vertical', command=self.tabelaClientes.yview)
        self.verticalBar.place(bordermode=OUTSIDE, height=350, width=20, x=739, y=50)
        self.tabelaClientes.configure(yscroll=self.verticalBar.set)

        self.listarClientes()

    def listarClientes(self):
        self.connection = sqlite3.connect('Loja.db')
        self.c = self.connection.cursor()
        self.c.execute('SELECT * FROM Clientes')
        self.listasCliente = self.c.fetchall()

        for x in self.listasCliente:
            self.tabelaClientes.insert("", tkinter.END, values=x)

    def volta(self):
        self.voltar.place_forget()
        self.separador.place_forget()
        self.msg.place_forget()
        self.tabelaClientes.place_forget()
        self.verticalBar.place_forget()
        self.registrar.place_forget()

        self.sc1 = Loja()
        self.sc1.lojaInicio()

    def registrar(self):
        self.voltar.place_forget()
        self.separador.place_forget()
        self.msg.place_forget()
        self.tabelaClientes.place_forget()
        self.verticalBar.place_forget()
        self.registrar.place_forget()

        self.sc2 = ClienteCadastro()
        self.sc2.cadastroInicio()

class ClienteCadastro():
    def __init__(self):
        self.bd = BancoDados()

    def cadastroInicio(self):
        self.msg = Label(text="Cadastrar cliente", font="Arial, 14")
        self.msg.place(bordermode=OUTSIDE, height=None, width=199, x=10, y=10)

        self.separador = ttk.Separator(orient=HORIZONTAL)
        self.separador.place(bordermode=OUTSIDE, height=None, width=10000, x=0, y=50)

        self.voltar = Button(text="Voltar", command=self.volta)
        self.voltar.place(bordermode=OUTSIDE, height=30, width=100, x=115, y=280)

        self.cadastrar = Button(text="Cadastrar", command=self.cadastrado)
        self.cadastrar.place(bordermode=OUTSIDE, height=30, width=100, x=15, y=280)

        self.nome = Entry()
        self.nome.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=90)

        self.nomeLabel = Label(text="Nome do cliente:")
        self.nomeLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=70)

        self.cpfLabel = Label(text="CPF do cliente:")
        self.cpfLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=170)

        self.telefoneLabel = Label(text="Telefone:")
        self.telefoneLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=120)

        self.enderecoLabel = Label(text="Endereço:")
        self.enderecoLabel.place(bordermode=OUTSIDE, height=20, width=None, x=15, y=220)

        self.endereco = Entry()
        self.endereco.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=240)

        self.cpf = Entry()
        self.cpf.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=190)

        self.telefone = Entry()
        self.telefone.place(bordermode=OUTSIDE, height=25, width=200, x=20, y=140)

        self.msg2 = Label(text="", font="Arial, 12")
        self.msg2.place(bordermode=OUTSIDE, height=None, width=200, x=30, y=320)

    def cadastrado(self):
        nome = self.nome.get()
        cpf = self.cpf.get()
        telefone = self.telefone.get()
        endereco = self.endereco.get()

        if nome == "":
            self.msg2["text"] = "Nome Inválido"
        elif cpf == "":
            self.msg2["text"] = "CPF Inválido"
        elif telefone == "":
            self.msg2["text"] = "Telefone Inválido"
        elif endereco == "":
            self.msg2["text"] = "Endereço Inválido"
        else:
            try:
                self.bd.cadastrarCliente(nome, cpf, telefone, endereco)
                self.msg2["text"] = "Cliente cadastrado"
            except sqlite3.IntegrityError:
                self.msg2["text"] = "Cliente já cadastrado"

    def volta(self):
        self.msg.place_forget()
        self.separador.place_forget()
        self.voltar.place_forget()
        self.cadastrar.place_forget()
        self.enderecoLabel.place_forget()
        self.endereco.place_forget()
        self.cpfLabel.place_forget()
        self.cpf.place_forget()
        self.telefoneLabel.place_forget()
        self.telefone.place_forget()
        self.nome.place_forget()
        self.nomeLabel.place_forget()
        self.msg2.place_forget()

        self.sc1 = Cliente()
        self.sc1.clienteInicio()

class BancoDados():
    def __init__(self):
        self.connection = sqlite3.connect('Loja.db')
        self.c = self.connection.cursor()
        try:
            self.c.execute('CREATE TABLE Produtos (CodigoProd VARCHAR NOT NULL, Quantidade INT NOT NULL, NomeProd VARCHAR NOT NULL, Preço FLOAT NOT NULL, PRIMARY KEY(NomeProd, CodigoProd))')
            self.c.execute('CREATE TABLE Clientes (NomeCliente VARCHAR NOT NULL, CPF VARCHAR NOT NULL, telefone VARCHAR ,Endereco VARCHAR NOT NULL, PRIMARY KEY(NomeCliente, CPF))')
            self.c.execute('CREATE TABLE Caixa (Nome VARCHAR NOT NULL, Email VARCHAR NOT NULL,Senha VARCHAR NOT NULL, PRIMARY KEY(Email))')
        except sqlite3.OperationalError:
            pass

    def inserirproduto(self, nomeProd, codProd, preco, quantidade):
        self.c.execute('INSERT INTO Produtos VALUES(?, ?, ?, ?)', (nomeProd, codProd, preco, quantidade))
        self.connection.commit()

    def cadastrarCliente(self, nome, cpf, telefone, endereco):
        self.c.execute('INSERT INTO Clientes VALUES(?, ?, ?, ?)', (nome, cpf, telefone, endereco))
        self.connection.commit()

    def mostrarClientes(self):
        self.c.execute('SELECT * FROM Clientes')
        for x in self.c.fetchall():
            print(x)

    def cadastrarCaixa(self, nome, email, senha):
        self.c.execute('INSERT INTO Caixa VALUES (?, ?, ?)', (nome, email, senha))
        self.connection.commit()






root = Tk()
app = Application(master=root)
app.master.title("Budega 2.0")
app.master.minsize(760, 400)
app.mainloop()
root.destroy()

