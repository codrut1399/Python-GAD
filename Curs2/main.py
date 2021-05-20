my_list=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_ascendent_list=my_list[:]

my_ascendent_list.sort()

my_descendent_list=my_ascendent_list[:]
my_descendent_list.reverse()
print("Lista initiala: ", my_list)
print("Lista ordonata ascendent: ", my_ascendent_list)
print("Lista ordonata descendent: ", my_descendent_list)
print("Numerele pare din lista: ", my_ascendent_list[1::2])
print("Numerele impare din lista:", my_ascendent_list[::2])
print("Elemente multipli de 3: ", my_ascendent_list[2::3])