__author__ = 's158079'
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

def serialised_to_decimal(dataResult):
    index1 = 0
    for i in dataResult:
        if i == 1:
            return index1
        index1 += 1


cossim = np.zeros(100)
maxcos = np.zeros(100)
pred_number = np.zeros(100)
actual_number = np.zeros(100)
confusion_matrix = np.zeros((10,10))
correct_predictions = 0
total_predictions = 100
index1 = 0
index2 = 0
for m in test:
    for n in training:
        numerator = 0
        denom1 = 0
        denom2 = 0
        for (i,k) in izip(m[0],n[0]):
            numerator += i*k
            denom1 += i*i
            denom2 += k*k
        if (denom1 != 0 and denom2 != 0):
            cossim[index1] =  numerator/(math.sqrt(denom1)*math.sqrt(denom2))
        if cossim[index1] >= maxcos[index1]:
            maxcos[index1] = cossim[index1]
            pred_number[index1] = serialised_to_decimal(training[index2][1])
            actual_number[index1] = test[index1][1]
        index2 += 1
        if index2 == 1000:
            index2 = 0
            break
    #print "Test sample: %d, Actual number: %d, Predicted number: %d" %(index1+1,actual_number[index1], pred_number[index1])
    confusion_matrix[pred_number[index1]][actual_number[index1]] += 1
    if (pred_number[index1] == actual_number[index1]):
        correct_predictions += 1;
    index1 += 1
    if index1 == 100:
        break

precision_x = (float(correct_predictions)/float(total_predictions))

print confusion_matrix

row_sum = np.zeros(10)
column_sum = np.zeros(10)
index = 0
for i in confusion_matrix:
    for j in i:
        row_sum[index] += j
    index += 1


transpose_confusion = confusion_matrix.transpose()
index = 0
for i in transpose_confusion:
    for j in i:
        column_sum[index] += j
    index += 1

precision = np.zeros(10)
recall = np.zeros(10)
index = 0
for i in confusion_matrix:
    if row_sum[index] != 0:
        precision[index] = (float(confusion_matrix[index][index])/float(row_sum[index]))
        print "Precision of %d : %f" %(index, precision[index])
    if  column_sum[index] != 0:
        recall[index] = float(confusion_matrix[index][index])/float(column_sum[index])
        print "Recall of %d : %f" %(index, recall[index])
    index += 1

