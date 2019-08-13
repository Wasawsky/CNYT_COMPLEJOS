import unittest
import Calculadora

class PruebaCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Calculadora.suma((3,-1),(1,4)),(4,3))
    def test_resta(self):
        self.assertEqual(Calculadora.resta((3,-1),(1,4)),(2,-5))
    def test_multiplicacion(self):
        self.assertEqual(Calculadora.multiplicacion((3,-1),(1,4)),(7,11))
    def test_division(self):
        self.assertEqual(Calculadora.division((-2,1),(1,2)),(0.0,1.0))
    def test_modulo(self):
        self.assertEqual(Calculadora.modulo((1,-1)),1.41)
    def test_conjugado(self):
        self.assertEqual(Calculadora.conjugado((1,-1)),(1,1))
    def test_fase(self):
        self.assertEqual(Calculadora.fase((1,1)),(45.0))
    def test_convpolaracartesiano(self):
        self.assertEqual(Calculadora.convpolaracartesiano((3.16,108.43)),(-1.0,3.0))
    def test_convcartesianoapolar(self):
        self.assertEqual(Calculadora.convcartesianoapolar((1,1)),(1.41,45.0))

if __name__ == "__main__":
    unittest.main()
	
	
