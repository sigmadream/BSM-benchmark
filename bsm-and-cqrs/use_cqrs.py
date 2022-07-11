import hashlib
import sqlite3
import time

import pandas as pd


def hash_unicode(a_string):
    return hashlib.sha512(str(a_string).encode('utf-8')).hexdigest()


if __name__ == '__main__':
    salt = '12345'
    conn = sqlite3.connect('bsm.db')
    c = conn.cursor()
    chunksize = 10 ** 6
    start = time.time()
    with pd.read_csv('data/Wyoming_CV_Pilot_Basic_Safety_Message_One_Day_Sample.csv', chunksize=chunksize,
                     low_memory=False) as reader:
        for chunk in reader:
            chunk['metadata_securityResultCode'].apply(hash_unicode)
            chunk.to_sql('bsm', conn, if_exists='append', index=False)
    print("time :", time.time() - start)
    # time : 1141.6928420066833

