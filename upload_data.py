
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://abdurrab:abdurrab@cluster0.iqwfe29.mongodb.net/?appName=Cluster0"

# create new client and connect to server
client = MongoClient(uri)

# create a database name and collection name
DATABASE_NAME = 'abdurrabkhan'
COLLECTION_NAME = 'wafer-fault'

df = pd.read_csv("/content/wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)


json_record = list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

