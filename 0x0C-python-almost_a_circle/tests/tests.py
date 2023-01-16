#!/usr/bin/python3

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test(unittest.TestCase):
    """Unittests for testing my code."""

    def test1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
        
if __name__ == "__main__":
    unittest.main()
