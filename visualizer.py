import pandas as pd
import numpy as np


def print_maxs(df=pd.read_csv('log.csv').drop(['DURATION', 'DATE'], axis=1)):
    for x in df:
        print("\033[1m+ {} MAX WEIGHT\033[0m: {} lbs".format(x.replace('_', ' '), max(df[x])))
    print()


def find_prevs(df, col_names):
    prev = {}
    df = df[col_names]
    for x in df:
        for y in reversed(df[x]):
            if(y > 0):
                prev[x] = y
                break
    return prev


def get_weight_progress(df):
    dec = '\033[01;31m-'
    inc = '\033[01;32m+'
    same = '\033[0;33m~'
    
    latest_row = df.iloc[[-1]]
    latest_index = len(df)-1
    latest = [x for x in latest_row if latest_row[x].at[latest_index]]
    print("===================")
    print("+ WEIGHT PROGRESS +")
    print("===================")

    prevs = find_prevs(df.drop(index=latest_index), latest)
    comparisons = {}
    for x in latest:
        latest_weight = latest_row[x].at[latest_index]
        comparisons[x] = "{} lbs ".format(latest_weight)
        if latest_weight > prevs[x]:
            comparisons[x] += "({}{})".format(inc, latest_weight-prevs[x])
        elif latest_weight < prevs[x]:
            comparisons[x] += "({}{})".format(dec, prevs[x]-latest_weight)
        else:
            comparisons[x] += "({})".format(same)
    
    for x, y in comparisons:
        print("+ {}: {}".format(x, y))


def get_progress(df):
    time = df['DURATION']
    time = round(np.mean([int(x[:x.index(':')]) * 60 + int(x[x.index(':')+1:]) for x in time]), 2)
    print("======================")
    print("+ DURATION PROGRESS  +")
    print("======================") 
    print("+ Average workout time: {} h, {} min".format(round(time/60+0.5), round(time%60+0.5)))
    print("+ Longest workout time (HH:MM): {}".format(max(df['DURATION'])))
    get_weight_progress(df.drop(columns=['DURATION', 'DATE']))

def visualize(df):
    get_progress(df)
    print_maxs(df.drop(columns=['DURATION', 'DATE']))