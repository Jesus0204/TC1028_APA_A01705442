"""
Proyecto APA python
El programa le pide informacion al usuario
y arroja al final la referencia y cita como texto
para que el usuario la pueda usar
"""

"""Funcion auxiliares como inputs o de minúsculas a mayúsculas"""

# Usa la libreria de random para crear el ejemplo
import random

def mayuscula(palabra):
    """
    (Operadores, condicionales, funciones, ciclos, y cadenas)
    Recibe: una palabra
    Funcion que convierte una palabra con la primera letra minuscula como mayuscula usando ASCII
    Devuelve: La palabra mayuscula
    """
    # Use esta pagina web para saber como convertir de ASCII a texto y vice versa 
    # https://www.programiz.com/python-programming/examples/ascii-character 

    # Si el usuario escribio el apellido con minuscula, esto sirve para convertirlo a mayuscula
    palabra_ma = ord(palabra[0])
    if palabra_ma >= 97 and palabra_ma <= 122:
        palabra_ma -= 32
    palabra_ma = chr(palabra_ma) 

    # Despues de convertir a mayuscula la primera letra, juntar las otras letras del apellido en una variable
    for letra in range(1, len(palabra)):
        palabra_ma += palabra[letra]

    return palabra_ma

def decision_si_o_no():
    """
    (ciclos, condicionales, funciones)
    Recibe: nada
    Funcion que asegura el input de una decisión del usuario con 0 o 1
    Devuelve: un integer de 0 o 1.
    """
    # Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    while True:
        try:
            decision = int(input("Escribe tu opcion: "))
        except ValueError:
            print("\nPor favor escribe un número :)")
            continue
        if decision <= -1 or decision >= 2:
            print("\nPor favor escribe 0 o 1.\n")
            continue
        else:
            break
    
    return decision

def inputs():
    """
    (ciclos, ciclos anidades, condicionales, operadores, funciones, listas, listas anidadas)
    Recibe: nada
    Funcion que toma inputs. Estos datos los tiene todo tipo de fuente. 
    Devuelve: los componentes de la fecha, matriz de autor, titulo y link
    """
    # Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    # Aqui obligo al usuario a escribir un numero para la fecha y a escribir algo en el titulo y link
    d_365_input = ""
    mes_input = ""
    dia_input = ""
    titulo_input = ""
    while True:
        try:
            if d_365_input == "":
                d_365_input = int(input("\nEscribe el year de tu fuente. Si no tiene escribe 0.\n"))
            if mes_input == "":
                mes_input = int(input("\nEscribe el mes en forma numerica. Por ejemplo Enero es 1. Si no tiene escribe 0.\n"))
            if dia_input == "":
                dia_input = int(input("\nEscribe el dia de tu fuente. Si no tiene escribe 0.\n"))
        except ValueError:
            print("Por favor escribe un numero :)")
            continue
        # Si el usuario no escribio nada pasa esta condición
        if titulo_input == "":
            titulo_input = input("\nEscribe el titulo del artículo, trabajo u obra que estas citando.\n")
            # Este if solo es para imprimirle al usuario que no tiene que dejar vacio lo que escribe.
            if titulo_input == "":
                print("Favor de no dejar vacio.")
            # Poner el continue para volver a empezar el ciclo. 
            # Si el usuario escribio algo no pasa la condicion de arriba; de otra forma pide el titulo de nuevo.
            continue
        link_input = input("\nPor favor escribe el link o DOI de tu fuente. Si no tiene (en el caso de libros) escribe 0.\n")
        if link_input == "":
            print("Favor de no dejar vacio.")
            continue
        else:
            break

    # Iniciar la variable para que entre el ciclo, y las listas vacias
    multiples_autores = 1
    autor_lista = []
    # No permitir ciertos comportamientos del usuario con el counter
    counter = 0

    while multiples_autores == 1:
        nombre_y_apellido = []
        print("\nPor favor escribe los autores correspondientes. \
            \nSolo se puede agregar mas de un autor cuando se tiene nombre y apellido.")
        lista_nombre_input = input("\nEscribe el primer nombre del autor. Si no tiene escribe 0.\n")
        lista_apellido_input = input("\nEscribe el apellido del autor. Si no tiene escribe 0.\n")
        # Solo aceptar estos casos en el primer autor. No tiene sentido que pongan un 0 si hay mas de un autor.
        if counter == 0:
        # Aceptar ambos 0 solo si es el primer autor
            if lista_nombre_input == "0" and lista_apellido_input == "0":
                nombre_y_apellido.append(lista_nombre_input)
                nombre_y_apellido.append(lista_apellido_input)
                autor_lista.append(nombre_y_apellido)
                multiples_autores = 0
                continue
        # Como no puede haber citas son solo nombre de autor y sin apellido, solo aceptar el nombre con 0.
            elif lista_nombre_input == "0" and lista_apellido_input.isalpha():
                nombre_y_apellido.append(lista_nombre_input)
                nombre_y_apellido.append(lista_apellido_input)
                autor_lista.append(nombre_y_apellido)
                multiples_autores = 0
                continue
        elif counter >= 1:
            if lista_nombre_input == "0" or lista_apellido_input == "0":
                print("\n\nEscribiste que hay mas de un autor. En este caso ya no se puede escribir 0. Favor de intentar de nuevo.\n")
                continue
        # Empezar de nuevos los ifs, ya que siempre se tiene que revisar esta condicion
        # No aceptar numeros aparte de 0 
        if (lista_nombre_input.isalpha() == False) or (lista_apellido_input.isalpha() == False):
            print("\nFavor de no dejar vacio y de no escribir un numero que no sea 0. También no se pueden escribir espacios.")
            print("Si escribiste un nombre para el autor, pero 0 en el apellido, no es un autor valido. Favor de intentar de nuevo.")
            continue
        else: 
            nombre_y_apellido.append(lista_nombre_input)
            nombre_y_apellido.append(lista_apellido_input)
            autor_lista.append(nombre_y_apellido)
        counter += 1
        print("\n¿Tu referencia tiene un autor más? \
                \nEscribe 0 por si ya fue el ultimo autor, y 1 para para agregar a otro autor.\n")
        multiples_autores = decision_si_o_no()
    
    return (d_365_input, mes_input, dia_input, autor_lista, titulo_input, link_input)

