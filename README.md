# Citatec

## TC1028 - Jesús Alejandro Cedillo Zertuche A01705442

### Contexto
Estar en el Tec de Monterrey muchas veces puede llegar a ser retador por todos los trabajos y actividades que nos dejan. Y muchas de estas actividades tienen algo en común. Esto es el uso del internet. Se usa desde para buscar información en libros, PDFs, páginas web, videos, etc. hasta para simplemente buscar inspiración en algo. Y al hacer esto, se tiene que citar en formato APA todo lo que usaste. 

Me he dado cuenta que mucha gente o no sabe citar en APA, o por todas las versiones diferentes que existen, lo hacen de forma distinta. Es por eso, que voy a crear un programa, que te hace la refrencia del APA y la cita, dependiendo de qué tipo de fuente sea, de acuerdo a la 7º edición; la más nueva y reciente. Me parece muy interesante ya que puedo retar mis capacidades para programar, al mismo tiempo que de cierta forma ayudar a mi universidad. Citar tus fuentes es algo ético que se debe de hacer, y esta es mi forma de ayudar. 

De hecho, el formato APA es uno de los más comunes, y este programa puede ayudar a gente también fuera del Tec de Monterrey. Al final el programa te va a arrojar la referencia y cita de la fuente de tu elección para que puedas copiar y pegarla a tu documento. 

### Pasos del Algoritmo
1. Estado inicial: Pedir al usuario que tipo de fuente le gustaría citar.

Pseudocódigo:

    tipo de fuente = input("Escribe tu tipo de fuente. 1 es para página web, 2 para libro, 3 para vídeo, etc.")

2. Asignar a cada tipo de fuente un número, y usar condiciones para correr las funciones en la parte principal del programa. Cada tipo de fuente va a llamar a una función, que le da forma al APA de ese tipo de fuente en específico. 

Pseudocódigo:

    Si tipo de fuente == 1:
        apa = web()
    Si tipo de fuente == 2:
        apa = libro()
    Si tipo de fuente == 3:
        apa = video()

3. En base a eso, pedir los datos del libro, página web, vídeo, enciclopedia, etc. Guardar esos datos en variables fáciles de recordar. 

4. Mandar cada dato a una función que procese ese dato. Por ejemplo le fecha se va a una función que formatea los datos y regresa la fecha ya lista para incorporar a la referencia. Esto se va a hacer por cada tipo de dato, autor, autores, fecha, páginas, link, título, organización, etc. Para los datos que se junten (como la fecha que tiene año, mes y día), se van a juntar los strings con el comando de +, que en Python se puede hacer. 

Pseudocódigo:

    def web():
        año = input("Escribe el año.")
        mes = input("Escribe el mes.")
        dia = input("Escribe el dia.")
        fecha final = fecha(año, mes, dia)

5. En el programa va a haver muchas funciones, pero tenerlas va a simplificar la vida para entender el programa y ejecutarlo fácilmente. Un ejemplo de cómo va a funcionar es el siguiente: la función del libro usa las funciones del inciso anterior para formatear el APA, donde los datos van a ser guardardados en una variable (es lo que va a regresar la función). Lo que regrese cada función ya va estar con formato de APA, ya que se van a sumar todas las variables con el operador de +. En resumen, va a haber funciones que formatean los elementos, y funciones que te juntan esos elementos en la referencia en una lista.

Pseudocódigo:

    apa = [Autor, fecha, pagina, link]

6. Estado final: Agradecerle al usuario y después de enseñar la referencia terminar el programa. El usuario ya tiene su referencia hecha :)

Pseudocódigo:

    print(apa)
    print("¡Gracias por usar el programa!")
    
* Nota: El Pseudocódigo está muy simplificado y solo incluye un tipo de dato y en específico un tipo de fuente. Esto se hace para simplicidad. Todos los elementos van a llevar el orden de arriba :)
