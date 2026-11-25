import tkinter as tk
from modulos import cadastro_servico, cadastro_cliente, venda



janela_principal = tk.Tk()

janela_principal.title("Sistema de Gestão")
janela_principal.geometry("800x600")

botao_cliente = tk.Button(
    janela_principal,
    text="Cadastro de Cliente",
    font=("Arial", 12),
    command=lambda: cadastro_cliente.abrir_cadastro_cliente(janela_principal)
)
botao_cliente.grid(
    row=1,
    column=1,
    padx=20,
    pady=20
)

botao_servico = tk.Button(
    janela_principal,
    text="Cadastro de Serviço",
    font=("Arial", 12),
    command=lambda: cadastro_servico.abrir_cadastro_servico(janela_principal)
)



botao_servico.grid(
    row=1,
    column=2,
    padx=(2, 20),
    pady=20
)

botao_venda = tk.Button(
    janela_principal,
    text="Venda",
    font=("Arial", 12),
    command=lambda:venda.abrir_vendas(janela_principal)
)
botao_venda.grid(
    row=1,
    column=3,
    padx=(2,20),
    pady=20
)


janela_principal.mainloop()