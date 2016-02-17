__author__ = 's158079'
# Source: http://neuralnetworksanddeeplearning.com/chap1.html
# You need only train and test sets. Simply disregard the validation set.
import numpy as np
import cPickle
import gzip
import math
from itertools import izip
from scipy import spatial

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


cossim = np.zeros(10000)  # change 1000 to new number of test data(if needed)
maxcos = np.zeros(10000)  # change 1000 to new number of test data(if needed)
pred_number = np.zeros(10000)  # change 1000 to new number of test data(if needed)
actual_number = np.zeros(10000)  # change 1000 to new number of test data(if needed)
confusion_matrix = np.zeros((10,10))
correct_predictions = 0
total_predictions = 10000  # change 1000 to new number of test data(if needed)
index1 = 0
index2 = 0
for m in test:
    for n in training:
        cossim[index1] = 1 - spatial.distance.cosine(m[0],n[0]) #  calculates cosine similarity
        if cossim[index1] >= maxcos[index1]:
            maxcos[index1] = cossim[index1]  #  assigns maximum value of cosine similarity
            pred_number[index1] = serialised_to_decimal(training[index2][1])  #  predicted number
            actual_number[index1] = test[index1][1]  # actual number
        index2 += 1
        if index2 == 50000:  # change 5000 to new value of training data (if needed)
            index2 = 0
            break
    # print "Test sample: %d, Actual number: %d, Predicted number: %d" %(index1+1,actual_number[index1], pred_number[index1])
    confusion_matrix[pred_number[index1]][actual_number[index1]] += 1
    if (pred_number[index1] == actual_number[index1]):
        correct_predictions += 1;
    index1 += 1
    if index1 == 10000: #  change 1000 to new value of test data (if needed)
        break


print confusion_matrix
# Calculate sum of each row
row_sum = np.zeros(10)
column_sum = np.zeros(10)
index = 0
for i in confusion_matrix:
    for j in i:
        row_sum[index] += j
    index += 1

transpose_confusion = confusion_matrix.transpose()
index = 0
# calculate sum of each column
for i in transpose_confusion:
    for j in i:
        column_sum[index] += j
    index += 1

# calculate precision and recall for each number
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

print row_sum
print column_sum