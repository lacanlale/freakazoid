#!/usr/bin/python
import pandas as pd
import numpy as np


def log():
    workouts = []
    print("+==========================================+")
    print("+  Enter Workout, leave empty if finished  +")
    print("+==========================================+")
    workout = input("Workout name: ").upper().replace(' ', '_').strip(), [input("Weight: ")]

    while workout[0] and workout[1]:
        workouts.append(workout)
        print("+==========================================+")
        print("+  Enter Workout, leave empty if finished  +")
        print("+==========================================+")
        workout = input("Workout name: ").upper().replace(' ', '_').strip(), [input("Weight: ")]

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