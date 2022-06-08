################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo

"""
En este test se va a probar la funcionalidad del programa de asignación de valores
"""
def test_signo_positivo():
    numero = 5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == 1, "El resultado para un valor positivo debe ser 1"
def test_signo_negativo():
    numero = -5
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == -1, "El resultado para un valor negativo debe ser -1"
def test_signo_neutro():
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número de tipo entero"
    assert resultado == 0, "El resultado para un valor neutro debe ser 0"
    