import tkinter as tk

COR_FUNDO = "#2d2d2d"
COR_DISPLAY = "#1e1e1e"
COR_TEXTO_DISPLAY = "#FFFFFF"
COR_BOTAO_NUM = "#404040"
COR_BOTAO_OP = "#505050"
COR_BOTAO_IGUAL = "#0078d7"
COR_TEXTO_BOTAO = "#FFFFFF"
COR_HOVER = "#606060"

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("340x520")
        self.root.resizable(False, False)
        self.root.configure(bg=COR_FUNDO)

        self.expressao_atual = ""

        self.display_frame = self.criar_display_frame()
        self.display_label = self.criar_display_label()
        self.botoes_frame = self.criar_botoes_frame()

        self.botoes_layout = [
            ('C', 1, 0, 'op'), ('+/-', 1, 1, 'op'), ('%', 1, 2, 'op'), ('/', 1, 3, 'op'),
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('*', 2, 3, 'op'),
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('-', 3, 3, 'op'),
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'), ('+', 4, 3, 'op'),
            ('0', 5, 0, 'num', 2), ('.', 5, 2, 'num'), ('=', 5, 3, 'igual'),
        ]

        self.criar_botoes()

    def criar_display_frame(self):
        frame = tk.Frame(self.root, height=120, bg=COR_FUNDO)
        frame.pack(expand=True, fill="both")
        return frame

    def criar_display_label(self):
        label = tk.Label(self.display_frame, text=self.expressao_atual, anchor=tk.E, bg=COR_DISPLAY,
                         fg=COR_TEXTO_DISPLAY, padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")
        return label

    def criar_botoes_frame(self):
        frame = tk.Frame(self.root, bg=COR_FUNDO)
        frame.pack(expand=True, fill="both")
        return frame

    def criar_botoes(self):
        for (texto, linha, coluna, tipo, *args) in self.botoes_layout:
            colspan = args[0] if args else 1

            if tipo == 'num':
                cor_bg = COR_BOTAO_NUM
            elif tipo == 'op':
                cor_bg = COR_BOTAO_OP
            else:
                cor_bg = COR_BOTAO_IGUAL

            btn = tk.Button(self.botoes_frame, text=texto, bg=cor_bg, fg=COR_TEXTO_BOTAO,
                            font=("Arial", 20), borderwidth=0,
                            command=lambda t=texto: self.ao_clicar(t))

            btn.grid(row=linha, column=coluna, columnspan=colspan, sticky=tk.NSEW, padx=1, pady=1)

            btn.bind("<Enter>", lambda e, b=btn, c=COR_HOVER: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=cor_bg: b.config(bg=c))

        for i in range(6):
            self.botoes_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.botoes_frame.grid_columnconfigure(i, weight=1)

    def ao_clicar(self, valor):
        if valor == 'C':
            self.limpar_tudo()
        elif valor == '=':
            self.calcular_resultado()
        elif valor == '+/-':
            self.negar()
        else:
            self.adicionar_a_expressao(valor)

    def adicionar_a_expressao(self, valor):
        if self.expressao_atual == "Erro":
            self.expressao_atual = ""
        self.expressao_atual += str(valor)
        self.atualizar_visor()

    def limpar_tudo(self):
        self.expressao_atual = ""
        self.atualizar_visor()

    def calcular_resultado(self):
        try:
            expressao_para_eval = self.expressao_atual.replace('%', '/100')
            resultado = str(eval(expressao_para_eval))
            self.expressao_atual = resultado
        except Exception:
            self.expressao_atual = "Erro"
        finally:
            self.atualizar_visor()

    def negar(self):
        if self.expressao_atual and self.expressao_atual != "Erro":
            if self.expressao_atual.startswith('-'):
                self.expressao_atual = self.expressao_atual[1:]
            else:
                self.expressao_atual = '-' + self.expressao_atual
            self.atualizar_visor()

    def atualizar_visor(self):
        if len(self.expressao_atual) > 11:
            self.display_label.config(font=("Arial", 20, "bold"))
        else:
            self.display_label.config(font=("Arial", 40, "bold"))
        self.display_label.config(text=self.expressao_atual[:22])

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
