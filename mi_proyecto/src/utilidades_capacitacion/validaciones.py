def esta_en_rango(valor, minimo, maximo):
    return minimo <= valor <= maximo

def texto_no_vacio(texto):
    if not isinstance(texto, str):
        return False
    return len(texto.strip()) > 0

def es_positivo(valor):
    return valor > 0

def nota_valida(nota):
    return esta_en_rango(nota, 0, 100)

def asistencia_valida(asistencia):
    return esta_en_rango(asistencia, 0, 100)

