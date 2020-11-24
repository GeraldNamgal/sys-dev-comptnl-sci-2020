#!/usr/bin/env python3

from P3 import *
from matplotlib import pyplot as plt

ns = (0, 10, 20, 50, 100, 200, 500)  # TODO: Define the lists sequence -- any changes needed?

npq_lists = timeit(ns, pqclass=NaivePriorityQueue)
print(npq_lists)
hpq_lists = timeit(ns, pqclass=HeapPriorityQueue)
print(hpq_lists)
ppq_lists = timeit(ns, pqclass=PythonHeapPriorityQueue)
print(ppq_lists)

# TODO: What graphs should look like -- https://piazza.com/class/kc57xuuysdm64b?cid=473

# TODO: Graphs -- Clean this up more and stuff
# Plot the results (Elapsed Time vs. ns)
plt.plot(ns, npq_lists, label='npq')
plt.plot(ns, hpq_lists, label='hpq')
plt.plot(ns, ppq_lists, label='ppq')
plt.title('Elapsed Time Vs. np for 3 Priority Queues')
plt.xlabel('ns')
plt.ylabel('Elapsed Time')
plt.legend()
plt.show()
