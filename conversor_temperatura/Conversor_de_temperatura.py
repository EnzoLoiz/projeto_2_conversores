lista_tipos_de_conversao_de_temperatura = [
    "[1] — Celsius para Fahrenheit",
    "[2] — Fahrenheit para Celsius",
    "[3] — Celsius para Kelvin",
    "[4] — Kelvin para Celsius",
    "[5] — Fahrenheit para Kelvin",
    "[6] — Kelvin para Fahrenheit",
    "[0] — Sair"
]

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



while True:
    for i in lista_tipos_de_conversao_de_temperatura:
        print(i)

    # A entrada do choice utilizando a validação para ver se será digitado um numero inteiro e não uma letra por exermplo
    while True:    
        try:
            choice = int(input("Escolha um numero correspondente a sua escolha: "))
            break
        except ValueError:
            print("Digitou algo inválido, por favor digite um numero inteiro.")

    if choice == 0:
        print("Saindo...")
        break

    # A entrada da temperatura utlizando a validação para ver se será digitado uma temperatura correta e não uma letra por exemplo
    while True:     
        try:
            temperatura = float(input("Digite a temperatura que quer converter: "))
            break
        except ValueError:
            print("Digitou algo inválido, por favor digite um numero válido para a temperatura desejada.")


    if choice == 1:
        c_f = converter_celsius_fahrenheit(temperatura)
        print(f"A temperatura {temperatura:.2f}°C é igual a {c_f:.2f}°F ")
    elif choice == 2:
        f_c = converter_fahrenheit_celsius(temperatura)
        print(f"A temperatura {temperatura:.2f}°F é igual a {f_c:.2f}°C ")
    elif choice == 3:
        c_k = converter_celsius_kelvin(temperatura)
        print(f"A temperatura {temperatura:.2f}°C é igual a {c_k:.2f}°K ")
    elif choice == 4:
        k_c = converter_kelvin_celsius(temperatura)
        print(f"A temperatura {temperatura:.2f}°K é igual a {k_c:.2f}°C ")
    elif choice == 5:
        f_k = converter_fahrenheit_kelvin(temperatura)
        print(f"A temperatura {temperatura:.2f}°F é igual a {f_k:.2f}°K ") 
    elif choice == 6:
        k_f = converter_kelvin_fahrenheit(temperatura)
        print(f"A temperatura {temperatura:.2f}°K é igual a {k_f:.2f}°F ")
    else:
        print("Opção inválida, escolha uma das opções.")