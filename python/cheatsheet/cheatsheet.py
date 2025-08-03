# List

pows_of_two = list(map(lambda x: 2 ** x, range(10)))
print('pows_of_two', pows_of_two)

third_power = pows_of_two[3]
print('third_power', third_power)
odd_pows_of_two = pows_of_two[1 : -1 : 2]
print('odd_pows_of_two', odd_pows_of_two)

pows_of_two += [1024] # OR pows_of_two.append(1024)
pows_of_two += [2048, 4096]  # OR pows_of_two.extend([2048, 4096])
print('pows_of_two', pows_of_two)

some_chars = list('asdbiobdas')
some_chars.sort()
some_chars.reverse()
print('reverse sorted', some_chars)
unsorted_chars = list('asdbiobdas')
sorted_chars = sorted(unsorted_chars)
reversed_unsorted_chars = reversed(unsorted_chars)
print('reverse sorted:', unsorted_chars, reversed_unsorted_chars)

import random
import math
random_tries=10
inf_random_tries = min(map(lambda x: random.random(), range(random_tries)))
sup_random_tries = max(map(lambda x: random.random(), range(random_tries)))
sum_random_tries = sum(map(lambda x: random.random(), range(random_tries)))
mul_random_tries = math.prod(map(lambda x: 1 + random.random(), range(random_tries)))
print(f'largest/least random ({random_tries} tries)', sup_random_tries, inf_random_tries)
print(f'sum of [0, 1]-valued random variables ({random_tries})', sum_random_tries)
print(f'product of [1, 2]-valued random variables ({random_tries})', mul_random_tries)

diagonal_relation = [[x,x] for x in range(10) ]
print('diagonal_relation', diagonal_relation)
# mixture of positional and named args
sorted_by_second = sorted([[x, 10 - x] for x in range(10)], key=lambda x: x[1])
sorted_by_both = sorted([[4, 1], [7, 1], [7, 0], [49, 1]], key=lambda x: [x[0], x[1]])
print('sorted_by_second', sorted_by_second, '\nsorted_by_both', sorted_by_both)

###

# example generator
def foo(c: int): 
  while True:
    yield c
    c += 1
