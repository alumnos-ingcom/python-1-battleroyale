################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
"""
Estas funciones sirven para tomár horas, minutos y segundos, transformalos a segundos
y hacer el camino inverso.
"""
def test_sexadecimal_a_decimal():
    horas = 1
    minutos = 10
    segundos = 5
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado >= 0, "Los datos de salida no pueden ser negativos"
    assert resultado == 4205, "No es el resultado esperado"
def test_decimal_a_sexadecimal():
    numero = 4205
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado == ('1', '10', '5'), "No es el resultado esperado"   
    