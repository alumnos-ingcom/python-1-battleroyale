################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import division_lenta
"""Test con dividendo y divisores positivos y negativos"""

def test_division_lenta_positiva():
    """Test con dividendo y divisor
    positivos"""
    dividendo =  6
    divisor = 3
    cociente, resto = division_lenta(dividendo, divisor)
    assert cociente == 2, "El cociente debe ser 2"
    assert resto == 0, "El resto debe ser 0"

def test_division_lenta_negativa():
    """Test con dividendo y divisor
    negativos"""
    dividendo = -6
    divisor = -3
    cociente, resto = division_lenta(dividendo, divisor)
    assert cociente == 2, "El cociente debe ser 2"
    assert resto == 0, "El resto debe ser 0"

def test_division_lenta_dividendo_negativo():
    """Test con dividendo negativo"""
    dividendo = -6
    divisor = 3
    cociente, resto = division_lenta(dividendo, divisor)
    assert cociente == -2, "El cociente debe ser -2"
    assert resto == 0, "El resto debe ser 0"

def test_division_lenta_divisor_negativo():
    """Test con divisor negativo"""
    dividendo = 6
    divisor = -3
    cociente, resto = division_lenta(dividendo, divisor)
    assert cociente == -2, "El cociente debe ser -2"
    assert resto == 0, "El resto debe ser 0"
