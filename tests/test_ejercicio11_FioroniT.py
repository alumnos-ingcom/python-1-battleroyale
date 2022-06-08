################
# Fioroni Tomás - @FioroniT
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio11 import es_multiplo
"""
Esta función indica con un valor booleano si un número indicado es múltiplo de otro, también indicado.
"""
def test_es_multiplo_true():
    numero = 10
    multiplo = 20
    resultado = es_multiplo(numero, multiplo)
    assert numero < multiplo, "El multiplo no puede ser menor que el numero, se devolverá 'False'" 
    assert isinstance(numero, int), "Los valores de entrada deben ser números enteros (int)"
    assert isinstance(multiplo, int), "Los valores de entrada deben ser números enteros (int)"
    assert isinstance(resultado, bool), "Los valores de salida deben ser de tipo 'bool'"
    assert resultado == True, f"En caso de que {multiplo} sea multiplo de {numero}, el valor devuelto es 'True'"
def test_es_multiplo_false():
    numero = 10
    multiplo = 15
    resultado = es_multiplo(numero, multiplo)
    assert numero < multiplo, "El multiplo no puede ser menor que el numero, se devolverá 'False'"
    assert isinstance(numero, int), "Los valores de entrada deben ser números enteros (int)"
    assert isinstance(multiplo, int), "Los valores de entrada deben ser números enteros (int)"
    assert isinstance(resultado, bool), "Los valores de salida deben ser de tipo 'bool'"
    assert resultado == False, f"En caso de que {multiplo} sea multiplo de {numero}, el valor devuelto es 'False'"
    