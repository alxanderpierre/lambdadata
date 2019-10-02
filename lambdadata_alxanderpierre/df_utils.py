"""
utility funchtions for working with DataFrames
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def null(X):
  null_list = X.isnull().sum()
  return null_list




def split(df):
    train, test =  train_test_split(df, train_size=.75)
    train, val = train_test_split(train, train_size=.75)
    print(train, test, val)
    print(train.shape, test.shape, val.shape)




def dropcol(df):
    df = df.copy()
    df= df.drop(columns=[drop_clomuns])
    return df
