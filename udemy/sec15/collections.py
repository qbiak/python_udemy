from collections import Counter
from collections import defaultdict

l = [1, 1, 2, 3, 2, 1, 3, 4, 65, 13, 1, 698, 1, 13, 2, 4, 69, 13, 549, 84, 31, 41, 4, 31, 1, 4, 1, 1]

# count occurrences
counted = Counter(l)
print(counted)

d = {}
d['one']

d1 = defaultdict(object)