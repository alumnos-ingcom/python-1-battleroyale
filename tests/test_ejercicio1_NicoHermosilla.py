################
# Nicolas Hermosilla- @NicoHermosilla
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_centigrados, convertir_a_fahrrenheit

def test_convertir_a_fahrrenheit():
    centigrados=-12
    resultado=convertir_a_fahrrenheit(centigrados)
def test_convertir_a_centigrados():
    fahrrenheit=12
    resultado=convertir_a_centigrados(fahrrenheit)

