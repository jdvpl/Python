
def listas_concatenar_en_nueva_lista():
    list1 = ['A', 'B', 'C', 'E']
    list2 = [1,2,3,4,5]
    list3 = list1 + list2
    print(list1)
    print(list2)
    print(list3)

def listas_concatenar_pero_no_en_nueva_lista():
    list1 = ['A', 'B', 'C', 'E']
    list2 = [1,2,3,4,5]
    list1 = list1 + list2
    print(list1)
    print(list2)

def listas_extend():
    list1 = ['A', 'B', 'C', 'E']
    list2 = [1,2,3,4,5]
    list1.extend(list2)
    print(list1)
    print(list2)

#listas_concatenar_en_nueva_lista()
#listas_concatenar_pero_no_en_nueva_lista()
listas_extend()