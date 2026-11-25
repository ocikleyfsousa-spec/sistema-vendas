import re
import tkinter as tk
from tkinter import messagebox, ttk

ufs = [
    "AC - Acre",
    "AL - Alagoas",
    "AP - Amapá",
    "AM - Amazonas",
    "BA - Bahia",
    "CE - Ceará",
    "DF - Distrito Federal",
    "ES - Espírito Santo",
    "GO - Goiás",
    "MA - Maranhão",
    "MT - Mato Grosso",
    "MS - Mato Grosso do Sul",
    "MG - Minas Gerais",
    "PA - Pará",
    "PB - Paraíba",
    "PR - Paraná",
    "PE - Pernambuco",
    "PI - Piauí",
    "RJ - Rio de Janeiro",
    "RN - Rio Grande do Norte",
    "RS - Rio Grande do Sul",
    "RO - Rondônia",
    "RR - Roraima",
    "SC - Santa Catarina",
    "SP - São Paulo",
    "SE - Sergipe",
    "TO - Tocantins",
]


def abrir_cadastro_cliente(janela_principal):
  janela = tk.Toplevel(janela_principal)
  janela.title("Cadastro de Cliente")
  janela.geometry("750x550")
  janela.resizable(False, False)

  # ==========================================================
  # Função Cadastro
  # ==========================================================
  def cadastro():
    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    cpf = entrada_cpf.get().strip()
    email = entrada_email.get().strip()
    cep = entrada_cep.get().strip()
    rua = entrada_rua.get().strip()
    numero = entrada_numero.get().strip()
    bairro = entrada_bairro.get().strip()
    cidade = entrada_cidade.get().strip()
    estado = entrada_uf.get()

    # 1. Validação Nome
    if not nome:
      messagebox.showwarning("Atenção", "Informe o nome do cliente!")
      entrada_nome.focus_set()
      return

    if not nome.replace(" ", "").isalpha():
      messagebox.showwarning(
          "Atenção",
          "O campo Nome/Razão Social não pode conter números ou caracteres"
          " especiais.",
      )
      entrada_nome.delete(0, tk.END)
      entrada_nome.focus_set()
      return

    # 2. Validação Telefone
    if not telefone:
      messagebox.showwarning("Atenção", "Informe o Telefone do Cliente!")
      entrada_telefone.focus_set()
      return

    telefone_limpo = (
        telefone.replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    if not telefone_limpo.isdigit():
      messagebox.showwarning(
          "Atenção", "O campo Telefone não pode conter letras."
      )
      entrada_telefone.delete(0, tk.END)
      entrada_telefone.focus_set()
      return

    if len(telefone_limpo) not in (10, 11):
      messagebox.showwarning(
          "Atenção", "Informe um telefone válido com 10 ou 11 números."
      )
      entrada_telefone.delete(0, tk.END)
      entrada_telefone.focus_set()
      return

    # 3. Validação CPF
    if not cpf:
      messagebox.showwarning("Atenção", "O campo CPF não pode ficar vazio!")
      entrada_cpf.focus_set()
      return

    cpf_limpo = cpf.replace(".", "").replace("-", "").replace(" ", "")

    if not cpf_limpo.isdigit():
      messagebox.showwarning("Atenção", "O campo CPF não pode conter letras!")
      entrada_cpf.delete(0, tk.END)
      entrada_cpf.focus_set()
      return

    if len(cpf_limpo) != 11 or len(set(cpf_limpo)) == 1:
      messagebox.showwarning("Atenção", "O CPF deve conter 11 números válidos!")
      entrada_cpf.delete(0, tk.END)
      entrada_cpf.focus_set()
      return

    soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    if int(cpf_limpo[9]) != digito1 or int(cpf_limpo[10]) != digito2:
      messagebox.showwarning("Atenção", "CPF inválido!")
      entrada_cpf.delete(0, tk.END)
      entrada_cpf.focus_set()
      return

    # 4. Validação E-mail
    if not email:
      messagebox.showwarning("Atenção", "O campo E-mail não pode ficar vazio!")
      entrada_email.focus_set()
      return

    if not re.fullmatch(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email
    ):
      messagebox.showwarning("Atenção", "Informe um endereço de e-mail válido!")
      entrada_email.delete(0, tk.END)
      entrada_email.focus_set()
      return

    # 5. Validação CEP
    if not cep:
      messagebox.showwarning("Atenção", "O campo CEP não pode ficar vazio!")
      entrada_cep.focus_set()
      return

    numeros_cep = cep.replace("-", "")
    if not re.fullmatch(r"\d{5}-?\d{3}", cep) or len(set(numeros_cep)) == 1:
      messagebox.showwarning(
          "Atenção",
          "Digite um CEP válido com 8 dígitos (ex: 65840-000 ou 65840000).",
      )
      entrada_cep.delete(0, tk.END)
      entrada_cep.focus_set()
      return

    cep_formatado = f"{numeros_cep[:5]}-{numeros_cep[5:]}"
    entrada_cep.delete(0, tk.END)
    entrada_cep.insert(0, cep_formatado)

    # 6. Validação Endereço
    if not rua or not numero or not bairro or not cidade or not estado:
      messagebox.showwarning(
          "Atenção",
          "Preencha todos os campos de endereço (Rua, Número, Bairro, Cidade e"
          " UF)!",
      )
      return

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    limpar()

  # ==========================================================
  # Função Limpar
  # ==========================================================
  def limpar():
    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_cep.delete(0, tk.END)
    entrada_rua.delete(0, tk.END)
    entrada_numero.delete(0, tk.END)
    entrada_bairro.delete(0, tk.END)
    entrada_cidade.delete(0, tk.END)
    entrada_uf.set("")

  # ==========================================================
  # FRAME PESQUISA
  # ==========================================================
  pesquisa_frame = tk.LabelFrame(janela, text="Pesquisa", font=("Arial", 12))
  pesquisa_frame.pack(padx=20, pady=10, fill="x")

  tk.Label(pesquisa_frame, text="Nome", font=("Arial", 12)).grid(
      row=0, column=0, padx=(10, 5), pady=10
  )
  entrada_pesquisa = tk.Entry(pesquisa_frame, font=("Arial", 11), width=45)
  entrada_pesquisa.grid(row=0, column=1, padx=5, pady=10)

  btn_pesquisar = tk.Button(
      pesquisa_frame, text="Pesquisar", font=("Arial", 12)
  )
  btn_pesquisar.grid(row=0, column=2, padx=10, pady=10)

  # ==========================================================
  # FRAME DADOS DO CLIENTE
  # ==========================================================
  dados_pessoais = tk.LabelFrame(
      janela, text="Dados do Cliente", font=("Arial", 12), padx=10, pady=10
  )
  dados_pessoais.pack(padx=20, pady=10, fill="x")

  # Linha 0: Nome
  tk.Label(dados_pessoais, text="Nome:", font=("Arial", 11)).grid(
      row=0, column=0, sticky="w", pady=5
  )
  entrada_nome = tk.Entry(dados_pessoais, font=("Arial", 11), width=55)
  entrada_nome.grid(
      row=0, column=1, columnspan=3, sticky="w", pady=5, padx=(5, 0)
  )

  # Linha 1: Telefone e CPF
  tk.Label(dados_pessoais, text="Telefone:", font=("Arial", 11)).grid(
      row=1, column=0, sticky="w", pady=5
  )
  entrada_telefone = tk.Entry(dados_pessoais, font=("Arial", 11), width=22)
  entrada_telefone.grid(row=1, column=1, sticky="w", pady=5, padx=(5, 15))

  tk.Label(dados_pessoais, text="CPF:", font=("Arial", 11)).grid(
      row=1, column=2, sticky="w", pady=5
  )
  entrada_cpf = tk.Entry(dados_pessoais, font=("Arial", 11), width=22)
  entrada_cpf.grid(row=1, column=3, sticky="w", pady=5, padx=(5, 0))

  # Linha 2: E-mail e CEP
  tk.Label(dados_pessoais, text="E-mail:", font=("Arial", 11)).grid(
      row=2, column=0, sticky="w", pady=5
  )
  entrada_email = tk.Entry(dados_pessoais, font=("Arial", 11), width=28)
  entrada_email.grid(row=2, column=1, sticky="w", pady=5, padx=(5, 15))

  tk.Label(dados_pessoais, text="CEP:", font=("Arial", 11)).grid(
      row=2, column=2, sticky="w", pady=5
  )
  entrada_cep = tk.Entry(dados_pessoais, font=("Arial", 11), width=18)
  entrada_cep.grid(row=2, column=3, sticky="w", pady=5, padx=(5, 0))

  # Linha 3: Rua e Número
  tk.Label(dados_pessoais, text="Rua:", font=("Arial", 11)).grid(
      row=3, column=0, sticky="w", pady=5
  )
  entrada_rua = tk.Entry(dados_pessoais, font=("Arial", 11), width=35)
  entrada_rua.grid(row=3, column=1, sticky="w", pady=5, padx=(5, 15))

  tk.Label(dados_pessoais, text="Número:", font=("Arial", 11)).grid(
      row=3, column=2, sticky="w", pady=5
  )
  entrada_numero = tk.Entry(dados_pessoais, font=("Arial", 11), width=12)
  entrada_numero.grid(row=3, column=3, sticky="w", pady=5, padx=(5, 0))

  # Linha 4: Bairro e Cidade
  tk.Label(dados_pessoais, text="Bairro:", font=("Arial", 11)).grid(
      row=4, column=0, sticky="w", pady=5
  )
  entrada_bairro = tk.Entry(dados_pessoais, font=("Arial", 11), width=25)
  entrada_bairro.grid(row=4, column=1, sticky="w", pady=5, padx=(5, 15))

  tk.Label(dados_pessoais, text="Cidade:", font=("Arial", 11)).grid(
      row=4, column=2, sticky="w", pady=5
  )
  entrada_cidade = tk.Entry(dados_pessoais, font=("Arial", 11), width=22)
  entrada_cidade.grid(row=4, column=3, sticky="w", pady=5, padx=(5, 0))

  # Linha 5: UF
  tk.Label(dados_pessoais, text="UF:", font=("Arial", 11)).grid(
      row=5, column=0, sticky="w", pady=5
  )
  entrada_uf = ttk.Combobox(
      dados_pessoais, values=ufs, font=("Arial", 11), width=23, state="readonly"
  )
  entrada_uf.grid(row=5, column=1, sticky="w", pady=5, padx=(5, 0))

  # ==========================================================
  # BOTÕES DE AÇÃO
  # ==========================================================
  botoes_frame = tk.Frame(janela)
  botoes_frame.pack(pady=15)

  btn_cadastrar = tk.Button(
      botoes_frame,
      text="Cadastrar",
      font=("Arial", 12),
      width=14,
      command=cadastro,
  )
  btn_cadastrar.grid(row=0, column=0, padx=10)

  btn_limpar = tk.Button(
      botoes_frame,
      text="Limpar",
      font=("Arial", 12),
      width=14,
  )