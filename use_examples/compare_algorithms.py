import random
import timeit

from pop_sort import quick_sort
from pop_sort import selection_sort


randomlist1 = random.sample(range(1, 10000), 1000)
randomlist2 = list(randomlist1)
start = timeit.default_timer()
quick_sort(randomlist1)
stop = timeit.default_timer()
print('Time QuickSort: ', stop - start)

# Timing SelectionSort
start = timeit.default_timer()
selection_sort(randomlist2)
stop = timeit.default_timer()
print('Time SelectionSort: ', stop - start)