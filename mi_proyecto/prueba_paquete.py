import utilidades_capacitacion as uc

# probando validaciones
nombre = 'Juan Carlos '
nota_ejemplo = 75
asistencia_ejemplo = 85

print(f'Texto valido?: {uc.texto_no_vacio(nombre)}')
print(f'Nota valida {nota_ejemplo}?: {uc.nota_valida(nota_ejemplo)}')

# probando calculos
mis_notas = [66, 89, 75, 61, 92, 32]
promedio = uc.calcular_promedio(mis_notas)
nota_max = uc.obtener_nota_mayor(mis_notas)
estado = uc.determinar_estado(promedio,asistencia_ejemplo)

print(f'Notas del participante {nombre}: {mis_notas}')
print(f'Promedio obtenido: {promedio:.2f}')
print(f'Su nota mas alta fue de: {nota_max} pts.')
print(f'Como su asistencia fue del {asistencia_ejemplo} % y su promedio fue de: {promedio:.2f}, su estado final fue: {estado}')