# Citatec

## TC1028 - Jesús Alejandro Cedillo Zertuche A01705442

### Contexto
Estar en el Tec de Monterrey muchas veces puede llegar a ser retador por todos los trabajos y actividades que nos dejan. Y muchas de estas actividades tienen algo en común. Esto es el uso del internet. Se usa desde para buscar información en libros, PDFs, páginas web, videos, etc. hasta para simplemente buscar inspiración en algo. Y al hacer esto, se tiene que citar en formato APA todo lo que usaste. 

Me he dado cuenta que mucha gente o no sabe citar en APA, o por todas las versiones diferentes que existen, lo hacen de forma distinta. Es por eso, que voy a crear un programa, que te hace la refrencia del APA y la cita, dependiendo de qué tipo de fuente sea, de acuerdo a la 7º edición; la más nueva y reciente. Me parece muy interesante ya que puedo retar mis capacidades para programar, al mismo tiempo que de cierta forma ayudar a mi universidad. Citar tus fuentes es algo ético que se debe de hacer, y esta es mi forma de ayudar.  

### Pasos del Algoritmo
1. Estado inicial: Pedir al usuario que tipo de fuente le gustaría citar. Asegurar que el tipo de dato sea correcto con un while loop. 

2. Asignar a cada tipo de fuente un número, y usar condiciones para correr las funciones en la parte principal del programa. 

3. En base a eso, pedir los datos del libro, página web, vídeo, enciclopedia, etc. Guardar esos datos en variables fáciles de recordar. 

4. Mandar cada dato a una función que procese ese dato. Por ejemplo le fecha se va a una función que formatea los datos y regresa la fecha ya lista para incorporar a la referencia. Esto se va a hacer por cada tipo de dato, autor, autores, fecha, páginas, link, título, organización, etc. Para los datos que se junten (como la fecha que tiene año, mes y día), se van a juntar los strings con el comando de +, que en Python se puede hacer. 

5. Usar una función por tipo de fuente, para que también este organizado el código. Por ejemplo, la función del libro usa las funciones anteriores para formatear el APA, donde los datos van a ser guardardados en una lista al final en orden (es lo que va a regresar la función). Esto va a permitir poder usar un for loop, para imprimir y enseñarle al usuario la referencia sin escribir muchas líneas de código. En resumen, va a haber funciones que formatean los elementos, y funciones que te juntan la referencia en la lista. El programa va a tener muchas funciones, pero va a simplificar la vida para entenderlo y ejecutarlo fácilmente. 

6. Estado final: Agradecerle al usuario y después de enseñar la referencia terminar el programa. El usuario ya tiene su referencia hecha :)
