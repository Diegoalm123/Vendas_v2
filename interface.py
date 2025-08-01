import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def cadastrar_venda():
    produto= entry_produto.get()
    categoria=entry_categoria.get()
    valor=entry_valor.get()
    data_venda = entry_data.get()
    cliente = entry_cliente.get()