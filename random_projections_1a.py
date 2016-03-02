__author__ = 's158079'
# Source: http://neuralnetworksanddeeplearning.com/chap1.html
# You need only train and test sets. Simply disregard the validation set.
import numpy as np
import cPickle
import gzip
import math
import csv
import random
from scipy.spatial import distance
from itertools import izip

def load_data():
    f = gzip.open('./data1a/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = cPickle.load(f)
    f.close()
    return training_data, validation_data, test_data


def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def load_data_wrapper():
    tr_d, va_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return training_data, validation_data, test_data

[training, validation, test] = load_data_wrapper()

# test_data1 = np.zeros((len(test),784))
# num1 = 0
# for item1 in test:
#     num2 = 0
#     for item2 in item1:
#         test_data1[num1][num2] = test[num1][0][num2]
#         num2 += 1
#     num1 += 1
#
# print "First test data:"
# print test_data1[0]

# Length of each training data
d_length = len(test[0][0])
print "Length of each test data:"
print d_length

k = input("Enter value of k:")
value = float(1/(math.sqrt(d_length)))
foo = [value, -value]
d_matrix = np.zeros((k,d_length))
row = 0
for item1 in d_matrix:
    column = 0
    for item2 in item1:
        d_matrix[row][column] = random.choice(foo)
        column += 1
    row += 1

print "Length of d matrix:"
print len(d_matrix)

new_training_data = np.zeros((20, d_length))

print len(new_data1[0])
count = 0
for item in test:
    for item2 in range(0,784,1):
        new_data1[count][item2] = test[count][0][item2]
    count += 1
    if count == 20:
        break



new_data1 = new_data1.transpose()

result_array = np.dot(d_matrix, new_data1)
result_array = result_array.transpose()
arr = np.zeros((190,3))
count = 0
print len(result_array[0])
for item1 in range(0,20,1):
    for item2 in range(item1+1,20,1):
        dist_num = distance.euclidean(result_array[item1],result_array[item2])
        dist_den = distance.euclidean(test[item1][0],test[item2][0])
        arr[count][1] = dist_num/dist_den
        arr[count][0] = count
        arr[count][2] = k
        count += 1
        print arr
count = 0
sum1 = 0
for item in arr:
    sum1 += arr[count]
    count += 1
print sum1

# temp1 = np.zeros((d_length, 1))
# temp2 = np.zeros((1,k))
# count1 = 0
# for item1 in test:
#     count2 = 0
#     for item2 in range(0,784,1):
#         temp1[item2] = test[count2][0][item2]
#         count2 += 0
#     temp2 = np.dot(d_matrix,temp1)
#     temp2 = temp2.transpose()
#     new_data1[count1] = temp2
#     count1 += 1
#     if count1 == 20:
#         break
# count = 0
# for item in new_data1:
#     print "Data", count
#     print new_data1[count]
#     count += 1
# # dist_array = np.zeros((20,20))
# # count = 0
# # for i in range(0,20,1):
# #     for j in range(i+1,20,1):
# #         dist_array[i][j] = spatial.distance.euclidean(training[])

with open('result00', 'at') as fp:
    a = csv.writer(fp, delimiter=' ')
    data = arr
    a.writerows(data)
