################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 6
"""
import pytest
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor


def test_ordenar_mayor_a_menor_abc():
    """
       Test para el caso en el que los numero ingresados estan ordenados: a b c
    """
    a = 10
    b = 5
    c = 3
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (a, b, c), "El resultado no es el esperado"
    pass

def test_ordenar_mayor_a_menor_bac():
    """
       Test para el caso en el que los numero ingresados estan ordenados: b a c
    """
    a = 5
    b = 10
    c = 3
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (b, a, c), "El resultado no es el esperado"
    pass

def test_ordenar_mayor_a_menor_cba():
    """
       Test para el caso en el que los numero ingresados estan ordenados: c b a
    """
    a = 3
    b = 5
    c = 10
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (c, b, a), "El resultado no es el esperado"
    pass

def test_ordenar_mayor_a_menor_bca():
    """
       Test para el caso en el que los numero ingresados estan ordenados: b c a
    """
    a = 3
    b = 10
    c = 5
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (b, c, a), "El resultado no es el esperado"
    pass

def test_ordenar_mayor_a_menor_cab():
    """
       Test para el caso en el que los numero ingresados estan ordenados: c a b 
    """
    a = 5
    b = 3
    c = 10
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (c, a, b), "El resultado no es el esperado"
    pass
def test_ordenar_mayor_a_menor_acb():
    """
       Test para el caso en el que los numero ingresados estan ordenados: a c b
    """
    a = 10
    b = 3
    c = 5
    resul_mayor_a_menor = ordenar_mayor_a_menor(a,b,c)
    assert isinstance(resul_mayor_a_menor, tuple), "El resultado debe ser una tupla"
    assert resul_mayor_a_menor == (a, c, b), "El resultado no es el esperado"
    pass

