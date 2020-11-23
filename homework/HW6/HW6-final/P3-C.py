#!/usr/bin/env python3

from P3 import *


lists = timeit(pqclass=NaivePriorityQueue)
print(lists)
lists = timeit(pqclass=HeapPriorityQueue)
print(lists)
lists = timeit(pqclass=PythonHeapPriorityQueue)
print(lists)
