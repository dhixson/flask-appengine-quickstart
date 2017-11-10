import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).strip('tests'))
# Place import for app here
# i.e "from app.<subpackage>.<file> import <class>"


class Test<_name_>(unittest.TestCase):

    def test_example(self):
        self.assertTrue(True)


if __name__ == '__main__':
    print "<_name_>"
    unittest.main()
