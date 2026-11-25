import tkinter as tk
from tkinter import ttk, messagebox


categoria = [
    "Manutenção",
    "Instalação",
    "Consultoria",
    "Suporte Técnico",
    "Outros"
]

unidade = [
    "Serviço",
    "Hora",
    "Dia",
    "Unidade"
]


def abrir_cadastro_servico(janela_principal):

    janela = tk.Toplevel(janela_principal)
    janela.title("Cadastro de Serviço")
    janela.geometry("600x500")
    janela.resizable(False, False)

    def salvar():
        nome = digito_nome.get().strip()
        descricao_1 = campo_desricao.get("1.0", tk.END).strip()
        categoria_1 = campo_categoria.get().strip()
        unidade_1 = campo_unidade.get().strip()

        # Verificação de nome vazio
        if nome == "":
            messagebox.showwarning(
                "Atenção",
                "O campo nome não pode ficar vazio!"
            )
            digito_nome.focus_force()
            digito_nome.delete(0, tk.END)
            return

        # Verificação de números no nome
        if not nome.replace(" ", "").isalpha():
            messagebox.showwarning(
                "Atenção",
                "O campo nome não pode conter números!"
            )
            digito_nome.focus_set()
            digito_nome.delete(0, tk.END)
            return

        # Verificação de descrição
        if descricao_1 == "":
            messagebox.showwarning(
                "Atenção",
                "O campo descrição não pode ficar vazio!"
            )
            campo_desricao.focus_set()
            return

        # Verificação de categoria
        if categoria_1 == "":
            messagebox.showwarning(
                "Atenção",
                "Selecione uma categoria!"
            )
            campo_categoria.focus_set()
            return

        # Verificação de unidade
        if unidade_1 == "":
            messagebox.showwarning(
                "Atenção",
                "Selecione uma unidade!"
            )
            campo_unidade.focus_set()
            return

        messagebox.showinfo(
            "Sucesso",
            "Serviço cadastrado com sucesso!"
        )

    def cancelar():
        digito_nome.delete(0, tk.END)
        campo_desricao.delete("1.0", tk.END)
        campo_categoria.set("")
        campo_unidade.set("")

    # Criação da Frame
    tela_frame = tk.LabelFrame(
        janela,
        text="Cadastro de Serviços",
        font=("Arial", 13, "bold")
    )
    tela_frame.pack(padx=10)

    # Campo nome
    campo_nome = tk.Label(
        tela_frame,
        text="Nome",
        font=("Arial", 12)
    )
    campo_nome.grid(
        row=0,
        column=0,
        padx=(10, 3),
        pady=10
    )

    digito_nome = tk.Entry(
        tela_frame,
        font=("Arial", 11)
    )
    digito_nome.grid(
        row=0,
        column=1,
        padx=(3, 10),
        pady=10
    )

    # Categoria
    digito_categoria = tk.Label(
        tela_frame,
        text="Categoria",
        font=("Arial", 12)
    )
    digito_categoria.grid(
        row=0,
        column=2,
        padx=(10, 2),
        pady=10
    )

    campo_categoria = ttk.Combobox(
        tela_frame,
        values=categoria,
        state="readonly",
        font=("Arial", 11)
    )
    campo_categoria.grid(
        row=0,
        column=3,
        padx=(3, 10),
        pady=10
    )

    # Unidade
    digito_unidade = tk.Label(
        tela_frame,
        text="Unidade",
        font=("Arial", 12)
    )
    digito_unidade.grid(
        row=1,
        column=2,
        padx=(10, 3),
        pady=10
    )

    campo_unidade = ttk.Combobox(
        tela_frame,
        values=unidade,
        state="readonly",
        font=("Arial", 11)
    )
    campo_unidade.grid(
        row=1,
        column=3,
        padx=(2, 10),
        pady=10
    )

    # Descrição
    digito_descricao = tk.Label(
        tela_frame,
        text="Descrição",
        font=("Arial", 12)
    )
    digito_descricao.grid(
        row=2,
        column=0,
        padx=(10, 2),
        pady=10
    )

    campo_desricao = tk.Text(
        tela_frame,
        font=("Arial", 11),
        width=35,
        height=4
    )
    campo_desricao.grid(
        row=2,
        column=1,
        columnspan=3,
        sticky="w",
        padx=(2, 10),
        pady=10
    )

    # Botão cadastrar
    botao_cadastrar = tk.Button(
        tela_frame,
        text="Cadastrar",
        command=salvar,
        font=("Arial", 12)
    )
    botao_cadastrar.grid(
        row=3,
        column=0,
        padx=20,
        pady=20
    )

    # Botão cancelar
    botao_cacelar = tk.Button(
        tela_frame,
        text="Cancelar",
        command=cancelar,
        font=("Arial", 12)
    )
    botao_cacelar.grid(
        row=3,
        column=1,
        padx=20,
        pady=20
    )