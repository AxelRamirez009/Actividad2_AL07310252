print ("\nEjercicio 3: ¿Cuánto escucho a mi artista favorito?")
print ("\nMI ARTISTA FAVORITO \n")

artista = "Myke Towers"
canciones_por_dia = 13
duracion_promedio = 2.8   # minutos por canción

minutos_dia = canciones_por_dia * duracion_promedio  # minutos al dia 
minutos_anio = minutos_dia * 365                     # minutos al año
horas_anio = minutos_anio / 60                       # 1 hora = 60 minutos
dias_anio = horas_anio / 24                          # 1 dia = 24 horas

print (f"Escuchas a {artista} {minutos_dia} minutos al día")
print (f"Al año son {minutos_anio} minutos")
print (f"Eso equivale a {horas_anio:.1f} horas")
print (f"i0 {dias_anio:.1f} días completos escuchando a {artista}!\n")
       
       