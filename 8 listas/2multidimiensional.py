# listas multidimensionales
# son listas que estan dentro de otras listas
print("#####Listado de contactos #####")
contactos=[
    [
    'Juan Daniel',
    'Juanda554242@gmail.com',
    '3209188638'
    ],
    [
        'Jiren',
        'jiren@gmail.com',
        '3152483691'
    ],
    [
        'Lucifer',
        'lucifer@mail.com',
        '312547896'
    ]
]
print(contactos)
print(contactos[1][2]) # accede a la sublista en la poscion 2 del la poscion 1
print("\nContactos solos\n")
for x in contactos:
    for elemento in x:
        if x.index(elemento)==0:
            print(f"Nombre: {elemento}")
        elif x.index(elemento)==1:
            print(f"Email: {elemento}")
        else:
            print(f"Telefono: {elemento}")

    print("\n")
