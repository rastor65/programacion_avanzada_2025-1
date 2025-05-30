
import re
import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        return f"Nodo({self.valor})"

class NodoArbol:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

# Función para mostrar el resultado en una ventana
def mostrar_resultados(resultado, mostrar_ventana=True):
    ventana_resultados = tk.Tk()
    ventana_resultados.title("Resultados del Analizador")
    ventana_resultados.geometry("700x500")

    area_texto = scrolledtext.ScrolledText(ventana_resultados, wrap=tk.WORD, width=80, height=20)
    area_texto.pack(padx=10, pady=10)
    area_texto.insert(tk.END, resultado)
    area_texto.configure(state='disabled')
    ventana_resultados.mainloop()

# Función del analizador léxico
def analizador_lexico(codigo):
    resultado = "Analizador Léxico\n\n"
    operadores = {
        '+': 'suma (aritmetico)','-': 'resta (aritmetico)', '*': 'multiplicación (aritmetico)','/': 'división (aritmetico)','%': 'módulo (aritmetico)',
    '**': 'potencia (aritmetico)', '//': 'división entera (aritmetico)',  '==': 'igual a (relacional)', '!=': 'diferente de (relacional)', '<': 'menor que (relacional)',
    '>': 'mayor que (relacional)','<=': 'menor o igual que (relacional)','>=': 'mayor o igual que (relacional)','&&': 'y lógico (AND)','||': 'o lógico (OR)',
    '!': 'negación lógica (NOT)', '=': 'igual (asignación)', '&': 'y bit a bit','|': 'o bit a bit','^': 'o exclusivo (XOR) (bit a bit)','~': 'negación bit a bit','<<': 'desplazamiento a la izquierda (bit a bit)',
    '>>': 'desplazamiento a la derecha (bit a bit)'
    }
    tipo_de_dato = {
        'int': 'entero', 'float': 'punto flotante', 'double': 'doble precisión', 'char': 'carácter',
    'bool': 'booleano (lógico)', 'string': 'cadena de caracteres', 'long': 'entero largo',
    'short': 'entero corto', 'byte': 'byte', 'void': 'vacío', 'array': 'arreglo (matriz)',
    'struct': 'estructura', 'union': 'unión', 'enum': 'enumeración', 'pointer': 'puntero'
    }
    puntuaciones = {
        ':': 'delimitador dos puntos', ';': 'delimitador punto y coma', '.': 'delimitador punto', ',': 'delimitador coma', '?': 'signo de interrogación',
    '!': 'signo de exclamación', '-': 'guion', '_': 'guion bajo', '(': 'delimitador paréntesis izquierdo',
    ')': 'delimitador paréntesis derecho', '[': 'delimitador corchete izquierdo', ']': 'delimitador corchete derecho', '{': 'delimitador llave izquierda',
    '}': 'delimitador llave derecha', '«': 'comillas angulares izquierda', '»': 'comillas angulares derecha',
    '"': 'comillas dobles', "'": 'comilla simple', '/': 'barra inclinada', '\\': 'barra invertida',
    '*': 'asterisco', '#': 'almohadilla', '@': 'arroba'
    }
    palabras_clave = {
        'if': 'palabra clave', 'else': 'palabra clave', 'for': 'palabra clave', 'while': 'palabra clave',
    'print': 'palabra clave', 'return': 'palabra clave', 'def': 'palabra clave', 'class': 'palabra clave',
    'import': 'palabra clave', 'from': 'palabra clave'
    }

    regex_cadenas = re.compile(r'"[^"]*"|\'[^\']*\'')
    regex_comentarios = re.compile(r'#.*')
    regex_tokens = re.compile(r'\b\w+\b|[^\w\s]')
    regex_identificadores = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
    regex_numeros = re.compile(r'\b\d+(\.\d+)?\b')  

    contador = 0
    program = codigo.split("\n")

    for line in program:
        contador += 1
        if not line.strip():
            resultado += "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
            resultado += f"Línea #{contador}: Está vacía\n"
            continue

        resultado += "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        resultado += f"Línea #{contador}:\n{line}\n"

        comentario = regex_comentarios.search(line)
        if comentario:
            resultado += f"Comentario encontrado: {comentario.group()}\n"
            line = regex_comentarios.sub('', line)

        cadenas = regex_cadenas.findall(line)
        for cadena in cadenas:
            resultado += f"Cadena de texto encontrada: {cadena}\n"
        
        line = regex_cadenas.sub('', line)

        tokens = regex_tokens.findall(line)
        tokens = [token for token in tokens if token.strip()]
        resultado += "Tokens: " + ", ".join(tokens) + "\n"

        for token in tokens:
            reconocido = False
            if token in palabras_clave:
                resultado += f"'{token}' es una {palabras_clave[token]}\n"
                reconocido = True
            elif token in operadores:
                resultado += f"Operador {token}: {operadores[token]}\n"
                reconocido = True
            elif token in tipo_de_dato:
                resultado += f"Tipo de dato: {tipo_de_dato[token]}\n"
                reconocido = True
            elif token in puntuaciones:
                resultado += f"'{token}' es un {puntuaciones[token]}\n"
                reconocido = True
            elif regex_identificadores.fullmatch(token):
                resultado += f"{token} es un identificador\n"
                reconocido = True
            elif regex_numeros.fullmatch(token):
                resultado += f"{token} es un número\n"
                reconocido = True
            if not reconocido:
                resultado += f"{token} no se reconoce\n"

    mostrar_resultados(resultado)

