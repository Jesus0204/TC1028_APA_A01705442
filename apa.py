"""
Proyecto APA python
El programa le pide información al usuario
y arroja al final la referencia y cita como texto
para que el usuario la pueda usar
"""

'''Función auxiliares como inputs o de minúsculas a mayúsculas'''

def mayuscula(palabra):
    '''
    Función que devuelve una palabra con la primera letra minúscula como mayúscula usando ASCII
    '''
    # Use esta página web para saber cómo convertir de ASCII a texto y vice versa 
    # https://www.programiz.com/python-programming/examples/ascii-character 

    # Si el usuario escrbió el apellido con minúscula, esto sirve para convertirlo a mayúscula
    palabra_ma = ord(palabra[0])
    if palabra_ma >= 97 and palabra_ma <= 122:
        palabra_ma -= 32
    palabra_ma = chr(palabra_ma) 

    # Después de convertir a mayúscula la primera letra, juntar las otras letras del apellido en una variable
    for letra in range(1, len(palabra)):
        palabra_ma += palabra[letra]

    return palabra_ma

def inputs():
    '''
    Función que toma inputs. Estos datos los tiene todo tipo de fuente. 
    '''
    # Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
    # Aquí obligo al usuario a escribir un número para la fecha
    while True:
        try:
            año_input = int(input("\nEscribe el año de tu fuente. Si no tiene escribe 0.\n"))
            mes_input = int(input("\nEscribe el mes en forma numérica. Por ejemplo Enero es 1. Si no tiene escribe 0.\n"))
            dia_input = int(input("\nEscribe el dia de tu fuente. Si no tiene escribe 0.\n"))
        except ValueError:
            print("Por favor escribe un número :)")
            continue
        else:
            break
    
    # Aquí pasa lo contrario, donde aseguro que el texto sea un string
    while True:

        nombre_input = input("\nEscribe el primer nombre del autor. Si no tiene escribe 0.\n")
        apellido_input = input("\nEscribe el apellido del autor. Si no tiene escribe 0.\n")

        if nombre_input == "0" or apellido_input == "0":
            break
        # Si el input es un número que no sea 0, continuar el ciclo. Basado de la página de abajo
        # https://betterprogramming.pub/how-you-make-sure-input-is-the-type-you-want-it-to-be-in-python-521f3565a66d
        elif nombre_input.isdigit() or apellido_input.isdigit():
            print("\nFavor de no escribir un numero.")
            continue
        elif (nombre_input == "") or (apellido_input == ""):
            print("\nFavor de escribir el nombre u apellido.")
            continue
        # Si no volver a pedir los datos
        else: 
            break
    
    # Obligar que usuario escriba texto
    while True:
        titulo_input = input("\nEscribe el titulo del artículo, trabajo u obra que estas citando.\n")
        if titulo_input == "":
            print("Favor de no dejar vacio.")
            continue
        else:
            break

    return (año_input, mes_input, dia_input, nombre_input, apellido_input, titulo_input)

'''Funciones que procesan datos como fechas o autores'''

# Primero voy a empezar con la fecha, ya que usa operadores

def fecha(año, mes, dia):
    '''
    Función que te regresa la fecha en el formato que se usa en APA.
    Esto sin importar el tipo de fuente.
    '''
    # Crear una lista con todos los meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    año_apa= str(año)
    mes_apa = ""
    # Usar un for loop y el indice de la lista de arriba para definir el mes
    for nombre_mes in meses: 
        if (meses.index(nombre_mes) + 1) == mes: 
            mes_apa = nombre_mes
            break
    dia_apa = str(dia)

    if año == 0 and mes == 0 and dia == 0:
        fecha_apa = "(s.f.)."
    elif mes > 12 or dia > 31:
        fecha_apa = "(Fecha no válida)."
    elif mes == 0 and dia == 0:
        fecha_apa = ("(" + año_apa + ").")
    elif dia == 0:
        fecha_apa = ("(" + mes_apa + ", " + año_apa + ").")
    elif año != 0 and mes != 0 and dia != 0:
        fecha_apa = ("(" + mes_apa + " " + dia_apa + ", " + año_apa + ").")
    else:
        fecha_apa = "(Fecha no válida)."
    return fecha_apa

