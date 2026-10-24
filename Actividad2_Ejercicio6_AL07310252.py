print("\n==============================================================")
print("Ejercicio 6: Vidas y daño")
print("========================= BATALLA ========================")
# Damos de alta la variable personaje y vida
personaje = "Axel"
vida = 97
print(f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")
# Como vida vale 100, esta fórmula dice: vida = 100 - 25
vida = vida - 25
print(f"Me dio un golpe un goblin, ahora tengo vida: {vida}")
# Ahora vida vale 75, esta fórmula dice: vida = 75 - 40
vida = vida - 40
print(f"Ah, ahora me tocó el golpe de un ogro, tengo de vida: {vida}")
# Ahora vida vale 35, esta fórmula dice: vida = 35 - 15
vida = vida - 15
print(f"¡Me tocó una flecha enemiga!, tengo de vida: {vida}")
# Ahora vida vale 20, esta fórmula dice: vida = 20 + 30
vida = vida + 30
print(f"Tomó una poción... mi vida: {vida}")

print(f"\n{personaje} terminó la batalla con {vida} HP\n")
print("==============================================================")