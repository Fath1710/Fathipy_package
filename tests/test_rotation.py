# test_rotation.py
import unittest
import numpy as np
from Fathipy.three_vector import ThreeVector
from Fathipy.rotation import Rotation  

class TestRotation(unittest.TestCase):

    def test_rotation_initialization(self):
        # Test de inicialización con un ángulo y un eje de rotación
        axis = ThreeVector(1, 0, 0)  # Eje de rotación: sobre el eje X
        rotation = Rotation(np.pi / 2, axis)  # Rotación de 90 grados
        self.assertTrue(np.isclose(rotation.rotation_matrix[0, 0], 1.0), f"Error en la matriz de rotación en [0, 0]: {rotation.rotation_matrix[0, 0]}")
        self.assertTrue(np.isclose(rotation.rotation_matrix[1, 1], 0.0), f"Error en la matriz de rotación en [1, 1]: {rotation.rotation_matrix[1, 1]}")
        self.assertTrue(np.isclose(rotation.rotation_matrix[2, 2], 0.0), f"Error en la matriz de rotación en [2, 2]: {rotation.rotation_matrix[2, 2]}")

    def test_rotation_zero_axis(self):
        # Test de error cuando el eje de rotación es el vector cero
        with self.assertRaises(ValueError):
            axis = ThreeVector(0, 0, 0)
            Rotation(np.pi / 2, axis)

    def test_rotation_invalid_axis(self):
        # Test de error cuando el eje no es un ThreeVector
        with self.assertRaises(ValueError):
            axis = [1, 0, 0]  # No es un ThreeVector
            Rotation(np.pi / 2, axis)

    def test_rotation_apply(self):
        # Test de aplicar la rotación a un vector
        axis = ThreeVector(0, 0, 1)  # Eje de rotación: sobre el eje Z
        rotation = Rotation(np.pi / 2, axis)  # Rotación de 90 grados

        v = ThreeVector(1, 0, 0)  # Vector que se va a rotar
        rotated_v = rotation.apply(v)

        expected_rotated_v = ThreeVector(0, 1, 0)  # Después de la rotación debería ser (0, 1, 0)
        self.assertTrue(np.allclose(rotated_v.vector, expected_rotated_v.vector), f"Error en la rotación: {rotated_v.vector}")

    def test_rotation_repr(self):
        # Test de la representación de la clase
        axis = ThreeVector(0, 1, 0)  # Eje de rotación: sobre el eje Y
        rotation = Rotation(np.pi / 2, axis)
        repr_str = repr(rotation)
        expected_repr = f"Rotation(rotation_matrix=\n{rotation.rotation_matrix})"
        self.assertEqual(repr_str, expected_repr, f"Error en la representación: {repr_str}")

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
