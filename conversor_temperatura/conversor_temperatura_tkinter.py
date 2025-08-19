import tkinter as tk 
from tkinter  import ttk


    
def converter_celsius_fahrenheit(celsius):
    fahrenheit = celsius*9/5 + 32
    return fahrenheit

def converter_fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit -32 )* 5/9
    return celsius

def converter_celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def converter_kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def converter_fahrenheit_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32)*5/9 + 273.15
    return kelvin

def converter_kelvin_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15)*9/5 + 32
    return fahrenheit


def fazer_a_conversao():
    temperatura = float(entrada_temperatura.get())

    tipo = tipo_conversao.get()

    if tipo == "Celsius -> Fahrenheit":
        resultado = converter_celsius_fahrenheit(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °F")
    elif tipo == "Fahrenheit -> Celsius":
        resultado = converter_fahrenheit_celsius(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °C")
    elif tipo == "Celsius -> kelvin":
        resultado = converter_celsius_kelvin(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °K")
    elif tipo == "Kelvin -> Celsius":
        resultado = converter_kelvin_celsius(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °C")
    elif tipo == "Fahrenheit -> kelvin":
        resultado = converter_fahrenheit_kelvin(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °K")
    elif tipo == "Kelvin -> Fahrenheit":
        resultado = converter_kelvin_fahrenheit(temperatura)
        label_resultado_final.config(text=f"{resultado:.2f} °F")    
    

janela =tk.Tk()
janela.title("Conversor de temperatura com o tkinter")
janela.geometry("300x200")

label_instrucao_usuario = tk.Label(janela, text= "Por favor, digite a temperatura")
label_instrucao_usuario.pack(pady=5)

entrada_temperatura = tk.Entry(janela)
entrada_temperatura.pack(pady=5)

tipo_conversao = ttk.Combobox( janela, 
    values= ["Celsius -> Fahrenheit", "Fahrenheit -> Celsius", "Celsius -> kelvin", "Kelvin -> Celsius", "Fahrenheit -> kelvin", "Kelvin -> Fahrenheit"]                                   
)
tipo_conversao.pack(pady=5)
tipo_conversao.current(0)

botao_de_converter = tk.Button(janela, text="Converter Temperatura", command= fazer_a_conversao)
botao_de_converter.pack(pady=5)

label_resultado_final= tk.Label(janela, text="")
label_resultado_final.pack(pady=5)

janela.mainloop()