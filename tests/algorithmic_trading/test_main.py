import unittest
from src.algorithmic_trading.main import *


class ShouldReturnHehe(unittest.TestCase):

    def test_shouldReturnHehe(self):
        result = start()
        self.assertEquals(result, "Hehe")
