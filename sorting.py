#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import collections
import random

class SortAlgorithm(object):
    def __init__(self, vals):
        self.vals = list(vals)
        self.N = len(vals)

        self.xchgs = 0
        self.compares = 0
        pass

    def less(self, e1, e2):
        self.compares = self.compares + 1
        return e1 < e2

    def xchg(self, a, i, j):
        self.xchgs = self.xchgs + 1
        t = a[i]
        a[i] = a[j]
        a[j] = t

    def partition(self, a, lo, hi):
        i = lo
        j = hi + 1
        v = a[lo] # Partitioning item

        while True:
            # Scan left
            while True:
                i = i + 1
                if not self.less(a[i], v) or i == hi:
                    break
            # Scan right
            while True:
                j = j - 1
                if not self.less(v, a[j]) or j == lo:
                    break
            # See if scan is complete
            if i >= j:
                break
            self.xchg(a, i, j)

        self.xchg(a, lo, j)

        # Position of the partitioning item
        return j


    def show(self):
        print(', '.join(str(x) for x in self.vals))

    def is_sorted(self):
        for i in range(1, len(self.vals)):
            if self.less(self.vals[i], self.vals[i-1]):
                return False
        return True

class InsertionSort(SortAlgorithm):
    def sort(self):
        for i in range(0, self.N):
            for j in range(i, 0, -1):
                if not self.less(self.vals[j], self.vals[j-1]):
                    break
                self.xchg(self.vals, j, j-1)

class SelectionSort(SortAlgorithm):
    def sort(self):
        for i in range(0, self.N):
            for j in range(i+1, self.N):
                if not self.less(self.vals[i], self.vals[j]):
                    self.xchg(self.vals, i, j)

class MergeSort(SortAlgorithm):
    def __init__(self, vals):
        super(MergeSort, self).__init__(vals)

    def _merge(self, a, lo, mid, hi):
        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            self.xchgs += 1
            if i > mid:
                a[k] = self.aux[j]
                j = j + 1
            elif j > hi:
                a[k] = self.aux[i]
                i = i + 1
            elif self.less(self.aux[j], self.aux[i]):
                a[k] = self.aux[j]
                j = j + 1
            else:
                a[k] = self.aux[i]
                i = i + 1

class MergeSortTD(MergeSort):
    def __init__(self, vals):
        super(MergeSort, self).__init__(vals)
        self.aux = [None] * self.N

    def sort(self):
        self._sort(self.vals, 0, self.N-1)

    def _sort(self, a, lo, hi):
        if (hi <= lo): return
        mid = lo + (hi - lo)/2
        self._sort(a, lo, mid)
        self._sort(a, mid+1, hi)
        self._merge(a, lo, mid, hi)

class MergeSortBU(MergeSort):
    def __init__(self, vals):
        super(MergeSortBU, self).__init__(vals)
        self.aux = [None] * self.N

    def sort(self):
        self._sort(self.vals, 0, self.N-1)

    def _sort(self, a, lo, hi):
        #print("_sort: ", a)
        sz = 1
        while sz < self.N:
            lo = 0
            while lo < self.N - sz:
                self._merge(a, lo, lo+sz-1, min(lo + 2*sz - 1, self.N - 1))
                #print("after merge of sz = {0}: {1}".format(sz, a))
                #print(a)
                lo += 2*sz
            sz = 2*sz

class QuickSort(SortAlgorithm):
    def sort(self):
        shuffled = list(self.vals)
        random.shuffle(shuffled) # random.shuffle is in-place

        self._sort(shuffled, 0, self.N - 1)

    def _sort(self, a, lo, hi):
        if hi <= lo: return;
        j = self.partition(a, lo, hi)
        self._sort(a, lo, j-1)
        self._sort(a, j+1, hi)
        self.vals = a

def main():
    # Generar arrays de prueba
    import random
    import time

    def genrandom(N):
        return [ random.randrange(0, int(2e+9)) for i in range(N) ]


    t0 = time.time()

    sizes = [10, 30, 70, 1000, 2000, 8000]
    samples = collections.OrderedDict()

    for size in sizes:
        samples[size] = genrandom(size)

    tf = time.time()

    RESULTS_FMT = u'{0:<8} {1}'

    def time_diff(t0, tf):
        return (tf-t0)*1000

    def format_result(label, value):
        value = '{0:.2f} ms'.format(value)
        return RESULTS_FMT.format(label, value)

    print(format_result(u'Random sequence generation time:', time_diff(t0, tf)))
    print()

    def measure_insert(items, stats):
        N = len(items)
        insort = InsertionSort(items)
        t0 = time.time()
        insort.sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': insort.xchgs,
            'compares': insort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_select(items, stats):
        N = len(items)
        selsort = SelectionSort(items)
        t0 = time.time()
        selsort.sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': selsort.xchgs,
            'compares': selsort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_merge(items, stats):
        N = len(items)
        mergesort = MergeSortTD(items)
        t0 = time.time()
        mergesort.sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': mergesort.xchgs,
            'compares': mergesort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_mergebu(items, stats):
        N = len(items)
        mergesort = MergeSortBU(items)
        t0 = time.time()
        mergesort.sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': mergesort.xchgs,
            'compares': mergesort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_quicksort(items, stats):
        N = len(items)
        qsort = QuickSort(items)
        t0 = time.time()
        qsort.sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': qsort.xchgs,
            'compares': qsort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_algorithm(alg_func, label):
        stats = list()
        print(u"Measuring {0}:".format(label))

        for var in samples.values():
            alg_func(var, stats)

        print()

        print(u"{0} stats:".format(label))
        print('{0:<8} {1:<15} {2:<15}'.format('N', 'Exchanges', 'Compares'))

        for stat in stats:
            print('{0:<8} {1:<15} {2:<15}'.format(stat['n'], stat['xchgs'], stat['compares']))


    measure_algorithm(measure_insert, 'insertion sort')

    print()
    measure_algorithm(measure_select, 'selection sort')

    print()
    measure_algorithm(measure_merge, 'merge sort')

    print()
    measure_algorithm(measure_mergebu, 'merge sort (bottom-up)')

    print()
    measure_algorithm(measure_quicksort, 'quicksort')

if __name__ == '__main__': main()
