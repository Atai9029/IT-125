data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:

        numbers.append(i)


numbers.remove(6.13)
letters.reverse()
letters.append(numbers.pop(0))

numbers.insert(1, 2)

del letters[4]
del letters[5]
del letters[6]
del letters[-1]
letters[3] = 'n'
letters.insert(1, 'r')
del letters[-1]

numbers.sort()
print(letters)
print(numbers)