'''Funciones que procesan datos como fechas o autores'''

def fecha(d_365, mes, dia):
    """
    (listas, ciclos, condicionales, operadores, funciones)
    Recibe: componentes de la fecha
    Funcion que te formatea la fecha en APA.
    Regresa: La fecha con su formato en APA
    """
    # Crear una lista con todos los meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    d_365_apa= str(d_365)
    mes_apa = ""
    # Usar un for loop y el indice de la lista de arriba para definir el mes
    for nombre_mes in meses: 
        if (meses.index(nombre_mes) + 1) == mes: 
            mes_apa = nombre_mes
            break
    dia_apa = str(dia)

    if d_365 == 0 and mes == 0 and dia == 0:
        fecha_apa = "(s.f.)."
    elif mes > 12 or dia > 31:
        fecha_apa = "(Fecha no valida)."
    elif mes == 0 and dia == 0:
        fecha_apa = ("(" + d_365_apa + ").")
    elif dia == 0:
        fecha_apa = ("(" + mes_apa + ", " + d_365_apa + ").")
    elif d_365 != 0 and mes != 0 and dia != 0:
        fecha_apa = ("(" + mes_apa + " " + dia_apa + ", " + d_365_apa + ").")
    else:
        fecha_apa = "(Fecha no valida)."

    return fecha_apa

def fecha_cita(d_365):
    """
    (condicionales, funciones)
    Recibe: El componente de la fecha que tiene 365 dias
    Funcion que deja lista la fecha de las citas. Como solo hay dos opciones, es una función corta
    Devuelve: El formato de la fecha para usar en citas.
    """
    if d_365 == 0:
        fecha = "s.f."
    else:
        fecha = d_365

    return fecha

