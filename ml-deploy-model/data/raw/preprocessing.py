import pandas as pd
import numpy as np

model_data = pd.get_dummies(pd.read_csv('abalone.csv'),
                            drop_first=True)

model_data[['age']] = model_data[['rings']] + 1
model_data = model_data.drop(columns="rings")
train_data, validation_data = np.split(model_data.sample(
    frac=1, random_state=123), [int(0.8 * len(model_data))])

pd.concat([train_data['age'], train_data.drop(['age'], axis=1)],
          axis=1).to_csv('../abalone_train.csv', index=False, header=False)
pd.concat([validation_data['age'], validation_data.drop(['age'], axis=1)], axis=1).to_csv(
    '../abalone_validation.csv', index=False, header=False)
