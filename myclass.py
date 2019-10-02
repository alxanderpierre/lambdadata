import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

ONES = pd.DataFrame(np.ones(10))
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})

class MyClass:

    def __init__(self,df):
        self.df = df
        self.x = 1



    def null(self):
        null_list = self.df.isnull().sum()
        return null_list

    def dropcol(self, drop_clomuns):
        df = self.df.drop(columns=drop_clomuns)
        return df

    def split(self):
        train, test = train_test_split(self.df, train_size=.75)
        train, val = train_test_split(train, train_size=.75)
        print(train.shape, test.shape, val.shape)
        return (train, test, val)
