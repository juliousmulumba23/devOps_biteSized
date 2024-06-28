from collections import Counter, defaultdict
import pdb


my_list = [1,1,1,1,1,1,1,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,3,2,2,2,2,2,4,5,5,5,5,5,5,6,6,6,6,6,5,5,5,5,4,4,4]

k = Counter(my_list)

print(k.most_common(2))

print(list(k))

d = defaultdict(lambda: 0)

#d = {'age':24, 'height':6, 'color':'black'}

print(d['colored'])

str(10)