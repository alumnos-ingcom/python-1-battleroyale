################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 4
"""
from src.ejercicio4 import suma_lenta
def test_sumar_lenta_siendo_ambos_positivos():
    """Esta función verifica si la función suma_lenta funciona correctamente.
    """
    numero = 5
    otro_numero = 4
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 9, "No se obtiene el resultado esperado."
def test_sumar_lenta_siendo_ambos_negativos():
    """Esta función verifica si la función suma_lenta funciona correctamente.
    """
    numero = -2
    otro_numero = -3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -5, "No se obtiene el resultado esperado."
def test_sumar_lenta_siendo_otro_numero_negativo():
    """Esta función verifica si la función suma_lenta funciona correctamente.
    """
    numero = 3
    otro_numero = -3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == 0, "No se obtiene el resultado esperado."
def test_suma_lenta_siendo_numero_negativo():
    """Esta función verifica si la función suma_lenta funciona correctamente.
    """
    numero = -8
    otro_numero = 3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un entero"
    assert resultado == -5, "No se obtiene el resultado esperado."
def test_suma_lenta_siendo_ambos_cero():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero = 0
    otro_numero = 0
    resultado=suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 0, "No se obtiene el resultado esperado."
    