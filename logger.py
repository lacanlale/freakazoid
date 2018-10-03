#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import ceil


def display_time():
    df = pd.read_csv('log.csv')
    time = df['DURATION']
    dates = df['DATE']
    time = [int(x[:x.index(':')]) * 60 + int(x[x.index(':')+1:]) for x in time]

    plt.figure()
    plt.title("Workout duration over time")
    plt.plot(np.arange(1,len(df)+1), time, label='Time')
    plt.xlabel("Workout day")
    plt.ylabel("Time (minutes)")
    plt.xticks(np.arange(len(dates)), dates)
    plt.legend()
    plt.show()
    print("+====================+")
    print("+  Average Duration  +")
    print("+====================+")
    print("{} Minutes".format(np.mean(round(time,2))))
    print("{} Hours || {} Minutes".format(ceil(np.mean(round(time,2))/60), ceil(np.mean(round(time,2)%60))))


def display_weights():
    df = pd.read_csv('log.csv')
    print("+=======================+")
    print("+  Workout Progression  +")
    print("+=======================+")
    dates = df['DATE']
    df.drop(['DATE', 'DURATION'], axis=1, inplace=True)
    count = 1
    plt.figure(figsize=(10,8))
    plt.title("WEIGHT OVER TIME")
    for col in df.columns:
        weights = df[col][df[col] != 0]
        plt.plot(np.arange(len(weights)), weights, label=col, markersize=25)
        count += 1
    plt.xlabel("DATES (MM/DD/YYYY)")
    plt.ylabel("WEIGHT (lb)")
    plt.legend(fontsize=15)
    plt.xticks(np.arange(len(dates)), dates)
    plt.show()


def log():
    workouts = []
    print("+==========================================+")
    print("+  Enter Workout, leave empty if finished  +")
    print("+==========================================+")
    workout = input("Workout name: ").upper().replace(' ', '_'), [input("Weight: ")]

    while workout[0] and workout[1]:
        workouts.append(workout)
        print("+==========================================+")
        print("+  Enter Workout, leave empty if finished  +")
        print("+==========================================+")
        workout = input("Workout name: ").upper().replace(' ', '_'), [input("Weight: ")]

    work_dict = dict((x, y) for x, y in workouts)
    print("+==========================+")
    work_dict['DATE'] = input("+  Date MM/DD/YYYY: ")
    print("+==========================+\n")
    print("+================================+")
    work_dict['DURATION'] = input("+  Length of workout HH:MM: ")
    print("+================================+")

    try:
        df_base = pd.read_csv("log.csv")
    except FileNotFoundError:
        df_base = pd.DataFrame(work_dict) 
        df_base.to_csv("log.csv", index=False)
        return df_base

    df_new = pd.DataFrame(work_dict)
    df_base = pd.concat([df_base, df_new], axis=0, sort=True)
    df_base.fillna(0, inplace=True)
    df_base.to_csv("log.csv", index=False)
    return df_base


def display():
    display_weights()
    display_time()
    

def main():
    intro = "|~~|~~\|~~  /\  | /  /\  ~~//~~\~|~|~~\ \n|--|__/|-- /__\ |(  /__\  /|    || |   | \n|  |  \|__/    \| \/    \/__\__/_|_|__/ "
    print(intro)
    log()
    print("+=======================+")
    print("+  DISPLAYING PROGRESS  +")
    print("+=======================+")
    display()


if __name__ == '__main__':
    main()