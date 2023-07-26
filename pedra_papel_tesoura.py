# instalação de bibliotecas
from tkinter import *
import random

# Inicializar Janela
raiz = Tk()
raiz.geometry("400x400")
raiz.resizable(0,0)
raiz.title("Jogo - Pedra, Papel, Tesoura")
raiz.config(bg='#3ea4c4')

# Cabeçalho
Label(raiz, text="Pedra / Papel / Tesoura", font="arial 20 bold", bg="seashell2").pack()

# Escolha do Usuário
palpite_usuário = StringVar()
Label(raiz, text='Escolha uma opção: pedra, papel ,tesoura', font='arial 13 bold', bg='seashell2').place(x=20, y=70)
Entry(raiz, font='arial 15', textvariable=palpite_usuário, bg='antiquewhite2').place(x=90, y=130)

# Escolha do computador
palpite_comp = random.randint(1, 3)
if palpite_comp == 1:
    palpite_comp = "pedra"
elif palpite_comp == 2:
    palpite_comp = "papel"
else:
    palpite_comp = "tesoura"

# Lógica de funcionamento
Result = StringVar()


def play():
    escolha_usuario = palpite_usuário.get()
    if escolha_usuario == palpite_comp:
        Result.set("Empate, os 2 escolheram o mesmo")
    elif escolha_usuario == "pedra" and palpite_comp == "papel":
        Result.set(f"Escolha do computador: {palpite_comp} \nComputador Ganhou!")
    elif escolha_usuario == "papel" and palpite_comp == "pedra":
        Result.set(f"Escolha do computador: {palpite_comp} \nVocê Ganhou!")
    elif escolha_usuario == "tesoura" and palpite_comp == "papel":
        Result.set(f"Escolha do computador: {palpite_comp} \nVocê Ganhou!")
    elif escolha_usuario == "papel" and palpite_comp == "tesoura":
        Result.set(f"Escolha do computador: {palpite_comp} \nComputador Ganhou!")
    elif escolha_usuario == "pedra" and palpite_comp == "tesoura":
        Result.set(f"Escolha do computador: {palpite_comp} \nVocê Ganhou!")
    elif escolha_usuario == "tesoura" and palpite_comp == "pedra":
        Result.set(f"Escolha do computador: {palpite_comp} \nComputador Ganhou!")
    else:
        print("Escolha incorreta, escolha dentra as opções: pedra, papel, tasoura")


# Resetar
def Reset():
    Result.set("")
    palpite_usuário.set("")


# Saida
def Exit():
    raiz.destroy()


# Butões

Entry(raiz, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)

Button(raiz, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(raiz, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(raiz, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

raiz.mainloop()
