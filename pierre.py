def null(X):
  null_list = X.isnull().sum()
  return null_list
