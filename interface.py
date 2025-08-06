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
    try:
        inserir_venda(
            produto=produto_entry.get(),
            categoria=categoria_entry.get(),
            valor=float(valor_entry.get()),
            data_venda=data_entry.get(),
            cliente=cliente_entry.get()
        )
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Venda adicionada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar: {e}")

def editar_venda_interface():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione uma venda para editar.")
        return

    valores = tree.item(item_selecionado)["values"]
    id_venda = valores[0]

    try:
        editar_venda(
            id_venda,
            produto_entry.get(),
            categoria_entry.get(),
            float(valor_entry.get()),
            data_entry.get(),
            cliente_entry.get()
        )
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Venda editada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao editar: {e}")

def deletar_venda_interface():
    item_selecionado = tree.selection()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione uma venda para deletar.")
        return

    valores = tree.item(item_selecionado)["values"]
    id_venda = valores[0]

    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir esta venda?")
    if confirmacao:
        try:
            deletar_venda(id_venda)
            atualizar_lista()
            messagebox.showinfo("Sucesso", "Venda deletada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar: {e}")

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

# Botao

tk.Button(janela, text="Adicionar Venda", command=adicionar_venda).grid(row=5, columnspan=2, pady=5)
tk.Button(janela, text="Editar Venda", command=editar_venda_interface).grid(row=6, columnspan=2, pady=5)
tk.Button(janela, text="Deletar Venda", command=deletar_venda_interface).grid(row=7, columnspan=2, pady=5)

# Tabela

colunas = ("ID", "Produto", "Categoria", "Valor", "Data", "Cliente")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, minwidth=0, width=100)

tree.grid(row=8, column=0, columnspan=2, pady=10)

# Atualizar lista ao iniciar

atualizar_lista()

janela.mainloop()
