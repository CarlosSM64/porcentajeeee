# Escriba un programa que solicite al usuario el ingreso de dos palabras,
# las cuales se guardarán en dos variables distintas.
# A continuación, almacena en una Variable la concatenación de la primera palabra,
# mas un espacio, más la segunda palabra. Muestre el resultado en pantalla

primera_palabra = str(input("Ingrese la primera palabra: "))
segunda_palabra = str(input("Ingrese la segunda palabra: "))

Conca = str(primera_palabra) + " " + str(segunda_palabra)

print("La palabra completa es "+ str(Conca))
