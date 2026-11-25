import tkinter as tk 
from tkinter import messagebox


def abrir_vendas(janela_principal):
    janela = tk.Toplevel(janela_principal)
    janela.title("Vesdas")
    janela.geometry("600x500")
    janela.resizable(False, False)