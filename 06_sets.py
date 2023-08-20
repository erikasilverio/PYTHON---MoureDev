### Sets ##  nao admite objectos repetidos!!!!

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un dict ( dicionario)

my_other_set = {"Erika", "Silverio", 36}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("KiwiKiwi")


print(my_other_set)  # Un set no es una estructura ordenada!!! Es imutable!!!

my_other_set.add("KiwiKiwi") # Un set no admite repetido!!!

print(my_other_set)

print("Erika" in my_other_set) # comprovamos se existe esse elementro, realizando buscas
print("Eriki" in my_other_set)

my_other_set.remove("Erika")  # podemos remover um objecto
print(my_other_set)



my_other_set.clear()  # apagamos todos os objectos.
print(my_other_set)
print(len(my_other_set))  # quantos objectos tem

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined ( nao esta definido pq nao esta carregado)

my_set = {"Erika", "Silverio", 36}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"HTML", "PYTHON", "CSS"}

my_new_set = my_set.union(my_other_set)  # unindo informacoes
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "#C"})) # elementos duplicados son ignorado, pero nuevo son add.

print(my_new_set.difference(my_set)) # mostrada informacoes nao duplicadas, as que foram add anteriormente nao aparece porque só foram criadas en union, addim sendo nao foram add, somente foram unidas no print.





