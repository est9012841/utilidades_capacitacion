def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def calcular_porcentaje(parte, total):
    if total == 0:
        return 0
    return (parte / total) * 100

def determinar_estado(promedio, asistencia):
    if promedio >= 60 and asistencia >= 80:
        return 'Aprobado'
    return 'Reprobado'

def obtener_nota_mayor(notas):
    if not notas:
        return 0
    return max(notas)

def obtener_nota_menor(notas):
    if not notas:
        return 0
    return min(notas)

