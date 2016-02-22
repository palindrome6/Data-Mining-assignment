This archive contains the data and useful scripts for Set1 homeworks.

It contains the MNIST data set that was downloaded from the e-book by Michael Nielsen: [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/chap1.html). The dataset description and the dataset in its original formal can be found at [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/).  

The corresponding code for loading the data is located in "**mnist_dataloader.py**".  It allows you load and manipulate data much faster.

"**mnist_dataloader_5.py**" containes an implementation of the nearest neighbor classifier using cosine distance. 50000 training samples and 10000 test samples are used and the resultant confusion matrix, presicion and recall values are calculated. 

To read data sets for the assignment 1b you can use the script "**dataloader_1b.py**".   

"**clustering_1a.py**" and "**clustering_1b**" contains implementations of k-means algorithm with different initializations.

"**clustering_1c.py**" contains an implementation of k-means++.

"**clustering_1d.py**" contains an implementation of Gonzales'algorithm.
