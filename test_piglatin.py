import unittest
import piglatin

class Test(unittest.TestCase):
  def test_to_piglatin(self):
    self.assertAlmostEqual(piglatin.to_piglatin('happy'),'appyhay')
    self.assertAlmostEqual(piglatin.to_piglatin('egg'),'eggay')

unittest.main()
