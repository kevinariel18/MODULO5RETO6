import random


aleatorio=random.randint(1,9)
aleatorio_dos=random.randint(1,9)

if aleatorio == 4:
    print("te ganaste un chupete")
elif aleatorio == 8:
    print("te ganaste un balon")
elif aleatorio == 3 and aleatorio_dos ==7:
    print("te ganaste un televisor")
else:
    print("perdiste el juego")