def autor(nombre, apellido):
    '''
    Función que te regresa el autor en el formato que se usa en APA.
    Esto sin importar el tipo de fuente.
    '''
    # Mandar a convertir la palabra completa a mayúscula
    apellido_apa = mayuscula(apellido)

    # Preparar la variable por si no hay autor. Esto se da más en páginas web.
    if nombre == "0" and apellido == "0":
        autor_apa = "0"
    # Para casos donde solo este el apellido
    elif nombre == "0":
        autor_apa = (apellido_apa + ".")
    else:
        # Aqui no se manda la función porque solo se usa una letra no toda la palabra
        nombre_apa = ord(nombre[0])
        if nombre_apa >= 97 and nombre_apa <= 122:
            nombre_apa -= 32
        nombre_apa = chr(nombre_apa)
        autor_apa = (apellido_apa + ", " + nombre_apa + ".")

    return autor_apa

'''Funciones que juntan la referencia por tipo de fuente'''

def web(fecha, autor, titulo):
    '''
    Función que usa otras funciones para juntar la referencia de páginas web
    '''
    # Pedir input de la organización y del link y obligar que usuario escriba texto
    while True:
        organizacion_input = input("\nPor favor escribe el titulo de la organización. \
        Esto sirve si la página no tiene autor, o para incluir despues en la cita. Si no tiene escribe 0\n")
        link = input("\nPor favor escribe el link de tu fuente.\n")
        if organizacion_input == "" or link == "":
            print("Favor de no dejar vacio.")
            continue
        else:
            break

    organizacion = mayuscula(organizacion_input)
    titulo = mayuscula(titulo)

    # Si hay una organización y un autor, ponerla al final de la cita. Usar otra variable porque ya se cambio la original
    if autor != "0" and organizacion_input != "0":
        web_apa = autor + " " + fecha + " " + titulo + ". " + organizacion + ". " + link + "."
    # De otro modo la cita no es válida
    elif autor == "0" and organizacion_input == "0":
        web_apa = "Cita no válida. Tiene que tener o autor u organización."
    # Si no tiene autor hacer la organizacion el autor para que se ponga primero
    elif autor == "0":
        web_apa = organizacion + ". " + fecha + " " + titulo + ". " + link + "."
    # Cita sin organización
    elif organizacion_input == "0":
        web_apa = autor + " " + fecha + " " + titulo + ". " + link + "."
    
    return web_apa

def libro(fecha, autor, titulo):
    '''
    Función que usa otras funciones para juntar la referencia de un libro
    '''
    titulo = mayuscula(titulo)
    libro_apa = autor + " " + fecha + " " + titulo + ". "

    return libro_apa

def video(fecha, autor, titulo):
    '''
    Función que usa otras funciones para juntar la referencia de un video
    '''
    titulo = mayuscula(titulo)
    # Pedir input del link y obligar que usuario escriba texto
    while True:
        link = input("\nPor favor escribe el link de tu fuente.\n")
        if link == "":
            print("Favor de no dejar vacio.")
            continue
        else:
            break
    video_apa = autor + " " + fecha + " " + titulo + ". [Video]." + link + "."

    return video_apa


'''Parte principal del programa'''

print("\n¡¡Bienvenido a Citatec!! Aquí podrás citar tus fuentes en formato APA\n")
print("\nPor favor escribe con un número el tipo de fuente que quieres citar. \
Un 1 para página web. Un 2 para libro. Un 3 para video. ")
print("\nEste es un programa en desarrollo, por lo que sus funciones saldrán \
semanalmente. También conforme pase el tiempo, habrá más tipo de fuentes. Gracias por su paciencia :) ")

# Este snippet fue basado de https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
# Aquí obligo al usuario a escribir un número para elegir el tipo de fuente
while True:
    try:
        tipo_de_fuente = int(input("\nElige el tipo de fuente que quieres citar\n"))
    except ValueError:
        print("\nPor favor escribe un número :)")
        continue
    if tipo_de_fuente == 0:
        print("\n0 no es una opción válida. Favor de escribir otra.")
        continue
    else:
        break

# Datos de todo tipo de fuente
año_usuario, mes_usuario, dia_usuario, nombre_usuario, apellido_usuario, titulo_usuario = inputs()

fecha_final = fecha(año_usuario, mes_usuario, dia_usuario)
autor_final = autor(nombre_usuario, apellido_usuario)

if tipo_de_fuente == 1:
    apa_final = web(fecha_final, autor_final, titulo_usuario)
elif tipo_de_fuente == 2:
    apa_final = libro(fecha_final, autor_final, titulo_usuario)
elif tipo_de_fuente == 3:
    apa_final = video(fecha_final, autor_final, titulo_usuario)

# APA final. Función con web y video ya estan listos.
print("\nTu APA final se vería así:", apa_final)
