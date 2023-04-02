import numpy as np
import pandas as pd
import pickle
import copy
from tqdm import tqdm
import matplotlib.pyplot as plt

datasets = ['BookCrossing', 'Epinions', 'LFM360K', 'ML1M', 'ML20M', 'Yelp']


for dataset in datasets:
    print("Now visualize the dataset: ", dataset)
    df = pd.read_csv(f'../../mod_data/{dataset}/{dataset}.csv', sep=',', names=['userId', 'itemId'] , skiprows=1)
    item_cnt = len(df['itemId'].unique())
    item_pop = list()
    item_dict = dict.fromkeys(range(item_cnt), 0)
    for i in df.iterrows():
        item_dict[i[1][1]] += 1
    for i in range(item_cnt):
        item_pop.append(item_dict[i])
    item_pop.sort()
    item_pop.reverse()
    plt.cla()
    plt.grid(linestyle="--")
    plt.xlabel("item rank", fontsize=12, labelpad = 10)
    plt.ylabel("item popularity", fontsize=12, labelpad = 10)
    plt.title(f"{dataset}", fontweight='bold', pad= 10)
    plt.plot(range(item_cnt), item_pop, color='blue')
    plt.savefig(f'./results/{dataset}.png', format='png', dpi=300, bbox_inches='tight')
print("All datasets processed, please check the 'results' folder")