################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio4 import suma_lenta

"""
Se testea 6 casos en los cuales son positivos o negativos, intercalados
o iguales positivos y iguales negativos
"""

def test_suma_lenta_positivos():
    """
    Testea la funcion con ambos numeros positivos
    """
    n1 = 25
    n2 = 30
    suma = n1 + n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 >= 0 and n2 >= 0,"Debe de ser un numero positivo"
    assert suma >= n1 and suma >= n2, "Al hacer una suma con numeros positivos la suma debe de ser mayor que los numeros ingresados"

def test_suma_lenta_negativos():
    """
    Testea la funcion con ambos numeros negativos
    """
    n1 = -25
    n2 = -30
    suma = n1 + n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 <= 0 and n2 <= 0,"Debe de ser un numero negativo"
    assert suma <= n1 and suma <= n2, "Al hacer una suma con numeros negativos la suma debe de ser menor que los numeros ingresados"

def test_suma_lenta_posyneg():
    """
    Testea la funcion con el primer numero positivo y el otro negativo
    """
    n1 = 5
    n2 = -5
    suma = n1 + n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 >= 0 and n2 <= 0,"El primer numero debe de ser positivo y el segundo debe de ser negativo"
    assert suma <= n1 and suma >= n2, "El resultado de la suma deberia de ser menor que el primero y mayor que el segundo"
    
def test_suma_lenta_negypos():
    """
    Testea la funcion con el primer numero negativo y el segundo positivo
    """
    n1 = -5
    n2 = 5
    suma = n1 + n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 <= 0 and n2 >= 0,"El primer numero debe de ser negativo y el segundo debe de ser positivo"
    assert suma >= n1 and suma <= n2, "El resultado de la suma deberia de ser mayor que el primero y menor que el segundo"
    
def test_suma_lenta_igualespos():
    """
    Testea la funcion con ambos numeros iguales positivos
    """
    n1 = 5
    n2 = 5
    resta = n1 - n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 >= 0 and n2 >= 0,"Debe de ser numeros positivos"
    assert resta == 0, "La resta de dos numeros iguales positivos tiene que dar 0"
    
def test_suma_lenta_igualesneg():
    """
    Testea la funcion con ambos numeros iguales negativos
    """
    n1 = -5
    n2 = -5
    resta = n1 - n2
    funcion = suma_lenta(n1,n2)
    assert isinstance(n1, int), "Se esperaba un nuemero entero"
    assert n1 <= 0 and n2 <= 0,"Debe de ser un numeros negativos"
    assert resta == 0, "La resta de dos numeros iguales negativos tiene que dar 0"