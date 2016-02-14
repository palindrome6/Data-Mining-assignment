# Source: http://neuralnetworksanddeeplearning.com/chap1.html
# You need only train and test sets. Simply disregard the validation set.
import numpy as np
import cPickle
import gzip
import math
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
# def serialised_to_decimal(dataResult):
#     index1 = 0
#     for i in dataResult:
#         if i == 1:
#             return index1
#         index1 += 1
#
#
# rowSize = 784
# numberList = np.zeros((10, rowSize))
# countNumberList = np.zeros(10)
#
# for row in training:
#     decimalResult = serialised_to_decimal(row[1])
#     if decimalResult != -1:
#         index2 = 0
#         for pixel in row[0]:
#             numberList[decimalResult][index2] += pixel
#             index2 += 1
#
#         countNumberList[decimalResult] += 1
#
#
# index3 = 0
# for number in numberList:
#     for pixel in number:
#         pixel = pixel/countNumberList[index3]
#         if pixel > 1:
#             print "Error"
#     # print ("Number")
#     # print (index3)
#     # print (":")
#     # print (number)
#     index3 += 1
#
# # sumc = 0
# # for count in countNumberList:
# #     sumc += count
# #     print count
# # print sumc
#
# cossim = np.zeros((10000,10))
# maxcos = np.zeros(10000)
#
# index1 = 0
# index2 = 0
# for m in test:
#     for n in numberList:
#         numerator = 0
#         denom1 = 0
#         denom2 = 0
#         for (i,k) in izip(m[0],n):
#             numerator += i*k
#             denom1 += i*i
#             denom2 += k*k
#         if (denom1 != 0 and denom2 != 0):
#             cossim[index1][index2] =  numerator/(math.sqrt(denom1)*math.sqrt(denom2))
#         if cossim[index1][index2] >= maxcos[index1]:
#             maxcos[index1] = cossim[index1][index2]
#         index2 += 1
#     index2 = 0
#     index1 += 1
#
# print cossim[0]
# print cossim[1]
# print cossim[2]
# print cossim[3]
# print cossim[4]
# print cossim[5]
# print cossim[6]
# print cossim[7]
# print cossim[8]
# print cossim[9]
# print cossim[10]
# print cossim[11]

print test[0][1]
print test[1][1]
print test[2][1]
print test[3][1]
print test[4][1]
print test[5][1]
print test[6][1]
print test[7][1]
print test[8][1]
print test[9][1]
print test[10][1]
print test[11][1]




