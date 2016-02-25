__author__ = 's158079'
import numpy as np
from random import randint
import csv
import math
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
c1 = np.zeros((len(c2),3))
ind = 0
for key1 in c2:
    c1[ind][0] = key1[0]
    c1[ind][1] = key1[1]
    ind += 1

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

k = input("Enter value of k:")

center1 = np.zeros((k,2))
center2 = np.zeros((k,2))

old_center = np.zeros((k,2))
new_center = np.zeros((k,2))

# initialize centers to k random data points
for key in range(0,k,1):
    randnum = randint(0, len(c2))
    old_center[key][0] = c2[randnum][0]
    old_center[key][1] = c2[randnum][1]

print "Initial centers: "
print old_center
c = 0
class1 = np.zeros(len(c2))
class2 = np.zeros(len(c2))
c3 = np.zeros((len(c2),3))
def kMeans(old_center,c):
    index1 = 0
    new_center = np.zeros((k,2))
    for item in c2:
        index2 = 0
        max_distance = distance.euclidean(key_min, key_max)
        for cent in old_center:
            dist = distance.euclidean(item, cent)
            if dist < max_distance:
                max_distance = dist
                class2[index1] = index2
                c1[index1][2] = index2
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
    cost_function = 0
    distance_1 = 0
    index = 0
    for temp1 in c2:
        num = c1[index][2]
        distance_1 = math.pow(distance.euclidean(c2[index], old_center[num]),2)
        index+=1
        cost_function += distance_1
    print(cost_function)
    if temp == k:
        c += 1
    if c == 1:
        return new_center, class2, c1
    else:
        return kMeans(new_center,c)


center1, class1, c3 = kMeans(old_center,c)

print "Final centers:"
print center1

print "Final clusters:"
print class1

# cost_function = 0
# distance_1 = 0
# index = 0
# for temp1 in c2:
#     num = c3[index][2]
#     distance_1 = math.pow(distance.euclidean(c2[index], old_center[num]),2)
#     index+=1
#     cost_function += distance_1
#
# print cost_function

# with open('result_1b_k5_10.csv', 'wt') as fp:
#     a = csv.writer(fp, delimiter=' ')
#     data = c3
#     a.writerows(data)
# c3 contains the data points with their class