# Dibujar el árbol sintáctico gráfico
def dibujar_arbol_grafico(nodo, posiciones=None, nivel=0, x=0.5, dx=0.25, ax=None):
    if posiciones is None:
        posiciones = {}
        
    posiciones[nodo] = (x, 1 - nivel * 0.1)

    hijos_invertidos = nodo.hijos[::1]

    for i, hijo in enumerate(hijos_invertidos):
        x_hijo = x - dx / 2 + i * dx
        dibujar_arbol_grafico(hijo, posiciones, nivel + 1, x_hijo, dx / 2, ax)
        ax.plot([posiciones[nodo][0], posiciones[hijo][0]], [posiciones[nodo][1], posiciones[hijo][1]], color="black", lw=2)

    ax.text(posiciones[nodo][0], posiciones[nodo][1], str(nodo.valor), fontsize=16, ha='center', va='center', bbox=dict(boxstyle="circle", facecolor="white", edgecolor="black"))

def crear_arbol_grafico(raiz):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.axis('off')
    dibujar_arbol_grafico(raiz, ax=ax)
    plt.show()

# Función mostrar_arbol para la representación textual del árbol
def mostrar_arbol(nodo, nivel=0):
    if nodo is None:
        return ""
    resultado = "  " * nivel + f"{nodo.valor}\n"
    for hijo in nodo.hijos:
        resultado += mostrar_arbol(hijo, nivel + 1)
    return resultado

# Analizador Sintáctico que maneja expresiones de asignación
def construir_arbol(tokens):
    def parse_asignacion():
        izquierda = parse_expresion()
        if tokens and tokens[0] == '=':
            tokens.pop(0)
            derecha = parse_expresion()
            return NodoArbol('=', [izquierda, derecha])
        return izquierda

    def parse_expresion():
        if tokens and tokens[0] == 'print':
            return parse_print()
        if tokens and tokens[0] == 'if':
            return parse_if()
        
        izquierda = parse_termino()
        while tokens and tokens[0] in ('+', '-'):
            operador = tokens.pop(0)
            derecha = parse_termino()
            izquierda = NodoArbol(operador, [izquierda, derecha])
        return izquierda

    def parse_if():
    
        tokens.pop(0)  
        condicion = parse_expresion()  # Parsear la condición del 'if'
        
        # Asegurarse de que la condición esté seguida de ':'
        if not tokens or tokens[0] != ':':
            raise SyntaxError("Se esperaba ':' después de la condición del if.")
        
        tokens.pop(0)  # Consumir ':'

        # Parsear las instrucciones dentro del bloque 'if'
        instrucciones_if = []
        while tokens and tokens[0] != 'else' and tokens[0] != 'EOF':
            instruccion = parse_instruccion()  # Cambiar a parse_instruccion()
            instrucciones_if.append(instruccion)

        # Verificar si hay un 'else'
        instrucciones_else = []
        if tokens and tokens[0] == 'else':
            tokens.pop(0)  # Consumir 'else'
            
            # Asegurarse de que 'else' esté seguido de ':'
            if not tokens or tokens[0] != ':':
                raise SyntaxError("Se esperaba ':' después de 'else'.")
            
            tokens.pop(0)  # Consumir ':'

            # Parsear las instrucciones dentro del bloque 'else'
            while tokens and tokens[0] != 'EOF':
                instruccion = parse_instruccion()  # Cambiar a parse_instruccion()
                instrucciones_else.append(instruccion)

        # Devolver un nodo 'if' con su condición y las instrucciones de los bloques
        return NodoArbol('if', [condicion] + instrucciones_if + [NodoArbol('else', instrucciones_else)])




    def parse_instruccion():
        if tokens and tokens[0] == 'print':
            return parse_print()
        return parse_expresion()  # Puedes agregar más casos aquí si necesitas manejar más instrucciones

    def parse_termino():
        izquierda = parse_factor()
        while tokens and tokens[0] in ('*', '/','<','>'):
            operador = tokens.pop(0)
            derecha = parse_factor()
            izquierda = NodoArbol(operador, [izquierda, derecha])
        return izquierda

    def parse_factor():
        if not tokens:
            return None
        token = tokens.pop(0)

        if token.isdigit():
            return NodoArbol(token)
        elif token.startswith('"') or token.startswith("'"):  # Manejar cadenas
            return NodoArbol(token)
        elif token == '(':
            subexpresion = parse_expresion()
            if tokens and tokens[0] == ')':
                tokens.pop(0)  # Consumir ')'
            return subexpresion
        elif token == 'print':  # Manejar funciones como print
            return parse_print()
        return NodoArbol(token)  # Manejar identificadores

    def parse_print():
        if tokens and tokens[0] == 'print':
            tokens.pop(0)  # Consumir 'print'
            if tokens and tokens[0] == '(':
                tokens.pop(0)  # Consumir '('
                argumento = parse_expresion()  # Parsear el argumento dentro del print
                if tokens and tokens[0] == ')':
                    tokens.pop(0)  # Consumir ')'
                    return NodoArbol('print', [argumento])
                else:
                    raise SyntaxError("Se esperaba ')' al final de la instrucción print.")
            else:
                raise SyntaxError("Se esperaba '(' después de 'print'")

    return parse_asignacion()





