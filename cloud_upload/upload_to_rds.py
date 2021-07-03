# %%
from sqlalchemy import create_engine 
import pandas as pd

#%%
# Setting up the DB
user = 'postgres'
password = 'postgres'
hostname = 'plants-db-instance.cp7nhwi8jhqz.us-east-2.rds.amazonaws.com'
port = '5432'
db_name = 'postgres'
db_string = f"postgresql://{user}:{password}@{hostname}:{port}/{db_name}"

#%%
# Create engine
db = create_engine(db_string)

#%%
# Open csv file
with open('cleaned_test_database.csv') as f:
    df = pd.read_csv(f)

#%%
# Insert data to db
df.to_sql('plant_database', db)
