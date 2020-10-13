import clases

persona=clases.Persona()
persona.setNombre("Juan Daniel")
persona.setApellidos("Suarez Amado")
persona.setAltura(168)
persona.setEdad(25)

print(f"""la persona es: {persona.getNombre()} {persona.getApellidos()} 
tiene {persona.getEdad()} años, {persona.hablar()}""")
# clase programador
print("\n-----------------Porgramador--------------\n")
informatico=clases.Programador()
informatico.setNombre("Jiren ")
informatico.setApellidos("Universo 11")

print(f"""{informatico.getNombre()} del {informatico.getApellidos()},
{informatico.dormir()}, {informatico.caminar()}
lenguajes: {informatico.getLenguajes()}, {informatico.experiencia}""")

print("\n------------Tecnico de redes------------")
tecnico=clases.TecnicoRedes()
tecnico.setNombre("Kakaroto")
tecnico.setExperiencia(5)
print(f"""experiencia {tecnico.auditarRedes}, {tecnico.getExpeiencia()} años
{tecnico.getLenguajes()}""")