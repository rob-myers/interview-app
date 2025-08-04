# List

pows_of_two = list(map(lambda x: 2 ** x, range(10)))
print('pows_of_two', pows_of_two)

print('third_power', pows_of_two[3])
print('odd_pows_of_two', pows_of_two[1 : -1 : 2])

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

import itertools
print('elementwise_sum', [sum(x) for x in zip(range(5), range(5))])
print('diagonal_relation', [[x,x] for x in range(10) ])
# mixture of positional and named args
sorted_by_second = sorted([[x, 10 - x] for x in range(10)], key=lambda x: x[1])
sorted_by_both = sorted([[4, 1], [7, 1], [7, 0], [49, 1]], key=lambda x: [x[0], x[1]])
print('sorted_by_second', sorted_by_second, '\nsorted_by_both', sorted_by_both)
print('flattened_list', list(itertools.chain.from_iterable([[1, 2], [3, 4]])))

print(
  f'length_of_list: {len(list("abc"))}',
  f'length_of_string {len("abc")}',
  f'number_of_occurrences (a) {[1, 3, 3, 1].count(3)}',
  f'number_of_occurrences (b) {"the quick brown fox jumped over the lazy dog".count("o")}',
  f'number_of_occurrences (c) {"the quick brown fox jumped over the lazy dog".count("the")}',
  f'number_of_occurrences (d) {[[1,2],[1,2]].count([1,2])}',
  f'number_of_occurrences (d) {[[1,2],[1,2]].count([1,2])}',
  f'index_of_el (a) {[1,2,3].index(3)}',
  f'index_of_el (a) {"abcefghijk".index("fg")}',
  sep='\n'
)
els = list(range(5))
print(f'el_popped: {els.pop()}')
some_random_numbers = list(map(lambda x: random.random(), range(6)))
some_random_numbers.insert(3, 42)
print('inserted_42_in_middle', some_random_numbers)
some_random_numbers.remove(42)
print('removed_42_from_list', some_random_numbers)
some_random_numbers.clear()
print('cleared_list', some_random_numbers)

# Dictionary

import collections
ages_dict = { 'rob': 42, 'will': 50, 'kate': 52 }

view_ages_keys = ages_dict.keys()
view_ages_values = ages_dict.values()
view_ages_items = ages_dict.items()

ages_dict.get('june')
ages_dict.get('june', 100)
ages_dict.setdefault('june', 100) # strict complains if 2nd omitted
ages_dict.pop('june')
print(f'ages: keys {ages_dict.keys()}, values {ages_dict.values()}, items {ages_dict.items()}')
a_default_dict: dict[int, int] = collections.defaultdict(lambda: 42)
a_default_dict[0] = 1
print('a_default_dict default value', a_default_dict[1])

dict_from_key_values = dict(zip(range(5), range(5)))
dict_from_keys = dict.fromkeys(range(5), 42)

ages_dict.update({ 'rob': -1 })
print('merged_ages_dict', ages_dict)
ages_dict.pop("rob")
ages_dict.update({ "rob": 42, "faris": 41, "nick": 41, "lewis": 42 })
# 🔔
print('keys_with_value_42', [k for k, v in ages_dict.items() if v == 42])
print('a_filtered_dict', {k: v for k, v in ages_dict.items() if v == 42})

# Counter 🚧


###

# example generator
def foo(c: int): 
  while True:
    yield c
    c += 1
