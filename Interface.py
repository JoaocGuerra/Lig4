from tkinter import *
from tkinter import font

class LIG4:
    def __init__(self,Janela):
        self.voltar = 0
        self.vez = 0
        self.linha_posicao = 0
        self.fontes = [font.Font(family="Super Mario 256", size="40"), font.Font(family="Super Mario 256", size="15"),font.Font(family="Super Mario 256", size="10")]
        self.azul_bebe = "#00BFFF"
        self.txt_lig4 = Label(Janela,bg=fundo,font=self.fontes[0], text="LIG4", fg=self.azul_bebe)
        self.txt_lig4.place(x=80, y=20)
        self.bt_jogar = Button(Janela,bg=fundo,font=self.fontes[1], text="JOGAR", fg=self.azul_bebe, activeforeground=self.azul_bebe,command=self.jan_info_colunas, relief=FLAT,state=NORMAL)
        self.bt_jogar.place(x=100, y=180)
        self.bt_sair = Button(Janela,bg=fundo,font=self.fontes[1], text="SAIR", fg=self.azul_bebe,activeforeground=self.azul_bebe, command=self.fechar, relief=FLAT,state=NORMAL)
        self.bt_sair.place(x=110, y=230)

    def jan_info_colunas(self):
        self.bt_jogar.place_forget()
        self.bt_sair.place_forget()
        if self.voltar>=1:
            self.bt_voltar.place_forget()

        self.bt_como_jogar = Button(Janela, bg=fundo, font=self.fontes[1], text="COMO JOGAR", fg=self.azul_bebe,activeforeground=self.azul_bebe, command=self.jan_como_jogar, relief=FLAT,state=NORMAL)
        self.bt_como_jogar.place(x=60, y=90)
        self.txt_escolha_tamanho=Label(Janela,bg=fundo,font=self.fontes[2], text="ESCOLHA O TAMANHO DO TABULEIRO:", fg=self.azul_bebe)
        self.txt_escolha_tamanho.place(x=10,y=150)
        self.scale_box=Scale(Janela,bg=fundo,from_=4, to=12,width=10,relief=FLAT)
        self.scale_box.place(x=10,y=180)
        self.bt_ok_scale=Button(Janela,bg=fundo,font=self.fontes[2], text="OK", fg=self.azul_bebe, activeforeground=self.azul_bebe,command=self.jan_jogo, relief=FLAT)
        self.bt_ok_scale.place(x=50,y=180)


    def jan_como_jogar(self):
        self.bt_como_jogar.place_forget()
        self.txt_escolha_tamanho.place_forget()
        self.scale_box.place_forget()
        self.bt_ok_scale.place_forget()

        self.bt_voltar=Button(Janela,bg=fundo,font=self.fontes[2], text="VOLTAR", fg=self.azul_bebe, activeforeground=self.azul_bebe,command=self.jan_info_colunas, relief=FLAT)
        self.bt_voltar.place(x=0,y=270)
        self.voltar+=1

    def criar_bt(self, i, j, posi_x, posi_y):
        # Criando botões "x"
        self.bt[i][j] = Button(Janela, bg="#A9A9A9", width=4, height=2, bd=2,state=DISABLED, relief=GROOVE)
        self.bt[i][j].place(x=posi_x, y=posi_y)

    def criar_bt_clicavel(self, i,posi_x_bt_clicavel, posi_y_bt_clicavel):

        def bt_clicado():
            if self.linha_posicao*-1==self.numero:
                self.linha_posicao=0
            self.linha_posicao-=1
            if self.vez%2==0:
                self.tabuleiro[self.linha_posicao][i]="X"
                self.bt[self.linha_posicao][i]["bg"]="red"
            if self.vez%2==1:
                self.tabuleiro[self.linha_posicao][i] = "O"
                self.bt[self.linha_posicao][i]["bg"] = "blue"

            for x in range(self.numero):  # Para imprimir o tabuleiro sem peças.
                for j in range(self.numero):
                    print(self.tabuleiro[x][j], end=' ')
                print()

            self.vez += 1
            print(self.vez)
            print(i)
        # Criando botões "x"
        self.bt_clicavel[i] = Button(Janela, bg="#A9A9A9",command=bt_clicado, width=4, height=2, bd=2, relief=GROOVE)
        self.bt_clicavel[i].place(x=posi_x_bt_clicavel, y=posi_y_bt_clicavel)

    def jan_jogo(self):
        self.numero = self.scale_box.get()
        self.scale_box.place_forget()
        self.bt_como_jogar.place_forget()
        self.txt_escolha_tamanho.place_forget()
        self.txt_lig4.place_forget()
        self.bt_ok_scale.place_forget()
        def Matriz(tamanho, vazio):  # Construção do Tabuleiro segundo o valor informado pelos os jogadores.
            matriz = []
            colunas = []
            lista = []

            for i in range(tamanho):
                matriz.append([])
                colunas.append(i)

            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    matriz[i].append(vazio)
            lista.append(matriz)
            lista.append(colunas)
            return lista
        tamanho_do_jogo = int(self.numero)
        coluna = self.numero

        coluna = int(coluna)
        vazio = '-'
        self.tabuleiro = Matriz(tamanho_do_jogo, vazio)[0]
        for i in range(tamanho_do_jogo):  # Para imprimir o tabuleiro sem peças.
            for j in range(tamanho_do_jogo):
                print(self.tabuleiro[i][j], end=' ')
            print()

        self.bt=[]
        self.bt_clicavel=[]
        for i in range(len(self.tabuleiro)):
            self.bt_clicavel.append("x")
            self.bt.append([])
            for j in range(len(self.tabuleiro)):
                self.bt[i].append("x")

        posi_x_bt_clicavel = 0
        posi_y_bt_clicavel = 39
        for i in range(len(self.bt_clicavel)):
            posi_x_bt_clicavel+=36
            self.criar_bt_clicavel(i,posi_x_bt_clicavel,posi_y_bt_clicavel)
        posi_x=0
        posi_y = 100
        # Criando os botões
        for i in range(len(self.tabuleiro)):
            if i >= 1:
                posi_y += 39
            for j in range(len(self.tabuleiro)):
                posi_x += 36
                if self.tabuleiro[i][j] == "-":
                    self.criar_bt(i, j, posi_x, posi_y)
            posi_x = 0

    def fechar(self):
        Janela.destroy()


Janela=Tk()
fundo="white"
Janela.config(bg=fundo)
LIG4(Janela)
Janela.title("Lig4")
Janela.geometry('300x300+350+150')
Janela.mainloop()
