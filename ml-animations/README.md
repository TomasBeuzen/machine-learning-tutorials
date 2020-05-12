# Machine Learning Animations

I find visuals, particularly animations, especially useful for understanding how machine learning algorithms work. This repository houses animations that I've developed for teaching purposes.

### Decision Tree

The animation below shows a decision tree being created. For every potential split in the raw data (shown on the left panel), the [Gini impurity](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity) is calculated (right panel). The split resulting in the minimum impurity is selected as the split for the tree, and the process is repeated until all data points have been split into homogenous groups.

![Decision Tree](./gif/decision_tree/decision_tree.gif)

### *k*-Nearest Neighors

The animation below shows the prediction of an unknown point using increasing values of *k* in the *k*-nearest neighbors algorithm. The animation only shows odd values for *k*. In a two-class problem such as that shown, even values of *k* may result in ties, such that a decision would have to be made on how to predict the query point, for example, a random class may be predicted, or the class of the closest point may be predicted.

![kNN](./gif/knn/knn.gif)