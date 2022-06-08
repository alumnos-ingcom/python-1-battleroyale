################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import compara

"""
Prueba para comprobar los retornos
"""

def test_compara_uno():
    """Al ingresar el primer número
    negativo y el siguiente positivo,
    debería retornar -1, ya que el primero
    es el menor"""
    numero = -10
    otro_numero = 5
    comparacion = compara(numero, otro_numero)
    assert comparacion == -1, "Comparacion debe retornar -1"

def test_compara_menos_uno():
    """Al ingresar el primer número
    positivo y el siguiente negativo
    debería retornar 1, ya que el primero
    es el mayor"""
    numero = 52
    otro_numero = -3
    comparacion = compara(numero, otro_numero)
    assert comparacion == 1, "Comparacion debe retornar 1"

def test_compara_cero():
    """Al ingresar ambos números
    iguales debería retornar 0"""
    numero = 52
    otro_numero = 52
    comparacion = compara(numero, otro_numero)
    assert comparacion == 0, "Comparacion debe retornar 0"
    