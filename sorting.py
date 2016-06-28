#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class SortAlgorithm(object):
    def __init__(self, vals):
        self.vals = vals

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
        N = len(self.vals)
        for i in range(0, N):
            for j in range(i, 0, -1):
                if not self.less(self.vals[j], self.vals[j-1]):
                    break
                self.xchg(j, j-1)

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
    tf = time.time()

    RESULTS_FMT = u'{0:<8} {1}'

    def time_diff(t0, tf):
        return (tf-t0)*1000

    def format_result(label, value):
        value = '{0:.2f} ms'.format(value)
        return RESULTS_FMT.format(label, value)

    print(format_result(u'Random sequence generation time:', time_diff(t0, tf)))
    print()

    stats = []

    def measure_insert(items):
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

    print("Measuring insertion sort:")

    measure_insert(s10)
    measure_insert(s30)
    measure_insert(s70)
    measure_insert(s1000)
    measure_insert(s3000)
    measure_insert(s7000)

    print()
    print('{0:<8} {1:<15} {2:<15}'.format('N', 'Exchanges', 'Compares'))

    print("Insertion sort stats:")
    for stat in stats:
        print('{0:<8} {1:<15} {2:<15}'.format(stat['n'], stat['xchgs'], stat['compares']))

if __name__ == '__main__': main()
