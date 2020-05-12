This data is modified after that provided by the UCI Machine Learning Repository, available [here](https://archive.ics.uci.edu/ml/datasets/abalone).

The data has been modified from the original, namely, the "Sex" characteristic has been one-hot-encoded and the "rings" target variable has had +1.5 added to it to represent the abalone age in years. It has been shuffled, one-hot-encoded and split into training and validation sets. The training set has 3341 rows and the validation set has 836 rows.

This preprocessing and splitting can be reproduced using the [build_model.ipynb](../deploy-with-flask/build_model.ipynb) in this repository.
