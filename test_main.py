"""Módulo de pruebas para main.py."""

from main import saludo

def test_saludo():
    """Prueba la función saludo."""
    assert saludo() == "Hola CI/CD"
