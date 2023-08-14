# Variables




my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print (type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)



# Concatenación de variables en un print

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable)

#Algunas Funciones del Sistema

print(len(my_string_variable))  # contanto caracteres. tambien conta los espacios.

# Variables en una sola linea !! Cuidado con abusar de esta sintaxis !!

name, surname, alias, age = "Erika", "Silverio", "Eri", 36
print("Mi llamo:",name, surname,". Mi edad es:",age, ".Y mi alias es:",alias)


# INPUTS ( variable podem cambiar de valor) 
"""
name = input('What is your name:')
age = input('How old are you?')

print(name)
print(age)

"""

# CAMBIAMOS SU TIPO

name = 36
age = "Erika"
print(name)
print(age)







