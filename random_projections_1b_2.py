# Source: http://neuralnetworksanddeeplearning.com/chap1.html
# You need only train and test sets. Simply disregard the validation set.
import numpy as np
import cPickle
import gzip
import math
import random
from scipy.spatial import distance
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
p = input("Enter the number of test samples (0-10000) :")
q = input("Enter the number of training samples (0- 50000) :")

d_length = len(test[0][0])

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


def serialised_to_decimal(dataResult):
    index1 = 0
    for i in dataResult:
        if i == 1:
            return index1
        index1 += 1

new_training_data = np.zeros((q, d_length))
training_data_num = np.zeros((q, 1))
new_test_data = np.zeros((p, d_length))
test_data_num = np.zeros((p, 1))

count = 0
for item1 in training:
    training_data_num[count] = serialised_to_decimal(training[count][1])
    for item2 in range(0,784,1):
        new_training_data[count][item2] = training[count][0][item2]
    count += 1
    if count == q:
        break


count = 0
for item1 in test:
    test_data_num[count] = test[count][1]
    for item2 in range(0,784,1):
        new_test_data[count][item2] = test[count][0][item2]
    count += 1
    if count == p:
        break


new_training_data_transpose = new_training_data.transpose()
new_test_data_transpose = new_test_data.transpose()

training_matrix = np.dot(d_matrix, new_training_data_transpose)
test_matrix = np.dot(d_matrix, new_test_data_transpose)
training_matrix = math.sqrt(d_length/k)* training_matrix
test_matrix = math.sqrt(d_length/k)* test_matrix
training_matrix_transpose = training_matrix.transpose()
test_matrix_transpose = test_matrix.transpose()

maxcos = np.zeros(p)  # used to store maximum cosine similarity
cossim = np.zeros(p)  # used to store cosine similarity
count = 0
for item in maxcos:
    maxcos[count] = 9999999
    count += 1


pred_number = np.zeros(p)  # Stores predicted digit for a test data
actual_number = np.zeros(p)  # Stores the actual digit of thr test data
confusion_matrix = np.zeros((10,10))
index1 = 0
index2 = 0
for m in test_matrix_transpose:
    for n in training_matrix_transpose:
        cossim[index1] = distance.euclidean(m,n) #  calculates cosine similarity
        if cossim[index1] <= maxcos[index1]:
            maxcos[index1] = cossim[index1]  #  assigns maximum value of cosine similarity
            pred_number[index1] = training_data_num[index2]  #  predicted digit
            actual_number[index1] = test_data_num[index1]  # actual digit
        index2 += 1
        if index2 == q:
            index2 = 0
            break
    confusion_matrix[pred_number[index1]][actual_number[index1]] += 1
    index1 += 1
    if index1 == p: #  change 1000 to new value of test data (if needed)
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
#Calculate transpose
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

