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
            type_of_particle="fermion",
            mean_life=6.7e28*365*24*60*60  # Vida media en segundos
        )
        
        self.assertEqual(particle.name, "Electron")
        self.assertEqual(particle.symbol, "e-")
        self.assertEqual(particle.mass, 0.511)
        self.assertEqual(particle.charge, -1)
        self.assertEqual(particle.spin, 0.5)
        self.assertEqual(particle.type_of_particle, "fermion")
        self.assertEqual(particle.mean_life, 6.7e28*365*24*60*60)
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
            is_antiparticle=True,
            mean_life=None  # No se especifica vida media
        )
        
        self.assertTrue(particle.is_antiparticle)  # La antipartícula debería tener is_antiparticle = True
        self.assertIsNone(particle.mean_life)  # Vida media no especificada debería ser None

    def test_particle_info(self):
        # Test de la descripción de la partícula
        particle = StandardModelParticle(
            name="Proton", 
            symbol="p", 
            mass=938.272, 
            charge=1, 
            spin=0.5, 
            type_of_particle="fermion",
            mean_life=1e34  # Vida media aproximada en segundos
        )
        
        expected_info = ("Proton (p) - Masa: 938.272 MeV/c^2, Carga: 1, Espín: 0.5, "
                         "Tipo: fermion, Antipartícula: False, Vida Media 1e+34")
        self.assertEqual(particle.info(), expected_info)

    def test_default_is_antiparticle(self):
        # Test para asegurarse de que por defecto is_antiparticle es False
        particle = StandardModelParticle(
            name="Neutron", 
            symbol="n", 
            mass=939.565, 
            charge=0, 
            spin=0.5, 
            type_of_particle="fermion",
            mean_life=880.2  # Vida media en segundos
        )
        self.assertFalse(particle.is_antiparticle)  # Por defecto debería ser False
        self.assertEqual(particle.mean_life, 880.2)

# Ejecutar las pruebas
if __name__ == "__main__":
    unittest.main()
