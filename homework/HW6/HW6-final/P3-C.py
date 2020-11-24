#!/usr/bin/env python3

from P3 import *
from matplotlib import pyplot as plt

# TODO: Define the lists sequence -- any changes needed?
ns = (0, 10, 20, 50, 100, 200, 500)

npq_lists = timeit(ns, pqclass=NaivePriorityQueue)
print(npq_lists)
hpq_lists = timeit(ns, pqclass=HeapPriorityQueue)
print(hpq_lists)
phpq_lists = timeit(ns, pqclass=PythonHeapPriorityQueue)
print(phpq_lists)

# TODO: Graphs -- Clean this up more and stuff?
# Plot the results (Elapsed Time vs. ns)
plt.plot(ns, npq_lists, label='Naive Priority Queue')
plt.plot(ns, hpq_lists, label='Heap Priority Queue')
plt.plot(ns, phpq_lists, label='Python Heap Priority Queue')
plt.title('Elapsed Time Vs. \'ns\' for Three Priority Queues')
plt.xlabel('ns (# of Lists Merged)')
plt.ylabel('Elapsed Time (Seconds)')
plt.legend()
plt.show()