def autor(autor_lista):
    """
    (listas, listas anidadas, funciones, condicionales, operadores, cadenas, ciclos, ciclos anidados)
    Recibe: Lista de autores
    Funcion que te formatea el autor en APA.
    Devuelve: El autor con su formato
    """
    # Esto es sirve para cuando digan que no hay autor o solo esta el apellido del autor, 
    # ya que ahi no hay necesidad de agregar mas autores
    nombre = autor_lista[0][0]
    apellido = autor_lista[0][1]
    apellido_apa = mayuscula(apellido)

    # Preparar la variable por si no hay autor. Esto se da mas en páginas web.
    if nombre == "0" and apellido == "0":
        autor_apa = "0"
    # Para casos donde solo este el apellido. Esto no pasa con varios autores, por lo que igual solo se usa el primero en la lista
    elif nombre == "0":
        autor_apa = (apellido_apa + ".")
    else:
        autor_apa = ""
        # Lista con listas
        for autor in range(len(autor_lista)):
            # Si tiene mas de 20 autores, este es el formato. No importan los demas autores por lo que se rompe.
            if autor >= 19:
                autor_apa += "... " + mayuscula(autor_lista[-1][1]) + ", " + mayuscula(autor_lista[-1][0][0]) + "."
                break
            numero_autor = ""
            # Lista individual con nombre y apellido. Contar para abajo para poner el apellido primero, y despues el nombre
            for indice_n_y_a in range(1,-1,-1):
                nombre_o_apellido = mayuscula(autor_lista[autor][indice_n_y_a])
                # Siempre que es un apellido lleva coma.
                if indice_n_y_a == 1:
                    numero_autor += nombre_o_apellido + ", "
                # Siempre que es nombre lleva un punto al final. 
                elif indice_n_y_a == 0:
                    # Agregar la primera letra solamente
                    numero_autor += nombre_o_apellido[0] + "."
            # El penultimo autor lleva el símbolo de más
            if autor == (len(autor_lista) - 2):
                autor_apa += numero_autor + " & "
            # Como el punto se pone por autor, ya no se agrega nada mas en el ultimo autor.
            elif autor == (len(autor_lista) - 1):
                autor_apa += numero_autor
            # Agregar comas para todos los demas casos. 
            else:
                autor_apa += numero_autor + ", "  

    return autor_apa

def edicion(num_edicion):
    """
    (condicionales, operadores, funciones)
    Recibe: El numero de la edicion
    Funcion que formatea la edicion para libros en APA
    Devuelve: String de la edicion
    """
    edicion_str = str(num_edicion)
    if num_edicion > 0:
        edicion_final = "(" + edicion_str + "a ed.). "
    else: 
        edicion_final = "0"
    
    return edicion_final

def cita(d_365, autor_lista, fuente, organizacion):
    """
    (condicionales, operadores, cadenas, listas, listas anidadas, funciones)
    Recibe: componente de fecha, lista de autores, string de fuente y de organizacion
    Funcion que regresa los diferentes tipos de cita que se insertan en el texto.
    Devuelve: Dos strings con el formato de las diferentes citas en APA
    """
    fecha_apa = fecha_cita(d_365)
    fecha_apa = str(fecha_apa)
    # Solo hay 3 posibles citas, por lo que enumerarlas
    if len(autor_lista) >= 3:
        autor = autor_lista[0][1] + " et al."
    elif len(autor_lista) == 2:
        autor = autor_lista[0][1] + " & " + mayuscula(autor_lista[1][1])
    else:
        autor = autor_lista[0][1]
    # Mandar a que sea mayuscula el primer apellido de autor
    autor_apa = mayuscula(autor)

    if (fuente == 1 or fuente == 4):
        if autor == "0" and organizacion != "0":
            cita_parentesis = "(" + organizacion + ", " + fecha_apa + ")"
            cita_narrativa = organizacion + ", (" + fecha_apa + ")"
        elif autor != "0":
            cita_parentesis = "(" + autor_apa + ", " + fecha_apa + ")"
            cita_narrativa = autor_apa + ", (" + fecha_apa + ")"
        # Como el otro else no entra ahi, poner que pasa en caso de que no haya autor u organizacion.
        else:
            cita_parentesis = "Cita no valida. Tiene que haber autor u organizacion."
            cita_narrativa = "Cita no valida. Tiene que haber autor u organizacion."
    # Estas dos fuentes son iguales, y como no pueden tener organizaciones se juntan
    elif (fuente == 2 or fuente == 3) and autor != "0":
        autor_apa = mayuscula(autor)
        cita_parentesis = "(" + autor_apa + ", " + fecha_apa + ")"
        cita_narrativa = autor_apa + ", (" + fecha_apa + ")"
    else:
        cita_parentesis = "Cita no valida. Tiene que haber autor."
        cita_narrativa = "Cita no valida. Tiene que haber autor."

    # Como hay diferentes formas, le voy a dar al usuario ambos metodos
    return cita_parentesis, cita_narrativa

'''Funciones que juntan la referencia por tipo de fuente'''

