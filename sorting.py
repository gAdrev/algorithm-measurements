#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

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

    def xchg(self, i, j):
        self.xchgs = self.xchgs + 1
        t = self.vals[i]
        self.vals[i] = self.vals[j]
        self.vals[j] = t

    def show(self):
        print(', '.join(str(x) for x in self.vals))

    def is_sorted(self):
        for i in range(1, len(self.vals)):
            if self.less(self.vals[i], self.vals[i-1]):
                return False
        return True

class InsertionSort(SortAlgorithm):
    def insert_sort(self):
        for i in range(0, self.N):
            for j in range(i, 0, -1):
                if not self.less(self.vals[j], self.vals[j-1]):
                    break
                self.xchg(j, j-1)

class SelectionSort(SortAlgorithm):
    def selection_sort(self):
        for i in range(0, self.N):
            for j in range(i+1, self.N):
                if not self.less(self.vals[i], self.vals[j]):
                    self.xchg(i, j)

class MergeSort(SortAlgorithm):
    def __init__(self, vals):
        super(MergeSort, self).__init__(vals)
        self.aux = [None] * self.N

    def _merge(self, a, lo, mid, hi):
        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            self.aux[k] = a[k]

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = a[j]
                j = j + 1
            elif j > hi:
                a[k] = a[i]
                i = i + 1
            elif self.less(self.aux[j], self.aux[i]):
                a[k] = a[j]
                j = j + 1
            else:
                a[k] = a[i]
                i = i + 1

    def merge_sort(self):
        self._merge_sort(self.vals, 0, self.N-1)

    def _merge_sort(self, a, lo, hi):
        if (hi <= lo): return
        mid = lo + (hi - lo)/2
        self._merge_sort(a, lo, mid)
        self._merge_sort(a, mid+1, hi)
        self._merge(a, lo, mid, hi)

def main():
    # Generar arrays de prueba
    import random
    import time

    def genrandom(N):
        return [ random.randrange(0, int(2e+9)) for i in range(N) ]


    t0 = time.time()

    s10 = genrandom(10)
    s30 = genrandom(30)
    s70 = genrandom(70)
    s1000 = genrandom(1000)
    s3000 = genrandom(3000)
    s7000 = genrandom(7000)
    s500000 = genrandom(500000)

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
        insort.insert_sort()
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
        selsort.selection_sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': selsort.xchgs,
            'compares': selsort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_merge(items, stats):
        N = len(items)
        mergesort = MergeSort(items)
        t0 = time.time()
        mergesort.merge_sort()
        tf = time.time()

        stats.append({
            'n': N,
            'xchgs': mergesort.xchgs,
            'compares': mergesort.compares
        })

        print(format_result(u'{0}'.format(N), time_diff(t0, tf)))

    def measure_algorithm(alg_func, label):
        stats = list()
        print(u"Measuring {0}:".format(label))

        for var in [s10, s30, s70, s1000, s3000, s7000, s500000]:
        #for var in [s10, s30, s70, s1000, s3000]:
            alg_func(var, stats)

        print()

        print(u"{0} stats:".format(label))
        print('{0:<8} {1:<15} {2:<15}'.format('N', 'Exchanges', 'Compares'))

        for stat in stats:
            print('{0:<8} {1:<15} {2:<15}'.format(stat['n'], stat['xchgs'], stat['compares']))


#    measure_algorithm(measure_insert, 'insertion sort')
#
#    print()
#    measure_algorithm(measure_select, 'selection sort')

    print()
    measure_algorithm(measure_merge, 'merge sort')



if __name__ == '__main__': main()
