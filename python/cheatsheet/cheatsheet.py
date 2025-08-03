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
