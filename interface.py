from banco import inserir_venda, listar_vendas, editar_venda, deletar_venda
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def atualizar_lista():
    for item in tree.get_children():
        tree.delete(item)
    for row in listar_vendas():
        tree.insert("", tk.END, values=row)

def adicionar_venda():
    inserir_venda(
        produto=produto_entry.get(),
        categoria=categoria_entry.get(),
        valor=float(valor_entry.get()),
        data_venda=data_entry.get(),
        cliente=cliente_entry.get()
    )
    atualizar_lista()
    

# interface

janela = tk.Tk()
janela.title("Sistema de Vendas")

# Entradas

tk.Label(janela, text="Produto").grid(row=0, column=0)
produto_entry = tk.Entry(janela)
produto_entry.grid(row=0, column=1)

tk.Label(janela, text="Categoria").grid(row=1, column=0)
categoria_entry = tk.Entry(janela)
categoria_entry.grid(row=1, column=1)

tk.Label(janela, text="Valor").grid(row=2, column=0)
valor_entry = tk.Entry(janela)
valor_entry.grid(row=2, column=1)

tk.Label(janela, text="Data (YYYY-MM-DD)").grid(row=3, column=0)
data_entry = tk.Entry(janela)
data_entry.grid(row=3, column=1)

tk.Label(janela, text="Cliente").grid(row=4, column=0)
cliente_entry = tk.Entry(janela)
cliente_entry.grid(row=4, column=1)

# Adicionar

tk.Button(janela, text="Adicionar Venda", command=adicionar_venda).grid(row=5, columnspan=2, pady=10)

# tabela

colunas = ("ID", "Produto", "Categoria", "Valor", "Data", "Cliente")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, minwidth=0, width=100)

tree.grid(row=6, column=0, columnspan=2)

# atualizar a tabela

atualizar_lista()

janela.mainloop()