def web_o_imagen(fecha, autor, titulo, link, tipo_fuente):
    """
    (ciclos, condicionales, operadores, cadenas, funciones)
    Recibe: fecha con formato, autor con formato, titulo, link y tipo de fuente
    Funcion que usa otras funciones para juntar la referencia de paginas web
    Devuelve: La referencia en APA, y la organizacion; ambos strings
    """
    # Pedir input de la organizacion y del link y obligar que usuario escriba texto
    while True:
        organizacion_input = input("\nPor favor escribe la organizacion. Esto sirve si la pagina no tiene autor,\
        \no para incluir despues en la cita. Si no tiene escribe 0\n")
        if organizacion_input == "":
            print("Favor de no dejar vacio.")
            continue
        else:
            break

    organizacion = mayuscula(organizacion_input)
    titulo = mayuscula(titulo)

    if link == "0" or (autor == "0" and organizacion == "0"):
        web_apa = "Referencia no valida. Tiene que autor u organizacion, aparte de un link."
    elif tipo_fuente == 1:
        # Si hay una organizacion y un autor, ponerla al final de la cita.
        if autor != "0" and organizacion != "0":
            web_apa = autor + " " + fecha + " " + titulo + ". " + organizacion + ". " + link + "."
        # Si no tiene autor hacer la organizacion el autor para que se ponga primero
        elif autor == "0":
            web_apa = organizacion + ". " + fecha + " " + titulo + ". " + link + "."
        # Cita sin organizacion
        elif organizacion == "0":
            web_apa = autor + " " + fecha + " " + titulo + ". " + link + "."
    elif tipo_fuente == 4:
        if autor != "0" and organizacion != "0":
            web_apa = autor + " " + fecha + " " + titulo + ". " + "[Imagen]. " + organizacion + ". " + link + "."
        elif autor == "0":
            web_apa = organizacion + ". " + fecha + " " + titulo + ". " + "[Imagen]. " + link + "."
        elif organizacion == "0":
            web_apa = autor + " " + fecha + " " + titulo + ". " + "[Imagen]. " + link + "."
    
    return web_apa, organizacion

def libro(fecha, autor, titulo, link):
    """
    (ciclos, condicionales, operadores, cadenas, funciones)
    Recibe: fecha con formato, autor con formato, titulo y link
    Funcion que usa otras funciones para juntar la referencia de un libro
    Devuelve: La referencia en APA del libro (string)
    """
    edicion_input = ""
    # Asegurar inputs
    while True:
        # Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
        try:
            if edicion_input == "":
                edicion_input = int(input("\nEscribe el numero de edicion de tu fuente. \
                    \nSi no tiene escribe 0 o un numero menor a 0.\n"))
        except ValueError:
            print("Por favor escribe un numero :)")
            continue
        editorial_input = input("\nPor favor escribe el editorial del libro. Debe de estar en las primeras paginas.\n")
        if editorial_input == "":
            print("Favor de no dejar vacio.")
            continue
        else: 
            break

    edicion_apa = edicion(edicion_input)
    editorial = mayuscula(editorial_input)
    titulo = mayuscula(titulo)

    # Formato de todo libro.
    libro_apa = autor + " " + fecha + " "  + titulo  + ". " 
    
    # Checar que haya edicion
    if edicion_apa != "0":
        libro_apa += edicion_apa
    
    libro_apa += editorial + ". "

    # Checar que haya link
    if link != "0":
        libro_apa += link
    # Checar que tenga autor para que no imprima 0
    if autor == "0":
        libro_apa = "Referencia no valida. El libro tiene que tener autor."

    return libro_apa

def video(fecha, autor, titulo, link):
    """
    (condicionales, operadores, cadenas, funciones)
    Recibe: fecha con formato, autor, titulo y link.
    Funcion que usa otras funciones para juntar la referencia de un video
    Devuelve: Referencia en APA del video (string)
    """
    titulo = mayuscula(titulo)

    video_apa = autor + " " + fecha + " " + titulo + ". [Video]. " + link + "."

    if autor == "0" or link == "0":
        video_apa = "Referencia no valida. El video tiene que tener autor y un link."

    return video_apa

"""Funcion de ejemplo de la referencia y cita"""

