################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
"""Test con grados, minutos y segundos, y segundos solos"""

def test_sexadecimal_a_decimal():
    """Test de conversión de grados
    minutos y segundos, a segundos"""
    grados = 52
    minutos = 52
    segundos = 52
    resultado = sexadecimal_a_decimal(grados, minutos, segundos)
    assert isinstance (resultado, int), "El resultado debe ser un entero"
    assert resultado == 190372, "El resultado no es el esperado"

def test_decimal_a_sexadecimal():
    """Test conversión de segundos
    a grados, minutos y segundos"""
    numero = 5252
    grados, minutos, segundos = decimal_a_sexadecimal(numero)
    assert grados == 1, "Los grados deben ser 1"
    assert minutos == 27, "Los minutos deben ser 27"
    assert segundos == 32, "Los segundos deben ser 32"
