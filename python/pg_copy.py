import io
import time
import pandas as pd
from sqlalchemy import create_engine
from keys import *
# import tracemalloc

if __name__ == '__main__':
    # tracemalloc.start()
    engine = create_engine(PG_CONN)
    conn = engine.connect()
    cur = conn.connection.cursor()
    store = io.BytesIO()
    then = time.time()
    cur.copy_expert("COPY (select * from lineitem_s10) TO STDOUT WITH CSV HEADER;", store)
    print("finish copy", time.time() - then)
    store.seek(0)
    df = pd.read_csv(store)
    print("finish read_csv", time.time() - then)
    conn.close()
    print(df)
    # _, peak = tracemalloc.get_traced_memory()
    # print(f"memory peak: {peak/10**9:.2f}G")


