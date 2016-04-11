import unittest

from .. import utils


class UtilsTests(unittest.TestCase):
    
    
    def test_translate(self):
        
        cases = [
            ('hallo', 'hello'),
            ('bobo', 'bobo')
        ]
        
        for s, expected in cases:
            self.assertEqual(utils.translate(s), expected)
