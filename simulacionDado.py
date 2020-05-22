import random
print("Para Salir del juego presiona Enter")
min_valor_dado = 1
max_valor_dado = 6

repetir = True

while repetir:
    print(random.randint(min_valor_dado, max_valor_dado))

    otro_lanzamiento = input('Quieres tirar los dados otra vez? Escribe si o s \n')
    
    if otro_lanzamiento == 'si' or otro_lanzamiento == 's':
        repetir = True
    else:
        repetir = False

print ("Gracias por Jugar con los dados!!! ")
