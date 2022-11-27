#https://github.com/Foxhead-Studio/SSW

import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    return df

def dataset_stat(dataset_df):
    #count the number of 'target' column data and cast it as list
    target_num_list = list(data_df['target'].value_counts())
    
    #index 0 means number of zeros, and index 1 means number of ones
    n_class0 = target_num_list[0]
    n_class1 = target_num_list[1]
    
    #drop out last index 'target' so that we can make x_dataset
    #wich only contains cause columns
    x_dataset_df = dataset_df.drop(["target"], axis = 1)
    n_feats = len(x_dataset_df.columns)
    return n_feats, n_class0, n_class1

def split_dataset(dataset_df, testset_size):
    #drop 'target' column and make it to numpy data so that scikit learn can use of it.
    x_data = dataset_df.drop(['target'], axis = 1)
    x_data = x_data.to_numpy()
    
    #split only 'target' column and make it to data frame and cast to numpy array.
    y_data = data_df.loc[:,'target']
    y_data = pd.DataFrame(y_data)
    y_data = y_data.to_numpy()
    
    #squeeze the dimension 2 to 1
    y_data = np.squeeze(y_data, axis = 1)
    
    #split data using scikit learn,
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.1)
    return x_train, x_test, y_train, y_test

if __name__ == '__main__':
    data_path = 'default_credit_card.csv'
    data_df = load_dataset(data_path)
    
    n_feats, n_class0, n_class1 = dataset_stat(data_df)
    print ("Number of features: ", n_feats)
    print ("Number of class 0 data entries: ", n_class0)
    print ("Number of class 1 data entries: ", n_class1)
    
    print ("\nSplitting the dataset with the test size of ", float(sys.argv[2]))
    x_train, x_test, y_train, y_test = split_dataset(data_df, float(sys.argv[2]))
    
    
    
    