def analizador_sintactico(codigo):
    resultado = "Analizador Sintáctico\n\n"

    # Expresiones regulares para identificar los diferentes tokens
    regex_cadenas = re.compile(r'"[^"]*"|\'[^\']*\'')
    regex_comentarios = re.compile(r'#.*')
    regex_tokens = re.compile(r'\b\w+\b|[^\w\s]')
    regex_identificadores = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
    regex_numeros = re.compile(r'\b\d+(\.\d+)?\b')

    # Combina todas las expresiones regulares en una sola para capturar todos los tokens relevantes
    regex_total = re.compile(r'({})|({})|({})|({})|({})'.format(
        regex_cadenas.pattern,
        regex_comentarios.pattern,
        regex_tokens.pattern,
        regex_identificadores.pattern,
        regex_numeros.pattern
    ))

    # Encuentra todos los tokens usando la expresión regular total
    tokens = [token for token in regex_total.findall(codigo) if any(token)]

    # Aplana la lista de tuplas de tokens generados
    tokens = [item for sublist in tokens for item in sublist if item]

    tokens = [token for token in tokens if not regex_comentarios.match(token)]

    print("Tokens generados:", tokens)  # Muestra los tokens antes de procesarlos

    # Asegúrate de que los tokens no estén vacíos
    if not tokens:
        resultado += "No se generaron tokens.\n"
        mostrar_resultados(resultado)
        return

    try:
        arbol = construir_arbol(tokens)
    except SyntaxError as e:
        resultado += f"Error de sintaxis: {str(e)}\n"
        mostrar_resultados(resultado)
        return
    except Exception as e:
        resultado += f"Error inesperado: {str(e)}\n"
        mostrar_resultados(resultado)
        return

    if arbol:
        resultado += "Árbol sintáctico construido exitosamente:\n"
        crear_arbol_grafico(arbol)
        resultado += mostrar_arbol(arbol)
    else:
        resultado += "No se pudo construir el árbol sintáctico."

    mostrar_resultados(resultado)



# Analizador Semántico (ejemplo)
def analizador_semantico(codigo):
    resultado = "Analizador Semántico (pendiente de implementación)\n\n"
    mostrar_resultados(resultado)

# Función para manejar la selección de la opción de análisis
def ejecutar_analizador(opcion, entrada_codigo):
    codigo = entrada_codigo.get("1.0", tk.END)
    if opcion == "Léxico":
        analizador_lexico(codigo)
    elif opcion == "Sintáctico":
        analizador_sintactico(codigo)
    elif opcion == "Semántico":
        analizador_semantico(codigo)
    else:
        messagebox.showerror("Error", "Opción inválida.")

# Interfaz gráfica principal
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Analizador Léxico, Sintáctico y Semántico")
    ventana.geometry("600x400")

    etiqueta = tk.Label(ventana, text="Escribe tu código:")
    etiqueta.pack()

    entrada_codigo = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=10)
    entrada_codigo.pack(padx=10, pady=10)

    def ejecutar_seleccion():
        opcion = seleccion.get()
        ejecutar_analizador(opcion, entrada_codigo)

    seleccion = tk.StringVar(value="Léxico")

    opciones = [("Léxico", "Léxico"), ("Sintáctico", "Sintáctico"), ("Semántico", "Semántico")]
    for texto, valor in opciones:
        tk.Radiobutton(ventana, text=texto, variable=seleccion, value=valor).pack(anchor=tk.W)

    boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_seleccion)
    boton_ejecutar.pack(pady=10)

    ventana.mainloop()

crear_interfaz()
