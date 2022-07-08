import sqlite3
import time

import pandas as pd

if __name__ == '__main__':
    conn = sqlite3.connect('bsm.db')
    c = conn.cursor()
    chunksize = 10 ** 6
    start = time.time()
    with pd.read_csv('data/Wyoming_CV_Pilot_Basic_Safety_Message_One_Day_Sample.csv', chunksize=chunksize,
                     low_memory=False) as reader:
        for chunk in reader:
            chunk.to_sql('bsm', conn, if_exists='append', index=False)
    print("time :", time.time() - start)
    # time : 1117.6711807250977
    # C:\Users\sigma\works\practice-sql\bsm-and-cqrs\venv\Scripts\python.exe C:/Users/sigma/works/practice-sql/bsm-and-cqrs/use_db.py
    # time : 1117.6711807250977