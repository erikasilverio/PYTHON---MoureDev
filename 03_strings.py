

### Strings ###


my_string = "Mi String"
my__other_string = 'Mi Otro String'

print(len(my_string))
print(len(my__other_string))

print(my_string + " " + my__other_string )

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)


### Formateo ###

name, surname, age = "Erika", "Silverio", 36

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))  # %s para letras e %d para numeros
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

### Desempaquetado de caracteres ###

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

## Dividión ##

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

## Reverse ##

reversed_languagem = language[::-1]
print(reversed_languagem)

## Funciones del Sistema

print(language.capitalize()) # primera letras en mayuscula
print(language.upper()) # TODAS letras en mayuscula
print(language.count("t")) # conta cuantas letras tiene , aca CUANTAS T HAY
print(language.isnumeric()) # se é um numero 
print("1".isnumeric()) # imprima se o 1 é um numero
print(language.lower()) # deja TODAS las letras en minusculas
print(language.upper().isupper()) # 
print(language.startswith("py")) # Python empieza con py? 
print(language.startswith("Py")) # Python empieza con Py? 
print("Py" == "py") ## no es lo mismo Py y py por eso es False!!!


