import unittest
import Calculadora

class PruebaCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Calculadora.suma((3,-1),(1,4)),(4,3))
    def test_resta(self):
        self.assertEqual(Calculadora.resta((3,-1),(1,4)),(2,-5))
    def test_multiplicacion(self):
        self.assertEqual(Calculadora.multiplicacion((3,-1),(1,4)),(7,11))
    def test_multiplicacioncuadradoComplejo(self):
        self.assertEqual(Calculadora.multiplicacion((0,1),(0,1)),(-1,0))
    def test_division(self):
        self.assertEqual(Calculadora.division((-2,1),(1,2)),(0.0,1.0))
    def test_modulo(self):
        self.assertEqual(Calculadora.modulo((1,-1)),1.4142135623730951)
    def test_conjugado(self):
        self.assertEqual(Calculadora.conjugado((1,-1)),(1,1))
    def test_fase(self):
        self.assertEqual(Calculadora.fase((1,1)),(45.0))
    def test_convpolaracartesiano(self):
        self.assertEqual(Calculadora.convpolaracartesiano((3.16,108.43)),(-0.999020803757226,2.9979255217000085))
    def test_convcartesianoapolar(self):
        self.assertEqual(Calculadora.convcartesianoapolar((1,1)),(1.4142135623730951,45.0))
    def test_sumaVectores(self):
        self.assertEqual(Calculadora.sumaVectores([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)],[(16.0, 2.3), (0.0, -7.0), (6.0, 0.0), (0.0, -4.0)]),[(22.0, -1.7000000000000002), (7.0, -4.0), (10.2, -8.1), (0.0, -7.0)])
    def test_sumaVectoresImposible(self):
        self.assertEqual(Calculadora.sumaVectores([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)],[(16.0, 2.3), (0.0, -7.0), (6.0, 0.0)]),"Imposible")
    def test_inversa(self):
        self.assertEqual(Calculadora.inversa([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)]),[(-6.0, 4.0), (-7.0, -3.0), (-4.2, 8.1), (0.0, 3.0)])
    def test_multiplicacionEscalarVector(self):
        self.assertEqual(Calculadora.multiplicacionEscalarVector([(6.0, 3.0), (0.0, 0.0), (5.0, 1.0), (4.0, 0.0)],(3.0, 2.0)),[(12.0, 21.0), (0.0, 0.0), (13.0, 13.0), (12.0, 8.0)])
    def test_sumaMatrices(self):
        self.assertEqual(Calculadora.sumaMatrices([[(6.0, -4.0), (6.0, -4.0)], [(7.0, 3.0), (7.0, 3.0)]],[[(4.2, -8.1), (4.2, -8.1)], [(0.0, -3.0), (0.0, -3.0)]]),[[(10.2, -12.1), (10.2, -12.1)], [(7.0, 0.0), (7.0, 0.0)]])
    def test_sumaMatricesImposible(self):
        self.assertEqual(Calculadora.sumaMatrices([[(6.0, -4.0), (6.0, -4.0)], [(7.0, 3.0), (7.0, 3.0)]],[[(4.2, -8.1), (4.2, -8.1)]]),"Imposible")
    def test_inversaMatriz(self):
        self.assertEqual(Calculadora.inversaMatriz([[(16.0, 2.3), (16.0, 2.3)], [(0.0, -7.0), (0.0, -7.0)], [(6.0, 0.0), (6.0, 0.0)], [(0.0, -4.0), (0.0, -4.0)]]),[[(-16.0, -2.3), (-16.0, -2.3)], [(0.0, 7.0), (0.0, 7.0)], [(-6.0, 0.0), (-6.0, 0.0)], [(0.0, 4.0), (0.0, 4.0)]])
    def test_multiplicacionEscalarMatriz(self):
        self.assertEqual(Calculadora.multiplicacionEscalarMatriz([[(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)], [(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)]],(4.0, 0.0)),[[(4.0, -8.0), (8.0, 12.0)], [(12.0, 16.0), (16.0, -20.0)], [(4.0, -8.0), (8.0, 12.0)], [(12.0, 16.0), (16.0, -20.0)]])
    def test_transpuesta(self):
        self.assertEqual(Calculadora.transpuesta([[(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)], [(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)]]),[[(1.0, -2.0), (3.0, 4.0), (1.0, -2.0), (3.0, 4.0)], [(2.0, 3.0), (4.0, -5.0), (2.0, 3.0), (4.0, -5.0)]])
    def test_matrizConjugada(self):
        self.assertEqual(Calculadora.matrizConjugada([[(1.0, -2.0), (2.0, 3.0), (4.0, 5.0)], [(3.0, 4.0), (4.0, -5.0), (5.0, 6.0)], [(1.0, -2.0), (2.0, 3.0), (7.0, 8.0)]]),[[(1.0, 2.0), (2.0, -3.0), (4.0, -5.0)], [(3.0, -4.0), (4.0, 5.0), (5.0, -6.0)], [(1.0, 2.0), (2.0, -3.0), (7.0, -8.0)]])
    def test_matrizAdjunta(self):
        self.assertEqual(Calculadora.matrizAdjunta([[(1.0, -2.0), (2.0, 3.0), (4.0, 5.0)], [(3.0, 4.0), (4.0, -5.0), (5.0, 6.0)], [(1.0, -2.0), (2.0, 3.0), (7.0, 8.0)]]),[[(1.0, 2.0), (3.0, -4.0), (1.0, 2.0)], [(2.0, -3.0), (4.0, 5.0), (2.0, -3.0)], [(4.0, -5.0), (5.0, -6.0), (7.0, -8.0)]])
    def test_multiplicacionMatrizMatriz(self):
        self.assertEqual(Calculadora.multiplicacionMatrizMatriz([[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)], [(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)]],[[(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)], [(0.0, 0.0), (4.0, 5.0), (2.0, 0.0)], [(7.0, -4.0), (2.0, 7.0), (0.0, 0.0)]]),[[(26.0, -52.0), (60.0, 24.0), (26.0, 0.0)], [(9.0, 7.0), (1.0, 29.0), (14.0, 0.0)], [(48.0, -21.0), (15.0, 22.0), (20.0, -22.0)]])
    def test_multiplicacionMatrizMatrizImposible(self):
        self.assertEqual(Calculadora.multiplicacionMatrizMatriz([[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)], [(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)]],[[(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)], [(0.0, 0.0), (4.0, 5.0), (2.0, 0.0)]]),"Imposible")
    def test_accion(self):
        self.assertEqual(Calculadora.accion([[(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)], [(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)]],[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)]),[[(9.0, 7.0)], [(34.0, -19.0)], [(21.0, -46.0)]])
    def test_accionImposible(self):
        self.assertEqual(Calculadora.accion([[(1.0, 0.0), (4.0, 2.0)], [(4.0, -1.0), (0.0, 0.0)], [(5.0, 0.0), (2.0, -1.0)]],[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)]),"Imposible")
    def test_sumaDiagonal(self):
        self.assertEqual(Calculadora.sumaDiagonal([[(1.0, 0.0), (0.0, 0.0), (0.0, 0.0)], [(0.0, 0.0), (1.0, 0.0), (0.0, 0.0)], [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0)]]),(3.0, 0.0))
    def test_productoInternoMatriz(self):
        self.assertEqual(Calculadora.productoInternoMatriz([[(1.0, 0.0), (-1.0, 0.0)], [(1.0, 0.0), (1.0, 0.0)]],[[(2.0, 0.0), (1.0, 0.0)], [(1.0, 0.0), (3.0, 0.0)]]),(5.0, 0.0))
    def test_productoInternoMatrizImposible(self):
        self.assertEqual(Calculadora.productoInternoMatriz([[(1.0, 0.0), (-1.0, 0.0)], [(1.0, 0.0), (1.0, 0.0)]],[[(1.0, 0.0), (3.0, 0.0)]]),"Imposible")
    def test_normaMatriz(self):
        self.assertEqual(Calculadora.normaMatriz([[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),9.16515138991168)
    def test_distanciaMatrizMatriz(self):
        self.assertEqual(Calculadora.distanciaMatrizMatriz([[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]],[[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),0.0)
    def test_distanciaMatrizMatrizImposible(self):
        self.assertEqual(Calculadora.distanciaMatrizMatriz([[(3.0, 2.0), (2.0, 4.0)]],[[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),"Imposible")
    def test_matrizIdentidad(self):
        self.assertEqual(Calculadora.matrizIdentidad(3),[[(1, 0), (0, 0), (0, 0)], [(0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), (1, 0)]])
    def test_matrizUnitaria(self):
        self.assertEqual(Calculadora.matrizUnitaria([[(0.0, 0.0), (0.0, 1.0)], [(0.0, -1.0), (0.0, 0.0)]]),True)
    def test_matrizUnitariaNoes(self):
        self.assertEqual(Calculadora.matrizUnitaria([[(0.0, 0.0), (2.4, 1.0)], [(0.0, 1.0), (0.0, 3.5)]]),False)
    def test_matrizUnitariaImposible(self):
        self.assertEqual(Calculadora.matrizUnitaria([[(0.0, 0.0), (0.0, 1.0)], [(0.0, -1.0), (0.0, 0.0)],[(0.0, -1.0), (0.0, 0.0)]]),"Imposible")
    def test_matrizHermitian(self):
        self.assertEqual(Calculadora.matrizHermitian([[(5.0, 0.0), (4.0, 5.0), (6.0, -16.0)], [(4.0, -5.0), (13.0, 0.0), (7.0, 0.0)], [(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)]]),True)
    def test_matrizHermitianNoes(self):
        self.assertEqual(Calculadora.matrizHermitian([[(5.0, 0.0), (4.0, 5.0)], [(4.0, -5.0), (13.0, 5.4)]]),False)
    def test_matrizHermitianImposible(self):
        self.assertEqual(Calculadora.matrizHermitian([[(5.0, 0.0), (4.0, 5.0), (6.0, -16.0)], [(4.0, -5.0), (13.0, 0.0), (7.0, 0.0)], [(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)],[(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)]]),"Imposible")
    def test_productoTensor(self):
        self.assertEqual(Calculadora.productoTensor([[(3.0, 2.0), (5.0, -1.0), (0.0, 2.0)], [(0.0, 0.0), (12.0, 0.0), (6.0, -3.0)], [(2.0, 0.0), (4.0, 4.0), (9.0, 3.0)]],[[(1.0, 0.0), (3.0, 4.0), (5.0, -7.0)], [(10.0, 2.0), (6.0, 0.0), (2.0, 5.0)], [(0.0, 0.0), (1.0, 0.0), (2.0, 9.0)]]),[[(3.0, 2.0), (1.0, 18.0), (29.0, -11.0), (5.0, -1.0), (19.0, 17.0), (18.0, -40.0), (0.0, 2.0), (-8.0, 6.0), (14.0, 10.0)], [(26.0, 26.0), (18.0, 12.0), (-4.0, 19.0), (52.0, 0.0), (30.0, -6.0), (15.0, 23.0), (-4.0, 20.0), (0.0, 12.0), (-10.0, 4.0)], [(0.0, 0.0), (3.0, 2.0), (-12.0, 31.0), (0.0, 0.0), (5.0, -1.0), (19.0, 43.0), (0.0, 0.0), (0.0, 2.0), (-18.0, 4.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (36.0, 48.0), (60.0, -84.0), (6.0, -3.0), (30.0, 15.0), (9.0, -57.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (120.0, 24.0), (72.0, 0.0), (24.0, 60.0), (66.0, -18.0), (36.0, -18.0), (27.0, 24.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (24.0, 108.0), (0.0, 0.0), (6.0, -3.0), (39.0, 48.0)], [(2.0, 0.0), (6.0, 8.0), (10.0, -14.0), (4.0, 4.0), (-4.0, 28.0), (48.0, -8.0), (9.0, 3.0), (15.0, 45.0), (66.0, -48.0)], [(20.0, 4.0), (12.0, 0.0), (4.0, 10.0), (32.0, 48.0), (24.0, 24.0), (-12.0, 28.0), (84.0, 48.0), (54.0, 18.0), (3.0, 51.0)], [(0.0, 0.0), (2.0, 0.0), (4.0, 18.0), (0.0, 0.0), (4.0, 4.0), (-28.0, 44.0), (0.0, 0.0), (9.0, 3.0), (-9.0, 87.0)]])
if __name__ == "__main__":
    unittest.main()
	
	
