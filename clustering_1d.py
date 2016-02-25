__author__ = 's158079'
import numpy as np
from random import randint
import csv
from scipy.spatial import distance
import math

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

c1 = np.zeros((len(c2),3))
ind = 0
for key1 in c2:
    c1[ind][0] = key1[0]
    c1[ind][1] = key1[1]
    ind += 1

center1 = np.zeros((k,2))
center2 = np.zeros((k,2))

old_center = np.zeros((k,2))
new_center = np.zeros((k,2))

# initialize first center to first data point

old_center[0][0] = c2[0][0]
old_center[0][1] = c2[0][1]

print "Initial centers: "
print old_center
c = 0
class1 = np.zeros(len(c2))
class2 = np.zeros(len(c2))
c3 = np.zeros((len(c2),3))
def gonZales(old_center,c):
    index3 = 0
    new_center = np.zeros((k,2))
    for item2 in c2:
        index4 = 0
        max_distance = distance.euclidean(key_min, key_max)
        for cent in old_center:
            dist = distance.euclidean(item2, cent)
            if dist < max_distance:
                max_distance = dist
                class2[index3] = index4
                c1[index3][2] = index4
            index4 += 1
            if index4 > c:
                break
        index3 += 1
    cost_function = 0
    index = 0
    max_dist = 0
    for temp1 in c2:
        num = c1[index][2]
        distance_1 = distance.euclidean(c2[index], old_center[num])
        index+=1
        if distance_1 > max_dist:
            max_dist = distance_1
    cost_function = max_dist
    print cost_function
    if c == k-1:
        return old_center,class2, c1
    else:
        c += 1
        index1 = 0
        temp = c-1
        index2 = 0
        min_distance = 0
        for item1 in c2:
            if c1[index2][2] == c-1:
                dist = distance.euclidean(item1, old_center[temp])
                if dist > min_distance:
                    min_distance = dist
                    value = index2
                    old_center[c][0] = c2[value][0]
                    old_center[c][1] = c2[value][1]
            index2 += 1

        return gonZales(old_center,c)

center1, class1, c3 = gonZales(old_center,c)

c4 = np.zeros((len(c2)+k,3))
ind = 0
for key1 in c3:
    c4[ind][0] = key1[0]
    c4[ind][1] = key1[1]
    c4[ind][2] = key1[2]

    ind += 1

print "Final centers:"
print center1

print "Final clusters:"
print class1

counter = len(c2)
keycount = 0
for key5 in old_center:
    c4[counter][0] = old_center[keycount][0]
    c4[counter][1] = old_center[keycount][1]
    c4[counter][2] = k
    counter += 1
    keycount += 1

cost_function = 0
index = 0
max_dist = 0
for temp1 in c2:
    num = c3[index][2]
    distance_1 = distance.euclidean(c2[index], old_center[num])
    index+=1
    if distance_1 > max_dist:
        max_dist = distance_1
cost_function = max_dist
print cost_function

with open('result_1d_k5test.csv', 'wt') as fp:
    a = csv.writer(fp, delimiter=' ')
    data = c4
    a.writerows(data)
# c3 contains the data points with their class


