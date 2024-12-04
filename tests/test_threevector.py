# test_threevector.py
import unittest
import numpy as np
from Fathipy.three_vector import ThreeVector 

class TestThreeVector(unittest.TestCase):
    
    def test_threevector_initialization(self):
        v = ThreeVector(1, 2, 3)
        self.assertTrue(np.all(v.vector == np.array([1, 2, 3], dtype=complex)), f"Error en la inicialización: {v.vector}")

    def test_threevector_addition(self):
        v1 = ThreeVector(1, 2, 3)
        v2 = ThreeVector(4, 5, 6)
        result = v1 + v2
        self.assertTrue(np.all(result.vector == np.array([5, 7, 9], dtype=complex)), f"Error en la suma: {result.vector}")

    def test_threevector_subtraction(self):
        v1 = ThreeVector(5, 6, 7)
        v2 = ThreeVector(1, 2, 3)
        result = v1 - v2
        self.assertTrue(np.all(result.vector == np.array([4, 4, 4], dtype=complex)), f"Error en la resta: {result.vector}")

    def test_threevector_multiplication(self):
        v = ThreeVector(1, 2, 3)
        scalar = 2
        result = v * scalar
        self.assertTrue(np.all(result.vector == np.array([2, 4, 6], dtype=complex)), f"Error en la multiplicación: {result.vector}")

    def test_threevector_dot(self):
        v1 = ThreeVector(1, 2, 3)
        v2 = ThreeVector(4, 5, 6)
        result = v1.dot(v2)
        self.assertTrue(np.isclose(result, 32), f"Error en el producto punto: {result}")

    def test_threevector_cross(self):
        v1 = ThreeVector(1, 0, 0)
        v2 = ThreeVector(0, 1, 0)
        result = v1.cross(v2)
        expected = np.array([0, 0, 1], dtype=complex)
        self.assertTrue(np.all(result.vector == expected), f"Error en el producto cruz: {result.vector}")

    def test_threevector_repr(self):
        v = ThreeVector(1, 2, 3)
        repr_str = repr(v)
        expected_repr = "ThreeVector(x=(1+0j), y=(2+0j), z=(3+0j))"
        self.assertEqual(repr_str, expected_repr, f"Error en la representación: {repr_str}")

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
