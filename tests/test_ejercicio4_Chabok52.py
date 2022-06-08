################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta
"""Testeo para comprobar la suma"""

def test_suma_lenta_positivo():
    """Test con ambos números postivos"""
    numero = 5
    otro_numero = 2
    suma = suma_lenta(numero, otro_numero)
    assert isinstance (suma, int), "El resultado debe ser un número entero"
    assert suma == 7, "El resultado no es el esperado"

def test_suma_lenta_negativos():
    """Test con ambos números negativos"""
    numero = -5
    otro_numero = -2
    suma = suma_lenta(numero, otro_numero)
    assert isinstance (suma, int), "El resultado debe ser un número entero"
    assert suma == -7, "El resultado no es el esperado"

def test_suma_lenta_un_negativo():
    """Test con uno de los números negativos"""
    numero = 5
    otro_numero = -2
    suma = suma_lenta(numero, otro_numero)
    assert isinstance (suma, int), "El resultado debe ser un número entero"
    assert suma == 3, "El resultado no es el esperado"
    