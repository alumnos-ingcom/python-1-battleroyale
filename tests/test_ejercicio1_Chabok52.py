################
# Valentin Mardones - @Chabok52
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados
"""Prueba para ver si devuelven los parametros esperados"""

def test_covertir_a_fahrrenheit_positivos():
    """Test con grados Fahrrenheit positivos"""
    grado = 100
    resultado = convertir_a_fahrrenheit(grado)
    assert isinstance(resultado, float), "el resultado debe ser un número con coma"
    assert resultado > 0, "El resultado debe ser mayor que cero"
    assert resultado == 37.77777777777778, "No obtenemos el resultado esperado"

def test_convertir_a_fahrrenheit_negativos():
    """Test con grados Fahrrenheit negativos"""
    grado = -31
    resultado = convertir_a_fahrrenheit(grado)
    assert isinstance(resultado, float), "el resultado debe ser un número con coma"
    assert resultado < 0, "El resultado debe ser menor que cero"
    assert resultado == -35.0, "No obtenemos el resultado esperado"

def test_convertir_a_centigrados_positivos():
    """Test con grados Centigrados, o Celsius,
    positivos"""
    grado = 100
    resultado = convertir_a_centigrados(grado)
    assert isinstance(resultado, float), "El resultado debe ser un número con coma"
    assert resultado > 0, "El resultado debe ser mayor que cero"
    assert resultado == 212.0, "No obtenemos el resultado esperado"

def test_convertir_a_centigrados_negativos():
    """Test con grados Centigrados, o Celsius,
    negativos"""
    grado = -100
    resultado = convertir_a_centigrados(grado)
    assert isinstance(resultado, float), "El resultado debe ser un número con coma"
    assert resultado < 0, "El resultado debe ser menor que cero"
    assert resultado == -148.0, "No obtenemos el resultado esperado"
    