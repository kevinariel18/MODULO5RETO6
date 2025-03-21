import emoji


cantidad_frase = int(input("cuantas fraces desea ingresar:"))
for i in range(cantidad_frase):
    frase = input(" ingrese la frase ")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)
    

