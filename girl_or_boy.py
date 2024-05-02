#Ejercicio de algoritmia

#Se ha ideado un método para identificar el género de los usuarios en un foro basándose en sus nombres de usuario. Según su método, si el número de caracteres distintos en el nombre de usuario es impar, el usuario es masculino. Si es par, el usuario es femenino.

#Escribir una función que determine el género de un usuario basándose en su nombre de usuario. La función debe aceptar un nombre de usuario como parámetro y devolver un mensaje que indique si debería chatear con la persona o ignorarla.

# Especificaciones de la Función:

# Nombre de la función:
# ● El nombre de la función debe ser: girl_or_boy

# Parámetros:
# ● nombre_usuario: Una cadena que contiene solo letras en minúscula.

# Retorno:

#Se crea una función que recibe como parametro un nombre de usuario.
def girl_or_boy(nombre_usuario):
    #Se obtiene el número de caracteres únicos en el nombre de usuario.
    caracteres_unicos = len(set(nombre_usuario))
    print(f'caracteres unicos: {caracteres_unicos}')
    #Se utiliza un condicional para determinar si el número de caracteres distintos es par o impar.
    if caracteres_unicos % 2 == 0:
# ● La función devuelve la cadena "¡ITS A GIRL!" si el número de caracteres distintos es par.
        return "¡ITS A GIRL!"
    else:
# ● La función devuelve la cadena "¡ITS A BOY!" si el número de caracteres distintos es impar.
        return "¡ITS A BOY!"
#Entrada de Prueba:
print(girl_or_boy("joseph"))

