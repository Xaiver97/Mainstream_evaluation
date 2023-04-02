import numpy as np
import pandas as pd
import pickle
import copy

datasets = ['BookCrossing', 'Epinions', 'LFM360K', 'ML1M', 'ML20M', 'Yelp']
data_statistic = dict()
for dataset in datasets:
    df = pd.read_csv(f'../mod_data/{dataset}/{dataset}.csv', sep=',', names=['userId', 'itemId'] , skiprows=1)
    print("Dataset : ", dataset)
    user_cnt = len(df['userId'].unique())
    item_cnt = len(df['itemId'].unique())
    data_statistic[dataset] = [user_cnt, item_cnt]
    print("total user: ", user_cnt)
    print("total item: ", item_cnt)
    print("total Interactions" ,len(df))
    print('sparsity: ' + str(len(df) * 1.0 / (user_cnt * item_cnt)))
    print("-------------------------------------------------------")
with open('../mod_data/data_statistic.pkl', 'wb') as f:
    pickle.dump(data_statistic, f)
    print('data_statistic.pkl has been generated')