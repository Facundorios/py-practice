# Ejercicio de Pandas

# Se les ha proporcionado un archivo CSV que contiene una lista de 250 personas junto con sus fechas de nacimiento, que van desde 1990 hasta 2004. Su tarea es la siguiente:

# ● Importar los datos del archivo, pero solo incluir a aquellas personas que sean mayores de 25 años.

# ● Ordenar las edades en forma ascendente.

# ● Determinar cuántas edades distintas existen y la frecuencia de cada una.

# ● Crear un DataFrame que incluya dos columnas: una para las edades y otra para la frecuencia de cada edad.
import pandas as pd
import matplotlib.pyplot as plt

#"Importación" y lectura del archivo
df = pd.read_csv("edades.csv")

# Importar los datos del archivo, pero solo incluir a aquellas personas que sean mayores de 25 años.


# Funcion que recibe comoaprametro un dataframe.
def odlers_than_25(df):
    # Dividimos la columna "age". en strings, que son separados por "/".

    ages = df["age"].str.split("/")

    # Re-definimos "ages",con el valor 2 del arreglo coseguido dela columna "age", que corresponde al año de nacimiento.
    ages = ages.str[2]

    # Obtenemos los nombres de las personas.
    names = df["full_name"]

    # Creamos un diccionario vacio.
    diccionary = {}

    # Utlizamos un for para recorrer las edades. En este caso, la longitud de las edades.
    for i in range(len(ages)):
        # con names[i], podemos obtener el nombre de las personas. Y con ages[i], lo mismo.
        current_year = 2024

        # Calculamos las edades. El archivo csv no contiene la edades concretamente, solo la fecha de nacimiento,por lo que restamos el año actual menos el año de nacimiento.
        age = current_year - int(ages[i])

        # Hacemos un condicional, en donde si la edad es mayor a 25, guardamos el nombre y la edad en un diccionario.

        if age > 25:

            # Guardamos el nombre y la edad en el diccionario.
            diccionary[names[i]] = age

        # Ordenamos las edades de forma ascendente.

        # En esta linea, el diccionario utiliza la funcion dict() para convertir el diccionario en una lista de tuplas, y la funcion sorted() para ordenar las edades de forma ascendente. Dentro de la funcion sorted(), se utiliza el parametro key, para indicar que se ordene por el valor de la edad. Se usa la funcion lambda para indicar que se ordene por el valor de la edad y el item[1] indica que se ordene por el valor de la edad.

        diccionary = dict(sorted(diccionary.items(), key=lambda item: item[1]))

    # Creamos un diccionario vacio.
    ages_diccionary = {}

    # Recorremos el diccionario, En este caso, este for recorre el diccionario, el cual guarda los nombres y las edades que son mayores a 25.
    for key in diccionary:
        # En esta linea, se guarda en el diccionario "ages_diccionary" la edad y la frecuencia de la edad. Para eso, se utiliza la funcion get() para obtener el valor de la edad, y se le suma 1 para indicar que hay una frecuencia de la edad, y se le pasa el 0, para indicar que si no hay una frecuencia de la edad, se le asigne un 0.
        ages_diccionary[diccionary[key]] = ages_diccionary.get(diccionary[key], 0) + 1

    # Creamos un dataframe con los datos, usando la propiedad list y dentro pasamos el ages_diccioanry con el metodo items, y le pasamos los nombres de las columnas.
    df = pd.DataFrame(list(ages_diccionary.items()), columns=["Edades", "fi"])
    
    plt.plot(df["Edades"], df["fi"])
    plt.title("Frecuencia de edades")
    plt.show()
    
    
    return df


print(odlers_than_25(df))
