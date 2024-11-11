# interface.py
import tkinter as tk
from tkinter import messagebox
from gerenciador_tarefas import adicionar, desfazer

def adicinar_tarefa_interface():
    tarefa = entry_gerenciador.get()
    adicionar(tarefa)
    entry_gerenciador.delete(0, tk.END)

def remover_tarefa_interface():
    desfazer()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador e Verificador de CPF")

# Seção para adicionar tarefa 
frame_gerenciador = tk.Frame(root, padx=10, pady=10)
frame_gerenciador.pack(pady=10)

label_gerenciador = tk.Label(frame_gerenciador, text="Adicionar Tarefa:")
label_gerenciador.grid(row=0, column=0, padx=5, pady=5)

entry_gerenciador = tk.Entry(frame_gerenciador, width=20)
entry_gerenciador.grid(row=0, column=1, padx=5, pady=5)

btn_gerenciador = tk.Button(frame_gerenciador, text="Add", command= adicinar_tarefa_interface)
btn_gerenciador.grid(row=0, column=2, padx=5, pady=5)

# Seção para remover tarefa 
frame_removedor = tk.Frame(root, padx=10, pady=10)
frame_removedor.pack(pady=10)

btn_removedor = tk.Button(frame_removedor, text="Remover última tarefa", command= remover_tarefa_interface)
btn_removedor.grid(row=0, column=2, padx=5, pady=5)


root.mainloop()
