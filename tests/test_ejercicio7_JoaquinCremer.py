################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Estos son los tests del ejercicio 7.

"""
import pytest
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    """
       En este test se prueba el caso para pasar de sexadecimal a decimal
    """
    horas = 1
    minutos = 1
    segundos = 30
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert resultado == 3690, "El resultado no es el esperado"
    assert isinstance(resultado, int), "El resultado no es un numero entero"
    pass
def test_decimal_a_sexadecimal():
    """
        En este test se prueba el caso para pasar de decimal a sexadecimal
    """
    numero = 3690
    resul_sexadecimal = decimal_a_sexadecimal(numero)
    assert isinstance(resul_sexadecimal, tuple), "El resultado obtenido no es una tupla"
    assert resul_sexadecimal == (1,1,30), "El resultado no es el esperado"
    pass
