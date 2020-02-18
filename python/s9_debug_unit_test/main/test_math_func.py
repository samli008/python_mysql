import sys
del sys.path[0]
sys.path.append('/root/git/python_mysql/python/s9_debug_unit_test')

import unittest
from main.math_func import add

class TestAdd(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(1,2),3)
    self.assertEqual(add(10,2),12)

  def test_add_again(self):
    self.assertEqual(add(11,22),33)

  def test_add_exception(self):
    self.assertRaises(ValueError,add,'a',1)

if __name__ == "__main__":
    unittest.main() 
