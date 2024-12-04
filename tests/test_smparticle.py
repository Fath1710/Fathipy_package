# test_standardmodelparticle.py
import unittest
from Fathipy.SMparticle import StandardModelParticle  

class TestStandardModelParticle(unittest.TestCase):

    def test_particle_initialization(self):
        # Test de inicialización con todos los parámetros
        particle = StandardModelParticle(
            name="Electron", 
            symbol="e-", 
            mass=0.511, 
            charge=-1, 
            spin=0.5, 
            type_of_particle="fermion"
        )
        
        self.assertEqual(particle.name, "Electron")
        self.assertEqual(particle.symbol, "e-")
        self.assertEqual(particle.mass, 0.511)
        self.assertEqual(particle.charge, -1)
        self.assertEqual(particle.spin, 0.5)
        self.assertEqual(particle.type_of_particle, "fermion")
        self.assertFalse(particle.is_antiparticle)  # El valor por defecto debería ser False

    def test_antiparticle_flag(self):
        # Test para una partícula que es la antipartícula
        particle = StandardModelParticle(
            name="Positron", 
            symbol="e+", 
            mass=0.511, 
            charge=1, 
            spin=0.5, 
            type_of_particle="fermion", 
            is_antiparticle=True
        )
        
        self.assertTrue(particle.is_antiparticle)  # La antipartícula debería tener is_antiparticle = True

    def test_particle_info(self):
        # Test de la descripción de la partícula
        particle = StandardModelParticle(
            name="Proton", 
            symbol="p", 
            mass=938.272, 
            charge=1, 
            spin=0.5, 
            type_of_particle="fermion"
        )
        
        expected_info = "Proton (p) - Masa: 938.272 MeV/c^2, Carga: 1, Espín: 0.5, Tipo: fermion, Antipartícula: False"
        self.assertEqual(particle.info(), expected_info)

    def test_default_is_antiparticle(self):
        # Test para asegurarse de que por defecto is_antiparticle es False
        particle = StandardModelParticle(
            name="Neutron", 
            symbol="n", 
            mass=939.565, 
            charge=0, 
            spin=0.5, 
            type_of_particle="fermion"
        )
        self.assertFalse(particle.is_antiparticle)  # Por defecto debería ser False

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
