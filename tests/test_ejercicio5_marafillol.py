################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 5
"""
from src.ejercicio5 import division_lenta
def test_division_lenta_siendo_ambos_positivos():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo = 4
    divisor = 2
    respuesta = division_lenta(dividendo, divisor)
    assert isinstance(respuesta, tuple), 'El resultado debe ser una tupla.'
    assert respuesta[0] == 2, 'No es el resultado esperado.'
    assert respuesta[1] == 0, 'No es el resultado esperado.'
def test_division_lenta_siendo_ambos_negativos():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo = -2
    divisor = -1
    respuesta = division_lenta(dividendo, divisor)
    assert isinstance(respuesta, tuple), 'El resultado debe ser una tupla.'
    assert respuesta[0] == 0, 'No es el resultado esperado.'
    assert respuesta[1] == -2, 'No es el resultado esperado.'
def test_division_lenta_siendo_dividendo_negativo():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo = -6
    divisor = 2
    respuesta = division_lenta(dividendo, divisor)
    assert isinstance(respuesta, tuple), 'El resultado debe ser una tupla.'
    assert respuesta[0] == 0, 'No es el resultado esperado.'
    assert respuesta[1] == -6, 'No es el resultado esperado.'
def test_division_lenta_siendo_iguales():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo = 7
    divisor = 7
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == 1, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."
def test_division_lenta_siendo_divisor_cero():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo = 0
    divisor = 9
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0] == 0, "No se obtiene el resultado esperado."
    assert resultado[1] == 0, "No se obtiene el resultado esperado."
