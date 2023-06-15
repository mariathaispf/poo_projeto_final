from tkinter import *
from tkinter import messagebox

from bd import *


################# definindo algumas cores ##############

co0 = "#000000"  # preta
co1 = "#59656F"
co2 = "#feffff"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cizenta

################# Criando Janela principal ##############

janela = Tk()
# to prevent the window size from being changed
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('500x225')
janela.title('To-do App')
janela.configure(background=co1)


### dividindo a janela em 2 frames, esquerdo e direito ########
frame_esquerda = Frame(janela, width=300, height=200, bg=co2, relief="flat",)
frame_esquerda.grid(row=0, column=0, sticky=NSEW)
frame_direita = Frame(janela, width=200, height=250, bg=co2,  relief="flat",)
frame_direita.grid(row=0, column=1, sticky=NSEW)

##### dividindo o frame esquerdo em duas partes,cima e baixo ######
frame_e_cima = Frame(frame_esquerda, width=300,
                     height=50, bg=co2, relief="flat",)
frame_e_cima.grid(row=0, column=0, sticky=NSEW)
frame_e_baixo = Frame(frame_esquerda, width=300,
                      height=150, bg=co2, relief="flat",)
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

#### função main #####
def main(a):
    ############## novo #############
    if a == 'novo':
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        #### função adicionar ###
        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()
        lb = Label(frame_e_baixo, text="Insira uma nova tarefa", width=42, height=5, pady=15)
        lb.grid(row=0, column=0, sticky=NSEW)

        entry = Entry(frame_e_baixo, width=15,)
        entry.grid(row=1, column=0, sticky=NSEW)
        b_adicionar = Button(frame_e_baixo, text="Adicionar", width=9, height=1, bg=co6,pady=10, fg=co0, font="8", relief=RAISED, overrelief=RIDGE, command=adicionar)
        b_adicionar.grid(row=2, column=0, sticky=NSEW, pady=15)


    ############## Atualizar ########
    if a == 'atualizar':
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def on():
            lb = Label(frame_e_baixo, text="Atualize a tarefa", width=42, height=5, pady=15)
            lb.grid(row=0, column=0, sticky=NSEW)
            entry = Entry(frame_e_baixo, width=15,)
            entry.grid(row=1, column=0, sticky=NSEW)

            #tarefas = selecionar()
            #cs = listbox.curselection()[0]
            #s_palavra = listbox.get(cs)
            #entry.insert(0, s_palavra)
        def mostrar():
            listbox.delete(0, END)
            tarefas = selecionar()
            for item in tarefas:
                listbox.insert(END, item[1])
        mostrar()
            ### função atualizar ####
        def alterar():
                for item in tarefas:
                    if s_palavra == item[1]:
                        nova = [entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)

                mostrar()

        b_atualizar = Button(frame_e_baixo, text="Atualizar", width=9, height=1, bg=co6, pady=10,
                                 fg=co0, font="8", relief=RAISED, overrelief=RIDGE, command=alterar)
        b_atualizar.grid(row=2, column=0, sticky=NSEW, pady=15)


        on()


############## Remove #############
def remover():
    cs = listbox.curselection()[0]
    s_palavra = listbox.get(cs)
    tarefas = selecionar()
    for item in tarefas:
        if s_palavra == item[1]:
            deletar([item[0]])

    mostrar()



##### criando botões no frame frame_e_cima  ########
b_novo = Button(frame_e_cima, text="+ Novo", width=10, height=1, bg=co3, fg="white",
                font="5", anchor="center", relief=RAISED, command=lambda: main('novo'))
b_novo.grid(row=0, column=0,  sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="Remover", width=10, height=1, bg=co4,
                   fg="white", font="5", anchor="center", relief=RAISED,command=remover)
b_remover.grid(row=0, column=1,  sticky=NSEW, pady=1)

b_atualizar = Button(frame_e_cima, text="Atualizar", width=10, height=1, bg=co5, fg="white",
                     font="5", anchor="center", relief=RAISED, command=lambda: main('atualizar'))
b_atualizar.grid(row=0, column=2,  sticky=NSEW, pady=1)

######### Adicionando Label e Listbox no frame a direita ########
label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7,
    padx=10, relief="flat", anchor=W, font=('Courier  20 bold'), bg=co2, fg=co0)
label.grid(row=0, column=0,  sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=('Arial  9 bold'), width=1)
listbox.grid(row=1, column=0, columnspan=2,  sticky=NSEW, pady=5)




############## Mostrar tarefas na Listbox #############
def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])
mostrar()


janela.mainloop()