def ejemplo():
    """
    (funciones, API random, listas)
    Recibe: nada
    Funcion que usando listas y random elige los elementos de una referencia.
    Posteriormente se usan las funciones para darle formato y simplemente se regresa
    Devuelve: El APA del un ejemplo usando random (string)
    """
    # Datos de entrada a escoger
    titulos = ["Quesadillas", "La teoria cuantica", "I have the high ground", 
            "Como usar random en Python", "¿Que hago en mi vida?", "¡Examen argumentativo!"]
    links = ["https://quesadillas.com", "https://cuanticaenmivida.com","https://ihavethehighground.com", 
            "https://randompython.com", "https://tipsdelavida.com", "https://examen.com"]
    autores = [["Jesus", "Cedillo"], ["Benjamin", "Valdes"], ["Rodrigo", "Perez"],
            ["Rebeca", "Blanco"], ["Julieta", "Galvan"], ["Erika", "Castañeda"]]
    
    # Escoger con random los elementos. Puede que los titulos no coincidan con los links; Esto fue hecho adrede
    d_365 = random.randrange(1800,2025,1)
    mes = random.randrange(1,12,1)
    dia = random.randrange(1,28,1)
    titulo = random.choice(titulos)
    link = random.choice(links)

    # Para que la funcion de autor funcione, conservar la matriz aunque solo tenga una lista
    autor_l = []
    autor_l.append(random.choice(autores))

    # Darle formato a estos dos elementos antes de juntar el APA
    fecha_ejemplo = fecha(d_365, mes, dia)
    autor_ejemplo = autor(autor_l)

    # Juntar todo con los datos
    apa_ejemplo = video(fecha_ejemplo,autor_ejemplo,titulo,link)

    return apa_ejemplo

"""Parte principal del programa"""

print("\n¡¡Bienvenido a Citatec!! Aqui podrás citar tus fuentes en formato APA\n")

ejemplo_v = ejemplo()
print("Aqui hay un ejemplo de como se va a ver tu referencia despues de usar el citador:\n\n" + ejemplo_v)

print("\nPor favor escribe con un numero el tipo de fuente que quieres citar. \n \
\nUn 1 para pagina web.\nUn 2 para libro con un autor. \nUn 3 para video. \nUn 4 para una imagen.")

# Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
# Aqui obligo al usuario a escribir un numero para elegir el tipo de fuente
while True:
    try:
        tipo_de_fuente = int(input("\nElige el tipo de fuente que quieres citar: "))
    except ValueError:
        print("\nPor favor escribe un numero :)")
        continue
    if tipo_de_fuente > 4 or tipo_de_fuente <= 0:
        print("\nLos numeros negativos, el 0 y cualquiera mayor de 4 no es valido. Favor de escribir otra.")
        continue
    else:
        break

# Datos de todo tipo de fuente
d_365_usuario, mes_usuario, dia_usuario, autor_usuario, titulo_usuario, link_usuario = inputs()

fecha_final = fecha(d_365_usuario, mes_usuario, dia_usuario)
autor_final = autor(autor_usuario)

if tipo_de_fuente == 1:
    apa_final, organizacion_cita = web_o_imagen(fecha_final, autor_final, titulo_usuario, link_usuario, tipo_de_fuente)
elif tipo_de_fuente == 2:
    apa_final = libro(fecha_final, autor_final, titulo_usuario, link_usuario)
    # Para que no declare error el programa al pasar el parametro
    organizacion_cita = 0
elif tipo_de_fuente == 3:
    apa_final = video(fecha_final, autor_final, titulo_usuario, link_usuario)
    organizacion_cita = 0
elif tipo_de_fuente == 4:
    apa_final, organizacion_cita = web_o_imagen(fecha_final, autor_final, titulo_usuario, link_usuario, tipo_de_fuente)

# APA final. Funcion con web y video ya estan listos.
print("\nTu APA final se veria asi:", apa_final)

print("\nTe gustaria generar la cita? Esta es la que se pone directamente en el texto. \
        \nEscribe 0 para no, y 1 para si.\n")
cita_decision = decision_si_o_no()

if cita_decision == 1:
    # Llamar la funcion para todo tipo de fuente
    cita_parentesis_final, cita_narrativa_final = cita(d_365_usuario, autor_usuario, tipo_de_fuente, organizacion_cita)
    print("\nHay dos formas de cita. La narrativa, que se pone directamente en el texto. \
        Un ejemplo de esta es 'de acuerdo a Botello (2005)'.")
    print("La otra forma es la de parentesis, donde se copia y pega la informacion y directamente \
        acabando el parentesis se pone. Un ejemplo es (Botello, 2005).")
    print("\nCita narrativa:", cita_narrativa_final)
    print("Cita de parentesis:", cita_parentesis_final)

print("\n¡Gracias por usar el programa!")
