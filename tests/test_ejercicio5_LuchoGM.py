################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio5 import division_lenta

"""
Testea con 4 posibilidades, ambos positivos o negativos o intercalados
"""

def test_division_lenta_positivo():
    """
    Se testea la funcion con numeros positivos
    """
    dividendo = 25
    divisor = 5
    resultado = division_lenta(dividendo,divisor)
    assert isinstance (dividendo, int), "El dividendo debe de ser un numero entero"
    assert isinstance (divisor, int), "El divisor debe de ser un numero entero"
    assert dividendo // divisor >= 0, "La division de dos numeros positivos debe de ser mayor a cero"

def test_division_lenta_negativo():
    """
    Se testea la funcion con numeros negativos
    """
    dividendo = -25
    divisor = -5
    resultado = division_lenta(dividendo,divisor)
    assert isinstance (dividendo, int), "El dividendo debe de ser un numero entero"
    assert isinstance (divisor, int), "El divisor debe de ser un numero entero"
    assert dividendo // divisor >= 0, "La division de dos numeros negativos debe de ser mayor a cero"

def test_division_lenta_posyneg():
    """
    Se testea la funcion con numeros positivos y negativos
    """
    dividendo = 25
    divisor = -5
    resultado = division_lenta(dividendo,divisor)
    assert isinstance (dividendo, int), "El dividendo debe de ser un numero entero"
    assert isinstance (divisor, int), "El divisor debe de ser un numero entero"
    assert dividendo // divisor <= 0, "La division entre un numero positivo y uno negativo debe de ser menor a cero"

def test_division_lenta_negypos():
    """
    Se testea la funcion con numeros negativos y positivos
    """
    dividendo = -25
    divisor = 5
    resultado = division_lenta(dividendo,divisor)
    assert isinstance (dividendo, int), "El dividendo debe de ser un numero entero"
    assert isinstance (divisor, int), "El divisor debe de ser un numero entero"
    assert dividendo // divisor <= 0, "La division entre un numero negativo y uno positivo debe de ser menor a cero"