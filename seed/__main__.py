import os, glob
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine


conn_string = "postgresql://postgres:postgres@db:5432/theraconsultingcesar"
db = create_engine(conn_string)
conn = db.connect()

folders = glob.glob(os.path.dirname(__file__) + "/*")
for folder in folders:
    if Path(folder).is_dir() and folder.split('/')[-1] != "__pycache__":
        df = pd.read_csv(f"{folder}/data.csv")
        df.to_sql(folder.split('/')[-1], con=conn, if_exists='replace', index=False)

        print(folder.split('/')[-1])

conn.close()
print("See data loaded successfully!")
