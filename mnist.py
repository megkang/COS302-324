"""MNIST.ipynb

Original file is located at
    https://colab.research.google.com/drive/1jKJY2hIxXcIUHffVoCvRIQwJ-KiT4Eol

#Working with the [MNIST data](https://en.wikipedia.org/wiki/MNIST_database)

Task 1: Principal component analysis
"""

#import packages 
import pickle as pkl
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt 
import math
import matplotlib

#import data 
#reshape from 2000x28x28 tensor of training data to 2000x784 matrix 
#center the data by subtracting off the mean image 
with open('/content/mnist2000.pkl', 'rb') as fh:
  mnist = pkl.load(fh)
training_data = np.reshape(mnist['train_images'], (2000,784))
centered = training_data - np.mean(training_data, axis=0)

#compute a scatter matrix of 784x784 by multiplying data matrix by its transpose
scatter = centered.T @ centered

#compute the eigenvalues and eigenvectors of the scatter matrix 
#plot the eigenvalues in decreasing order 
W, V = npla.eigh(scatter)
plt.plot(W[::-1], '.')
plt.show

#Get the "big" eigenvectors; for each of the top 5 eigenvectors reshape 
#into 28x28 images and render them using imshow 
plt.figure(figsize=(8,2))
for ii in range(5):
  plt.subplot(1,5,ii+1)
  plt.imshow(np.reshape(V[:,-1-ii], (28,28)))

#create low-dimensional representation of the data
#take the 2000 x 784 matrix and multiply it by the top two eigenvectors 
#make a scatter plot of these coordinates 
proj = centered @ V[:,-2:]
plt.plot(proj[:,0],proj[:,1], '.')

#build a scatter plot where the images are rendered instead of the dots 
# Make the projections into [0,1]
proj = proj - np.min(proj, axis=0)
proj = proj / np.max(proj, axis=0)

# Create a 12" x 12" figure.
viz_fig = plt.figure(figsize=(12,12.))

# Get the figure width and height in pixels.
width, height = viz_fig.get_size_inches()*viz_fig.dpi
plt.plot() # Colab seems to require this to render.

# Loop over images.  Could do all 2000 but it's crowded.
for ii in range(400):
  # Render each image in a location on the figure.
  plt.figimage(mnist['train_images'][ii,:,:],
              xo=proj[ii,1]*width,
              yo=(proj[ii,0]*height-150), # hack to make visible
              origin='upper')
