#Importamos las librerias que podemos necesitar
import inspect
import re
import unittest
import math
import pandas as pd
import código as co
from datetime import datetime, timedelta
from main import *


class Rectangulo(unittest.TestCase):
    def setUp(self):
        pass

    def test_base(self):
        ejex = 3
        ejey = 2
        self.assertEqual(ejex, ejey)

    def test_altura(self):
        ejex = 3
        ejey = 2
        self.assertEqual(ejex, ejey)

    def test_area(self):
        ejex = 3
        ejey = 2
        self.assertEqual(ejex, ejey)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()