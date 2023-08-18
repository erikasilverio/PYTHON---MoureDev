### Tuples ##  DIFERENTES DAS LISTAS , AS TUPLAS nao se pode add outros elementos, somente somar a outros

my_tuple = tuple()
my_other_tuple = ()


my_tuple = (35, 1.70 , "Erika", "Silverio", "Kiwi")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError


print(my_tuple.count("Erika")) # passa o valor e é contado a posicao.
print(my_tuple.count("Kiwi")) # se nao é encontrado entao mostra zero.

print(my_tuple.index("Erika")) # mostra a posicao 
print(my_tuple.index("Silverio")) # mostra a posicao 


# my_tuple[1] = 1.80  # 'tuple' object does not support item assignment, uma tupla é um valor imutable, no se pode add valores 


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)



print(my_sum_tuple[3:6])  # imprimindo elemento 3 e 6

my_tuple = list(my_tuple)  # cambiamos a TUPLE para LIST
print(type(my_tuple))


my_tuple[4] = "Quinoa"
my_tuple.insert(1, "Violeta")
my_tuple = tuple(my_tuple)   # voltamos a mudar de LIST para TUPLE
print(my_tuple)
print(type(my_tuple))   



# del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion , no se puede alterar!!!! aca intente deletar un objecto


del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined


