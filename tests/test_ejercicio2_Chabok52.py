################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import signo
"""Testeo de la función signo con
    3 variables"""

def test_signo_negativo():
    """
    Testeo con un número negativo
    """
    numero = -52
    negativo = signo(numero)
    assert negativo == -1, "El numero debe ser negativo"

def test_signo_positivo():
    """Testo con un número positivo"""
    numero = 52
    positivo = signo(numero)
    assert positivo == 1, "El número debe ser positivo"

def test_signo_cero():
    """Testeo con 0"""
    numero = 0
    cero = signo(numero)
    assert cero == 0, "El número debe ser 0"
    