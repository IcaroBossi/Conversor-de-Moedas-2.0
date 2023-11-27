# Algoritmo para conversão de moedas utilizando uma interface gráfica.

import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class ConversorMoedasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas")

        # Variáveis
        self.valor_var = tk.DoubleVar()
        # Aqui é possível adicionar mais moedas conforme necessário
        self.moedas_disponiveis = ["USD", "EUR", "GBP", "JPY", "AUD", "BRL"]
        self.moeda_origem_var = tk.StringVar(value=self.moedas_disponiveis[0])
        self.moeda_destino_var = tk.StringVar(value=self.moedas_disponiveis[1])
        self.resultado_var = tk.StringVar()

        # Configuração da Interface Gráfica
        self.criar_widgets()

    def converter_moeda(self):
        valor = self.valor_var.get()
        moeda_origem = self.moeda_origem_var.get()
        moeda_destino = self.moeda_destino_var.get()

        if valor and moeda_origem and moeda_destino:
            c = CurrencyRates()
            taxa = c.get_rate(moeda_origem, moeda_destino)
            resultado = valor * taxa
            self.resultado_var.set(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        else:
            self.resultado_var.set("Preencha todos os campos.")

    def criar_widgets(self):
        # Layout com Grid
        tk.Label(self.root, text="Valor:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.valor_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Moeda de Origem:").grid(row=1, column=0, padx=10, pady=5)
        ttk.Combobox(self.root, textvariable=self.moeda_origem_var, values=self.moedas_disponiveis).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Moeda de Destino:").grid(row=2, column=0, padx=10, pady=5)
        ttk.Combobox(self.root, textvariable=self.moeda_destino_var, values=self.moedas_disponiveis).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Converter", command=self.converter_moeda).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.root, textvariable=self.resultado_var).grid(row=4, column=0, columnspan=2, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorMoedasApp(root)
    root.mainloop()
