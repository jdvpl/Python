

tabla=[
    {
        "categoria":"Accion",
        "juegos":["Gta","call of duty","free fire"]

    },
    {
        "categoria":"Aventura",
        "juegos":["Asassins Creed","Crash","God of War"]
    },
    {
        "categoria":"Deporte",
        "juegos":["fifa","pes","moto Gp"]
    }
]
for i in tabla:
    print(f"---- {i['categoria']}-------")
    for juego in i['juegos']:
        print(juego)