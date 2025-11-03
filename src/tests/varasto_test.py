import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ei_oteta_liikaa(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otetaan_negatiivinen(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisataan_negatiivinen(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_printtaa_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

class Tyhja(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(0)

    def test_virheellinen_varasto(self):
        self.varasto = Varasto(0)
        self.assertEqual(self.varasto.tilavuus, 0)

class Virheellinen(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10, -1)

    def test_virheellinen_alkusaldo(self):
        self.assertEqual(self.varasto.saldo, 0)

class Alku(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(5, 10)

    def test_mahtuuko_alkusaldo(self):
        self.assertEqual(self.varasto.saldo, 5)
