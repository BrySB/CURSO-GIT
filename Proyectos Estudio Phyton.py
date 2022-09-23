###### EN ESTE ARCHIVO ESTARÉ CREANDO UNOS VIDEOJUEGOS PARA APRENDER HERRAMIENTAS BÁSICAS DEL LENGUAJE PYTHON #####

### Primer reto: 
# MADLIBS. Son en esencia un texto que completa una oración según unas palabras que se le pidan a un usuario con anterioridad.

to = input("Para: ")
name = input("De: ")
verb1 = input("Escribe un verbo: ")
verb2 = input("Escribe otro verbo: ")
adj1 = input("Escribe un estado de ánimo: ")
adj2 = input("Escribe un elogio: ")
adj3 = input("Escribe un defecto: ")

madlib = f"Hola, {to}. Te saluda {name}. Te escribo porque desde hace un par de meses no hago más que {verb1} de mi {adj1}. No puedo olvidar lo {adj2} que \
siempre fuiste. Espero algún día puedas volver a {verb2} junto a la {adj3} de tu mamá."

print(madlib)