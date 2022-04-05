import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):

    searchList = [4,7,12,33,100,345]

    def test_binarysearch(self):
        self.assertEqual(binary_search.binarySearch(TestBinarySearch.searchList, 7), 1)