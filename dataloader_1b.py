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

# print key_max, key_min

# initialize k random centers
k = 2
center1 = np.zeros((k,2))
center2 = np.zeros((k,2))

old_center = np.zeros((k,2))
new_center = np.zeros((k,2))
# for key in range(0,k,1):
#     old_center[key][0] = uniform(key_min[0], key_max[0])
#     old_center[key][1] = uniform(key_min[1], key_max[1])
for key in range(0,k,1):
    old_center[key][0] = c2[key][0]
    old_center[key][1] = c2[key][1]


print old_center
c = 0
class1 = np.zeros(len(c2))
class2 = np.zeros(len(c2))
def kMeans(old_center,c):
    index1 = 0
    for item in c2:
        index2 = 0
        max_distance = distance.euclidean(key_min, key_max)
        for cent in old_center:
            dist = distance.euclidean(item, cent)
            if dist < max_distance:
                max_distance = dist
                class2[index1] = index2
            index2 += 1
        index1 += 1
    index = 0
    countnumb = np.zeros(k)
    for key in c2:
        for numb in range(0, k, 1):
            if class2[index] == numb:
                new_center[numb][0] += key[0]
                new_center[numb][1] += key[1]
                countnumb[numb] += 1
        index += 1
    for numb in range(0, k, 1):
        new_center[numb][0] /= countnumb[numb]
        new_center[numb][1] /= countnumb[numb]
    temp = 0
    for numb in range(0, k, 1):
        if new_center[numb][0] == old_center[numb][0] and new_center[numb][1] == old_center[numb][1]:
            temp += 1
    if temp == k:
        c += 1
    if c == 10:
        return new_center, class2
    else:
        old_center = new_center
        return kMeans(old_center,c)


center1, class1 = kMeans(old_center,c)

print center1, class1










