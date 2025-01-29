import re

def analizar_lexico(entradas):
    # Definir las expresiones regulares para los tokens
    patron_int = r'^\d+$'  # Numeros enteros (ejemplo: 90)
    patron_float = r'^\d+\.\d+$'  # Numeros reales (ejemplo: 80.5)
    patron_string = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  # Strings validos (ejemplo: Hola, Hola29, Hola_Mundo)
    
    # Clasificar cada entrada
    tokens = []
    for entrada in entradas:
        if re.match(patron_int, entrada):
            tokens.append((entrada, 'int'))
        elif re.match(patron_float, entrada):
            tokens.append((entrada, 'float'))
        elif re.match(patron_string, entrada):
            tokens.append((entrada, 'string'))
        else:
            tokens.append((entrada, 'error'))
    
    return tokens


# Ejemplo de entradas
entradas = [
    "90",       # int
    "80.5",     # float
    "Hola",     # string
    "Hola29",   # string
    "Hola_Mundo", # string
    "80.",      # error
    ".5",       # error
    "hola",     # string
    "_hola"     # string
]

# Ejecutar el analizador léxico
tokens = analizar_lexico(entradas)

# Imprimir los tokens encontrados
for entrada, tipo in tokens:
    print(f'Entrada: {entrada}, Tipo: {tipo}')