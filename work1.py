import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import csv

def mostrar_escolha_radio():
    escolha_radio = escolha_var.get()
    escolha_series = series_var.get()
    label_radio.config(text=f"Treino do Dia: {escolha_radio}, {escolha_series}")

def salvar_dados():
    data = calendario.get_date()
    variacao = combobox_variacao.get()
    grupo_muscular = escolha_var.get()
    progressao = combobox_progressao.get()
    nome_exercicio = entry_exercicio.get()
    sets = spinbox_sets.get()
    reps = spinbox_reps.get()

    # Indexar a data no calendário
    calendario.selection_set(data)

    with open('dados_treino.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, variacao, grupo_muscular, progressao, nome_exercicio, sets, reps])

    # Limpar os campos após salvar
    combobox_variacao.set("Selecione a Variação")
    escolha_var.set('')
    combobox_progressao.set("Selecione a progressão")
    entry_exercicio.delete(0, tk.END)
    spinbox_sets.delete(0, tk.END)
    spinbox_reps.delete(0, tk.END)


# GUI
janela = tk.Tk()
janela.title('Registro de Treinos')
janela.geometry('500x600')  # Aumentei a altura para acomodar o botão de salvar
janela.grid_columnconfigure(0, weight=1)

# Calendário
calendario = Calendar(janela, selectmode='day', date_pattern='dd/MM/yyyy')
calendario.pack(padx=10, pady=(5, 10))

# Label para mostrar a escolha do radio
label_radio = tk.Label(janela, text="GRUPO MUSCULAR:")
label_radio.pack(pady=1)

# Frame para os radio buttons
frame_radio = tk.Frame(janela)
frame_radio.pack(pady=5)

# Combobox para variações de séries
series_var = tk.StringVar()
variacoes_series = ["Press", "Hold", "Reps"]
combobox_variacao = ttk.Combobox(frame_radio, textvariable=series_var, values=variacoes_series, state="readonly")
combobox_variacao.set("Selecione a Variação")
combobox_variacao.pack(padx=5)

# Radio buttons
escolha_var = tk.StringVar()
radio1 = tk.Radiobutton(frame_radio, text="PUSH", variable=escolha_var, value="PUSH", command=mostrar_escolha_radio)
radio2 = tk.Radiobutton(frame_radio, text="PULL", variable=escolha_var, value="PULL", command=mostrar_escolha_radio)
radio1.pack(side=tk.LEFT, padx=5)
radio2.pack(side=tk.LEFT, padx=5)

# Combobox para variações de progressões
progressoes_var = tk.StringVar()
progressoes_series = ["Pike", "Tuck", "Half-Lay", "Straddle", "Full"]
combobox_progressao = ttk.Combobox(frame_radio, textvariable=progressoes_var, values=progressoes_series, state="readonly")
combobox_progressao.set("Selecione a progressão")
combobox_progressao.pack(pady=5)

# Entry para digitar o nome do exercício
label_exercicio = tk.Label(janela, text="Nome do Exercício:")
label_exercicio.pack()
entry_exercicio = tk.Entry(janela)
entry_exercicio.pack(pady=5, padx=10)

# Spinboxes para Sets e Reps
label_sets = tk.Label(janela, text="Sets:")
label_sets.pack(side=tk.LEFT, padx=5)
spinbox_sets = tk.Spinbox(janela, from_=1, to=10)
spinbox_sets.pack(side=tk.LEFT, padx=5)

label_reps = tk.Label(janela, text="Reps:")
label_reps.pack(side=tk.LEFT, padx=5)
spinbox_reps = tk.Spinbox(janela, from_=1, to=20)
spinbox_reps.pack(side=tk.LEFT, padx=5)

# Botão de salvar
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_dados)
botao_salvar.pack(pady=10)

janela.mainloop()
