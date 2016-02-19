import numpy as np
from random import randrange, uniform
from scipy.spatial import distance

def load_data_1b(fpath):
    data = []
    f = open(fpath, 'r')
    for line in f:
        words = line.split()
        data.append(words)
    f.close()
    arr = np.array(data, dtype=np.float64)
    return arr[:, 1:]

if __name__ == "__main__":
    c2 = load_data_1b("./data1b/C2.txt")


key_max = np.zeros(2)
key_min = np.zeros(2)
# find the range of the data points
for key in c2:
    if key[0] > key_max[0]:
        key_max[0] = key[0]
    if key[1] > key_max[1]:
        key_max[1] = key[1]
    if key[0] < key_min[0]:
        key_min[0] = key[0]
    if key[1] < key_min[1]:
        key_min[1] = key[1]

#print key_max, key_min

# initialize k random centers
k = 3
center = np.zeros((k,2))
for key in range(0,k,1):
    center[key][0] = uniform(key_min[0], key_max[0])
    center[key][1] = uniform(key_min[1], key_max[1])

#print center
max_distance = distance.euclidean(key_min ,key_max)
q = len(c2)
class1 = np.zeros(q)
index1 = 0
for item in c2:
    index2 = 0
    max_distance = distance.euclidean(key_min ,key_max)
    for cent in center:
        dist = distance.euclidean(item, cent)
        if dist < max_distance:
            max_distance = dist
            class1[index1] = index2
        index2 += 1
    index1 += 1

print class1



