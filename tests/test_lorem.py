#!/usr/bin/env python

"""
test_lorem
----------

Tests for the `lorem` module.
"""


import unittest

import lorem


class TestLorem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sentence_001(self):
        self.assertTrue(lorem.sentence()[0].isupper())

    def test_sentence_002(self):
        self.assertEqual(lorem.sentence()[-1], '.')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
