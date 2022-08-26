"""
Proyecto APA python
El programa le pide información al usuario
y arroja al final la referencia y cita como texto
para que el usuario la pueda usar
"""

'''Función que toma datos del usuario'''

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
    
    nombre_input = input("\nEscribe el primer nombre del autor. Si no tiene escribe 0.\n")
    apellido_input = input("\nEscribe el apellido del autor. Si no tiene escribe 0.\n")
    titulo_input = input("\nEscribe el titulo del artículo, trabajo u obra que estas citando.\n")

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
        fecha_apa = "(Fecha no válida)"
    elif mes == 0 and dia == 0:
        fecha_apa = ("(" + año_apa + ")")
    elif dia == 0:
        fecha_apa = ("(" + mes_apa + ", " + año_apa + ")")
    elif año != 0 and mes != 0 and dia != 0:
        fecha_apa = ("(" + mes_apa + " " + dia_apa + ", " + año_apa + ")")
    else:
        fecha_apa = "(Fecha no válida)"
    return fecha_apa


'''Funciones que juntan la referencia por tipo de fuente'''

def web():
    '''
    Función que usa otras funciones para juntar la referencia de páginas web
    '''
    # Ver si puedo crear una función para dar a cada dato una variable. Investigar
    año_usuario, mes_usuario, dia_usuario, nombre_usuario, apellido_usuario, titulo_usuario = inputs()
    
    fecha_final = fecha(año_usuario, mes_usuario, dia_usuario)

    # Esto es mientras se va incorporando las otras funciones
    print("\nTu fecha en APA se vería así:", fecha_final)

def libro():
    '''
    Función que usa otras funciones para juntar la referencia de un libro
    '''
    datos = inputs()
    año_usuario, mes_usuario, dia_usuario, nombre_usuario, apellido_usuario, titulo_usuario = datos

def video():
    '''
    Función que usa otras funciones para juntar la referencia de un video
    '''
    datos = inputs()
    año_usuario, mes_usuario, dia_usuario, nombre_usuario, apellido_usuario, titulo_usuario = datos


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
        print("Por favor escribe un número :)")
        continue
    else:
        break

if tipo_de_fuente == 1:
    web()
elif tipo_de_fuente == 2:
    libro()
elif tipo_de_fuente == 3:
    video()