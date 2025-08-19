import tkinter as tk
from tkinter import ttk


valor_das_taxas = {
    "USD" : 1.00,
    "BRL" : 5.44,
    "EUR" : 0.92, 
    }

lista_de_moedas_existentes =[
    "BRL -> Real",
    "USD -> Dólar",
    "EUR-> Euro",
]
    

def converter_moeda(valor_de_entrada, valor_de_destino, quantia):
    #transformar em dolar para ficar mais fácil para outras conversões
    valor_dolar= quantia / valor_de_entrada
    valor_moeda_convertida = valor_dolar * valor_de_destino
    return valor_moeda_convertida   


def fazer_a_conversao():
    quantia_moeda= float(Entrada_quantia_moeda.get())

    tipo_1= tipo_conversao_1.get()
    tipo_2= tipo_conversao_2.get()

    tipo_1_1 = valor_das_taxas[tipo_1]
    tipo_2_1 = valor_das_taxas[tipo_2]

    resultado = converter_moeda(tipo_1_1, tipo_2_1, quantia_moeda)
    label_resultado_final.config(text=f"{resultado:.2f} {tipo_2}")



janela=tk.Tk()
janela.title("Conversor de moeda com o tkinter")
janela.geometry("500x300")

label_instrucao_usuario_1 = tk.Label(janela, text="Escolha a moeda que entrada que será convertida: ")
label_instrucao_usuario_1.pack(pady=5)

tipo_conversao_1 = ttk.Combobox(janela,
    values= ["BRL", "USD", "EUR"]
)
tipo_conversao_1.pack(pady=5)
tipo_conversao_1.current(0)

label_instrucao_usuario_1 = tk.Label(janela, text="Escolha a moeda de destino: ")
label_instrucao_usuario_1.pack(pady=5)

tipo_conversao_2 = ttk.Combobox(janela,
    values= ["BRL", "USD", "EUR"]
)
tipo_conversao_2.pack(pady=5)
tipo_conversao_2.current(0)

label_instrucao_usuario_3 = tk.Label(janela, text="Por favor, digite a quantidade a ser convertida")
label_instrucao_usuario_3.pack(pady=5)

Entrada_quantia_moeda=tk.Entry(janela)
Entrada_quantia_moeda.pack(pady=5)

botao_de_converter=tk.Button(janela, text="Converter moeda", command=fazer_a_conversao)
botao_de_converter.pack(pady=10)

label_resultado_final=tk.Label(janela, text='')
label_resultado_final.pack(pady=5)

janela.mainloop()