import tkinter as tk

class Janela(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text='Digite o nome do arquivo:')
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.botao = tk.Button(self, text='Enviar', command=self.submit)
        self.botao.pack()

        self.nome_arquivo = ''

    def submit(self):
        self.nome_arquivo = self.entry.get()
        self.destroy()

