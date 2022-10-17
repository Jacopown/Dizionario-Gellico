import random

dictionary = []

with open('dizionarioGellico.txt') as f:
    [dictionary.append(str(line)) for line in f.read().splitlines()]

a, b, c = random.sample(range(0, len(dictionary)-1), 3)

print(dictionary[a] + ' ' + dictionary[b] + ' ' + dictionary[c])
