import tkinter as tk
from tkinter import messagebox, ttk


def abrir_vendas(janela_principal):
    janela = tk.Toplevel(janela_principal)
    janela.title("Nova Venda")
    janela.geometry("600x500")
    janela.resizable(False, False)

    # FRAME DO CABEÇALHO
    frame_cabecalho = ttk.Frame(janela)
    frame_cabecalho.pack(
        fill="x",
        padx=20,
        pady=10
    )

    ttk.Label(
        frame_cabecalho,
        text="NOVA VENDA"
    ).pack()

    # LABELFRAME DOS DADOS DO CLIENTE
    frame_dados = tk.LabelFrame(
        janela,
        text="Dados do Cliente",
        font=("Arial", 12, "bold")
    )
    frame_dados.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # NOME
    digito_nome = tk.Label(
        frame_dados,
        text="Nome:",
        font=("Arial", 12, "bold")
    )
    digito_nome.grid(
        row=0,
        column=0,
        padx=20,
        pady=15
    )

    entrada_nome = ttk.Entry(
        frame_dados,
        width=40
    )
    entrada_nome.grid(
        row=0,
        column=1,
        padx=10,
        pady=15
    )
    
    