# Machine Learning Animations

I find visuals, particularly animations, especially useful for understanding how machine learning algorithms work. This repository houses animations that I've developed for teaching purposes.

## Decision Tree

The animation below shows a decision tree being created. For every potential split in the raw data (shown on the left panel), the [Gini impurity](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity) is calculated (right panel). The split resulting in the minimum impurity is selected as the split for the tree, and the process is repeated until all data points have been split into homogenous groups.

![Decision Tree](./gif/decision_tree/decision_tree.gif)

## *k*-Nearest Neighors

The animation below shows the prediction of an unknown point using increasing values of *k* in the *k*-nearest neighbors algorithm. The animation only shows odd values for *k*. In a two-class problem such as that shown, even values of *k* may result in ties, such that a decision would have to be made on how to predict the query point, for example, a random class may be predicted, or the class of the closest point may be predicted.

![kNN](./gif/knn/knn.gif)

## Convolutional Neural Network

### 1D ConvNet

The animation below shows how a 1D sequence (d=1) of 20 observations (T=20) is "broken into" 4 sequences by a 1D convolutional layer with 4 filters (f=4) of length 3. The original input is actually 2D with shape (d=1, T=20). This is a little confusing given that we are working with a "1D ConvNet", but you should think of the 1D as referring to the dimensionality of the filters being passed over the data (not the data itself) - as you can see in the example below, we are passing a 1D filter of length 3 over the data. The output of the 1D convolutional layer is 3D with shape (d=1, f=4, T=20). Note that the ends of the input sequence have been zero-padded to facilitate convolution there. The weights of the filters are just random numbers here, the network has not been trained. There are 16 parameters in the network: (1 input x 4 filters) * (3 weights per filter) + (4 biases) = 16 parameters.

![cnn](./gif/cnn/cnn_1d.gif)
