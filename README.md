# COS302-324
Code for Princeton COS302 & 324: math for machine learning and intro to machine learning 

__nyt.py__

- In this assignment we used singular value decomposition (SVD) on a small subset of NyTimes articles. We used bag of words representation in which documents are represented by the counts of words, excluding common stop words. 
- We did this through finding the term frequency-inverse document frequency (TF-IDF), or the number of times word *n* appeared in document *m* (TF) multiplied by the natural log of the number of documents divided by the number of documents in which word *m* appears (IDF). 
- Then we took the SVD of the TF-IDF matrix and plotted the singular values in descending order. 
- For each of the top 20 right singular vectors which represented interesting topical dimensions, we identified the words in that were most common. 

__mnist.py__

- In this assignment we conducted principal component analysis (PCA) on the MNIST data. PCA enables us to represent high-dimensional data in a low-dimensional way by identifying important directions in the data. PCA does this by computing the covariance matrix of the data and then looking at the the eigenvectors of it that correspond to the largest eigenvectors. 
