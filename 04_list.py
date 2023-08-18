

### Listas ###

my_list = list()
my_other_list = []


print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36, 1.71, "Erika", "Silverio"]


print(type(my_list))
print(type(my_other_list)) 


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # ao reves
print(my_other_list[-4]) # ao reves
print(my_other_list.count("Erika")) # quants vezes se repite
print(my_list.count(30)) # conta quantas vezes repite

# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # aqui mostra a posicao do que quero imprimir
print(name)

print(my_list + my_other_list) # concatenar listas , me mostre todo o centenido de listas.
# print(my_list - my_other_list) IndexError



my_other_list.append("KiwiQuinoa") # con APPEND se inserta algo al fim da lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # inserta na posicao desejada a informacao desejada.
print(my_other_list)


my_other_list[1] = "Violeta" # quando quer alterar algum elemento , coloque a posicao e o que vai no lugar
print(my_other_list)


my_other_list.remove("Violeta") # remove a informacao solicitada
print(my_other_list)



my_list.remove(30) # remove a informacao solicitada
print(my_list)

# my_list.pop(2) # elimina o ultimo elemento por defecto e nos mostra qual foi
# print(my_list)

print(my_list.pop())  # podemos ver qual elemento foi excluido
print(my_list)

my_pop_element = my_list.pop(2)  # guardando informacao da variavel
print(my_pop_element)
print(my_list)

del my_list[2]  # elimina o item solicitado
print(my_list)




my_new_list = my_list.copy()  # faz uma copia para outra variavel, dos valores que ela possui


my_list.clear()  # apaga toda a lista
print(my_list)
print(my_new_list)




my_list = "Hola Python" # variaveis sao mudaveis
print(my_list)
print(type(my_list))

