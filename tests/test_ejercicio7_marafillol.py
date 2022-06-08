################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""TEST EJERCICIO 7
"""
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
def test_sexadecimal_a_decimal_positivos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas = 2
    minutos = 37
    segundos = 20
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 9440 , "No se obtiene el resultado esperado."
def test_sexadecimal_a_decimal_cero_horas():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas = 0
    minutos = 59
    segundos = 60
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 3600, "No se obtiene el resultado esperado."
def test_sexadecimal_a_decimal_cero_minutos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas = 3
    minutos = 0
    segundos = 60
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 10860, "No se obtiene el resultado esperado."
def test_sexadecimal_a_decimal_cero_segundos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas = 1
    minutos = 60
    segundos = 0
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 7200, "No se obtiene el resultado esperado."
def test_sexadecimal_a_decimal_h_m_s_iguales():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas = 1
    minutos = 1
    segundos = 1
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 3661 , "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_cero():
    """Esta función evalúa si decimal_a_sexadecimal funciona correctamente.
    """
    numero = 0
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (0,0,0), "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_positivo():
    """Esta función evalúa si decimal_a_sexadecimal funciona correctamente.
    """
    numero = 7514
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado == (2,5,14), "No se obtiene el resultado esperado."
    