import json
import os
import tkinter as tk
from tkinter import messagebox


PESSOAS = []


if os.path.exists("pessoas.json"):
    ARQUIVO = open("pessoas.json", "r")
    PESSOAS = json.load(ARQUIVO)
    ARQUIVO.close()


def SALVAR():
    ARQUIVO = open("pessoas.json", "w")
    json.dump(PESSOAS, ARQUIVO, indent=4)
    ARQUIVO.close()


def CADASTRAR():

    JANELA_CADASTRO = tk.Toplevel(JANELA)
    JANELA_CADASTRO.title("Cadastrar Pessoa")
    JANELA_CADASTRO.geometry("500x600")
    JANELA_CADASTRO.configure(bg="#111111")

    TITULO = tk.Label(
        JANELA_CADASTRO,
        text="CADASTRAR PESSOA",
        font=("Segoe UI", 22, "bold"),
        bg="#111111",
        fg="white"
    )
    TITULO.pack(pady=(35, 30))

    tk.Label(
        JANELA_CADASTRO,
        text="Nome",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="#aaaaaa"
    ).pack(anchor="w", padx=60)

    NOME = tk.Entry(
        JANELA_CADASTRO,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    NOME.pack(fill="x", padx=60, ipady=8, pady=(5, 18))

    tk.Label(
        JANELA_CADASTRO,
        text="Idade",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="#aaaaaa"
    ).pack(anchor="w", padx=60)

    IDADE = tk.Entry(
        JANELA_CADASTRO,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    IDADE.pack(fill="x", padx=60, ipady=8, pady=(5, 18))

    tk.Label(
        JANELA_CADASTRO,
        text="Email",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="#aaaaaa"
    ).pack(anchor="w", padx=60)

    EMAIL = tk.Entry(
        JANELA_CADASTRO,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    EMAIL.pack(fill="x", padx=60, ipady=8, pady=(5, 18))

    tk.Label(
        JANELA_CADASTRO,
        text="Telefone",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="#aaaaaa"
    ).pack(anchor="w", padx=60)

    TELEFONE = tk.Entry(
        JANELA_CADASTRO,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    TELEFONE.pack(fill="x", padx=60, ipady=8, pady=(5, 25))


    def SALVAR_PESSOA():

        if NOME.get() == "":
            messagebox.showwarning("Atenção", "Digite o nome!")
            return

        if IDADE.get() == "":
            messagebox.showwarning("Atenção", "Digite a idade!")
            return

        if EMAIL.get() == "":
            messagebox.showwarning("Atenção", "Digite o email!")
            return

        if TELEFONE.get() == "":
            messagebox.showwarning("Atenção", "Digite o telefone!")
            return

        PESSOA = {
            "nome": NOME.get(),
            "idade": IDADE.get(),
            "email": EMAIL.get(),
            "telefone": TELEFONE.get()
        }

        PESSOAS.append(PESSOA)

        SALVAR()

        messagebox.showinfo(
            "Sucesso",
            "Pessoa cadastrada com sucesso!"
        )

        JANELA_CADASTRO.destroy()


    BOTAO = tk.Button(
        JANELA_CADASTRO,
        text="CADASTRAR",
        command=SALVAR_PESSOA,
        font=("Segoe UI", 11, "bold"),
        bg="#ffffff",
        fg="#111111",
        activebackground="#dddddd",
        relief="flat",
        cursor="hand2"
    )

    BOTAO.pack(fill="x", padx=60, ipady=10)


def LISTAR():

    JANELA_LISTAR = tk.Toplevel(JANELA)
    JANELA_LISTAR.title("Pessoas cadastradas")
    JANELA_LISTAR.geometry("650x600")
    JANELA_LISTAR.configure(bg="#111111")

    TITULO = tk.Label(
        JANELA_LISTAR,
        text="PESSOAS CADASTRADAS",
        font=("Segoe UI", 22, "bold"),
        bg="#111111",
        fg="white"
    )
    TITULO.pack(pady=30)

    if len(PESSOAS) == 0:

        tk.Label(
            JANELA_LISTAR,
            text="Nenhuma pessoa cadastrada.",
            font=("Segoe UI", 13),
            bg="#111111",
            fg="#888888"
        ).pack(pady=40)

    else:

        for PESSOA in PESSOAS:

            CARTAO = tk.Frame(
                JANELA_LISTAR,
                bg="#1b1b1b"
            )

            CARTAO.pack(
                fill="x",
                padx=40,
                pady=8
            )

            TEXTO = (
                PESSOA["nome"] +
                "\n" +
                PESSOA["idade"] +
                " anos" +
                "\n" +
                PESSOA["email"] +
                "\n" +
                PESSOA["telefone"]
            )

            tk.Label(
                CARTAO,
                text=TEXTO,
                font=("Segoe UI", 11),
                bg="#1b1b1b",
                fg="white",
                justify="left"
            ).pack(
                anchor="w",
                padx=20,
                pady=15
            )


def PESQUISAR():

    JANELA_PESQUISA = tk.Toplevel(JANELA)
    JANELA_PESQUISA.title("Pesquisar")
    JANELA_PESQUISA.geometry("500x400")
    JANELA_PESQUISA.configure(bg="#111111")

    tk.Label(
        JANELA_PESQUISA,
        text="PESQUISAR PESSOA",
        font=("Segoe UI", 22, "bold"),
        bg="#111111",
        fg="white"
    ).pack(pady=35)

    NOME_PESQUISA = tk.Entry(
        JANELA_PESQUISA,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    NOME_PESQUISA.pack(
        fill="x",
        padx=60,
        ipady=10
    )

    RESULTADO = tk.Label(
        JANELA_PESQUISA,
        text="",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="white",
        justify="left"
    )

    RESULTADO.pack(pady=30)


    def PESQUISAR_PESSOA():

        ENCONTROU = False

        for PESSOA in PESSOAS:

            if NOME_PESQUISA.get() == PESSOA["nome"]:

                ENCONTROU = True

                RESULTADO.config(
                    text=
                    "NOME: " + PESSOA["nome"] +
                    "\nIDADE: " + PESSOA["idade"] +
                    "\nEMAIL: " + PESSOA["email"] +
                    "\nTELEFONE: " + PESSOA["telefone"]
                )

        if ENCONTROU == False:

            RESULTADO.config(
                text="PESSOA NÃO ENCONTRADA",
                fg="#ff5555"
            )


    tk.Button(
        JANELA_PESQUISA,
        text="PESQUISAR",
        command=PESQUISAR_PESSOA,
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#111111",
        relief="flat",
        cursor="hand2"
    ).pack(
        padx=60,
        fill="x",
        ipady=10,
        pady=15
    )


def ALTERAR():

    JANELA_ALTERAR = tk.Toplevel(JANELA)
    JANELA_ALTERAR.title("Alterar cadastro")
    JANELA_ALTERAR.geometry("500x650")
    JANELA_ALTERAR.configure(bg="#111111")

    tk.Label(
        JANELA_ALTERAR,
        text="ALTERAR CADASTRO",
        font=("Segoe UI", 22, "bold"),
        bg="#111111",
        fg="white"
    ).pack(pady=30)

    CAMPOS = []

    NOMES = [
        "Nome atual",
        "Novo nome",
        "Nova idade",
        "Novo email",
        "Novo telefone"
    ]

    for TEXTO in NOMES:

        tk.Label(
            JANELA_ALTERAR,
            text=TEXTO,
            font=("Segoe UI", 10),
            bg="#111111",
            fg="#aaaaaa"
        ).pack(anchor="w", padx=60)

        CAMPO = tk.Entry(
            JANELA_ALTERAR,
            font=("Segoe UI", 11),
            bg="#1f1f1f",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        CAMPO.pack(
            fill="x",
            padx=60,
            ipady=8,
            pady=(3, 12)
        )

        CAMPOS.append(CAMPO)


    def ALTERAR_PESSOA():

        NOME_ATUAL = CAMPOS[0].get()

        ENCONTROU = False

        for PESSOA in PESSOAS:

            if NOME_ATUAL == PESSOA["nome"]:

                ENCONTROU = True

                PESSOA["nome"] = CAMPOS[1].get()
                PESSOA["idade"] = CAMPOS[2].get()
                PESSOA["email"] = CAMPOS[3].get()
                PESSOA["telefone"] = CAMPOS[4].get()

                SALVAR()

                messagebox.showinfo(
                    "Sucesso",
                    "Cadastro alterado com sucesso!"
                )

                JANELA_ALTERAR.destroy()

                break

        if ENCONTROU == False:

            messagebox.showwarning(
                "Atenção",
                "Pessoa não encontrada!"
            )


    tk.Button(
        JANELA_ALTERAR,
        text="SALVAR ALTERAÇÕES",
        command=ALTERAR_PESSOA,
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#111111",
        relief="flat",
        cursor="hand2"
    ).pack(
        fill="x",
        padx=60,
        ipady=10,
        pady=10
    )


def EXCLUIR():

    JANELA_EXCLUIR = tk.Toplevel(JANELA)
    JANELA_EXCLUIR.title("Excluir cadastro")
    JANELA_EXCLUIR.geometry("500x350")
    JANELA_EXCLUIR.configure(bg="#111111")

    tk.Label(
        JANELA_EXCLUIR,
        text="EXCLUIR CADASTRO",
        font=("Segoe UI", 22, "bold"),
        bg="#111111",
        fg="white"
    ).pack(pady=35)

    tk.Label(
        JANELA_EXCLUIR,
        text="Digite o nome da pessoa:",
        font=("Segoe UI", 11),
        bg="#111111",
        fg="#aaaaaa"
    ).pack()

    NOME_EXCLUIR = tk.Entry(
        JANELA_EXCLUIR,
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        insertbackground="white",
        relief="flat"
    )

    NOME_EXCLUIR.pack(
        fill="x",
        padx=60,
        ipady=10,
        pady=15
    )


    def EXCLUIR_PESSOA():

        for PESSOA in PESSOAS:

            if NOME_EXCLUIR.get() == PESSOA["nome"]:

                CONFIRMAR = messagebox.askyesno(
                    "Confirmar exclusão",
                    "Tem certeza que deseja excluir?"
                )

                if CONFIRMAR:

                    PESSOAS.remove(PESSOA)

                    SALVAR()

                    messagebox.showinfo(
                        "Sucesso",
                        "Cadastro excluído com sucesso!"
                    )

                    JANELA_EXCLUIR.destroy()

                return


        messagebox.showwarning(
            "Atenção",
            "Pessoa não encontrada!"
        )


    tk.Button(
        JANELA_EXCLUIR,
        text="EXCLUIR",
        command=EXCLUIR_PESSOA,
        font=("Segoe UI", 11, "bold"),
        bg="#ff4444",
        fg="white",
        activebackground="#cc3333",
        relief="flat",
        cursor="hand2"
    ).pack(
        fill="x",
        padx=60,
        ipady=10
    )


def SAIR():

    JANELA.destroy()


JANELA = tk.Tk()

JANELA.title("Sistema de Cadastro")

JANELA.geometry("900x600")

JANELA.configure(bg="#0b0b0b")


LATERAL = tk.Frame(
    JANELA,
    bg="#151515",
    width=230
)

LATERAL.pack(
    side="left",
    fill="y"
)

LATERAL.pack_propagate(False)


tk.Label(
    LATERAL,
    text="SISTEMA",
    font=("Segoe UI", 22, "bold"),
    bg="#151515",
    fg="white"
).pack(pady=(50, 0))

tk.Label(
    LATERAL,
    text="CADASTRO",
    font=("Segoe UI", 22, "bold"),
    bg="#151515",
    fg="#888888"
).pack()


tk.Label(
    LATERAL,
    text="────────────────",
    font=("Segoe UI", 10),
    bg="#151515",
    fg="#333333"
).pack(pady=25)


def CRIAR_BOTAO(TEXTO, COMANDO):

    return tk.Button(
        LATERAL,
        text=TEXTO,
        command=COMANDO,
        font=("Segoe UI", 11, "bold"),
        bg="#151515",
        fg="white",
        activebackground="#2a2a2a",
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=25,
        cursor="hand2"
    )


CRIAR_BOTAO(
    "   Cadastrar pessoa",
    CADASTRAR
).pack(
    fill="x",
    ipady=12
)


CRIAR_BOTAO(
    "   Listar pessoas",
    LISTAR
).pack(
    fill="x",
    ipady=12
)


CRIAR_BOTAO(
    "   Pesquisar",
    PESQUISAR
).pack(
    fill="x",
    ipady=12
)


CRIAR_BOTAO(
    "   Alterar cadastro",
    ALTERAR
).pack(
    fill="x",
    ipady=12
)


CRIAR_BOTAO(
    "   Excluir cadastro",
    EXCLUIR
).pack(
    fill="x",
    ipady=12
)


CRIAR_BOTAO(
    "   Sair",
    SAIR
).pack(
    side="bottom",
    fill="x",
    ipady=12
)


CONTEUDO = tk.Frame(
    JANELA,
    bg="#0b0b0b"
)

CONTEUDO.pack(
    side="left",
    fill="both",
    expand=True
)


tk.Label(
    CONTEUDO,
    text="Olá! 👋",
    font=("Segoe UI", 30, "bold"),
    bg="#0b0b0b",
    fg="white"
).pack(
    anchor="w",
    padx=55,
    pady=(60, 5)
)


tk.Label(
    CONTEUDO,
    text="Gerencie seus cadastros de forma simples.",
    font=("Segoe UI", 13),
    bg="#0b0b0b",
    fg="#777777"
).pack(
    anchor="w",
    padx=55
)


CARTAO = tk.Frame(
    CONTEUDO,
    bg="#151515"
)

CARTAO.pack(
    fill="x",
    padx=55,
    pady=45
)


tk.Label(
    CARTAO,
    text="Pessoas cadastradas",
    font=("Segoe UI", 12),
    bg="#151515",
    fg="#888888"
).pack(
    anchor="w",
    padx=25,
    pady=(25, 5)
)


QUANTIDADE = tk.Label(
    CARTAO,
    text=str(len(PESSOAS)),
    font=("Segoe UI", 38, "bold"),
    bg="#151515",
    fg="white"
)

QUANTIDADE.pack(
    anchor="w",
    padx=25,
    pady=(0, 25)
)


JANELA.mainloop()
