### DICIONARIOS ## SEPARADOS POR :  - ARMAZENANDO CLAVE Y VALOR

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Erika", "Apellido":"Silverio", "Edad":36, 1:"Python"}

my_dict = {
    "Nombre":"Erika",
    "Apellido":"Silverio",
    "Edad":36,
    "Languagens":{"Python", "CSS", "Java"},
    1:1.71
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # quantos elementos
print(len(my_dict)) # quantos elementos 

print(my_dict["Nombre"])  # busca a clave a vai imprimir o valor 

my_dict["Nombre"]= "Pedro"  # alterando um valor
print(my_dict["Nombre"])

my_dict["Calle"] = "KiwiLandia"
print(my_dict)

del my_dict["Calle"]  # eliminando un elemento del dict!!!!!!
print(my_dict)

print("Silverio" in my_dict) # estamos buscando o VALOR!!! se busca na verdad a CLAVE
print("Apellido" in my_dict) #  se busca na verdad a clave

print(my_dict.items()) # mostra todo o dicionario
print(my_dict.keys()) # mostra todos as claves
print(my_dict.values()) # mostra todos os valores


my_list = ["Nombre", 1, "Piso"]


my_new_ditc = dict.fromkeys((my_list)) # criamos un nuevo dicionario sin valores, depois posso por datos
print(my_new_ditc)

my_new_ditc = dict.fromkeys(("Nombre", 1, "Piso")) # criamos un nuevo dicionario sin valores, depois posso por datos
print(my_new_ditc)

my_new_ditc = dict.fromkeys(my_dict) # nuevo dicionario , com claves
print((my_new_ditc))


my_new_ditc = dict.fromkeys(my_dict, "Kiwkizinha") # nuevo dicionario , com valores se duplican em todas as claves
print((my_new_ditc))


my_values = my_new_ditc.values()
print(type(my_values))


print(my_new_ditc.values())
print(list(dict.fromkeys(list(my_new_ditc.values())).keys()))
print(list(dict.fromkeys(list(my_new_ditc.keys()))))


print(list(my_new_ditc)) # mostrando as CLAVES, foi transformado em LIST
print(tuple(my_new_ditc)) # mostrando as CLAVES, foi transformado em TUPLE
print(set(my_new_ditc)) # mostrando as CLAVES, foi transformado em SET ( aparece desordenado)


