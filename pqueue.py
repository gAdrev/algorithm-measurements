#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import collections
import random

class MaxPQ(object):
    def __init__(self, maxN):
        self.maxN = maxN
        self.N = 0
        self.pq = [None for i in range(maxN+1)]

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, v):
        self.N = self.N + 1
        self.pq[self.N] = v
        self.swim(self.N)

    def delMax(self):
        max = self.pq[1]

        self.xchg(1, self.N)
        self.N = self.N - 1

        self.pq[self.N+1] = None
        self.sink(1)

        return max

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def xchg(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t

    def swim(self, k):
        while k > 1 and self.less(k/2, k):
            self.xchg(k/2, k)

    def sink(self, k):
        while 2*k <= self.N:
            j = 2*k
            if j < self.N and self.less(j, j+1):
                j = j + 1
            if not self.less(k, j):
                break
            self.xchg(k, j)
            k = j


def main():
    # Generar arrays de prueba
    import random
    import time

    # pq1 = MaxPQ()

    def genrandom(N):
        return [ random.randrange(0, int(2e+9)) for i in range(N) ]

    t0 = time.time()

    sizes = [10, 30, 70, 1000, 2000, 8000, 20000, 80000, 200000, 1000000]
    samples = collections.OrderedDict()

    for size in sizes:
        samples[size] = genrandom(size)

    tf = time.time()
    print("Random samples generation time:", tf-t0)

    t0 = time.time()
    queues = collections.OrderedDict()
    for size in sizes:
        queues[size] = MaxPQ(size)
    tf = time.time()
    print("PQueue allocation time:", tf-t0)

    for size, pqueue in queues.iteritems():
        tbuild0 = time.time()
        for val in samples[size]:
            pqueue.insert(val)
        tbuildf = time.time()
        print("size:", size, "time:", tbuildf-tbuild0)


    pass

if __name__ == '__main__': main()
