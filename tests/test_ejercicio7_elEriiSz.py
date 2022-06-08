################
# Eric Alexander Szuka - @elEriiSz
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Estos son los test correspondienets al archivo `ejercicio6.py` que esta en
`src`
"""

import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_funciona():
    horas = 1
    minutos = 0
    segundos = 1
    decimal = 3600
    hora, minuto, segundo = decimal_a_sexadecimal(decimal)
    decimales = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(hora, int), "el resultado debe ser un número entero"
    assert isinstance(minuto, int), "el resultado debe ser un número entero"
    assert isinstance(segundo, int), "el resultado debe ser un número entero"
    assert isinstance(decimales, int), "el resultado debe ser un número entero"
    assert hora == 1, "el resultado hora para el valor 3600 debe ser 1"
    assert minuto == 0, "el resultado minuto para el valor 3600 debe ser 0"
    assert segundo == 0, "el resultado segundo para el valor 3600 debe ser 0"
    assert decimales == 3601, "el resultado decimales para los valores 1, 0, 1 debe ser 3601"


def test_menor_60():
    decimal = 3600
    hora, minuto, segundo = decimal_a_sexadecimal(decimal)
    assert isinstance(minuto, int), "el resultado debe ser un número entero"
    assert isinstance(segundo, int), "el resultado debe ser un número entero"
    assert minuto < 60, "el resultado minuto para el valor 3600 debe ser menor a 60"
    assert segundo < 60, "el resultado segundo para el valor 3600 debe ser menor a 60"


def test_mayor_0():
    horas = 1
    minutos = 0
    segundos = 1
    decimal = 3600
    hora, minuto, segundo = decimal_a_sexadecimal(decimal)
    decimales = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(hora, int), "el resultado debe ser un número entero"
    assert isinstance(minuto, int), "el resultado debe ser un número entero"
    assert isinstance(segundo, int), "el resultado debe ser un número entero"
    assert isinstance(decimales, int), "el resultado debe ser un número entero"
    assert hora >= 0, "el resultado hora para el valor 3600 debe ser mayor o igual a 0"
    assert minuto >= 0, "el resultado minuto para el valor 3600 debe ser mayor o igual a 0"
    assert segundo >= 0, "el resultado segundo para el valor 3600 debe ser mayor o igual a 0"
    assert decimales >= 0, "el resultado decimales para los valores 1, 0, 1 debe ser mayor o igual a 0"

