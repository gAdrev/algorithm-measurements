import unittest

import sorting

sample = [9, -3, 8, 5, 1, 0, -2, 4, 1]
expected = [-3, -2, 0, 1, 1, 4, 5, 8, 9]

class TestSorting(unittest.TestCase):
    def test_insertsort(self):
        insort = sorting.InsertionSort(sample)
        insort.sort()

        self.assertTrue(insort.is_sorted())
        self.assertEqual(expected, insort.vals)

    def test_selectiontsort(self):
        s = sorting.SelectionSort(sample)
        s.sort()

        self.assertTrue(s.is_sorted())
        self.assertEqual(expected, s.vals)

    def test_mergesort(self):
        ms = sorting.MergeSort(sample)
        ms.sort()

        self.assertTrue(ms.is_sorted())
        self.assertEqual(expected, ms.vals)

if __name__ == '__main__':
    unittest.main()
