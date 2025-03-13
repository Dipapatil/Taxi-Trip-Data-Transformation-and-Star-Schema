# import pandas as pd
#
# df = pd.read_parquet("yellow_tripdata_2024-12.parquet")
#
# df.to_csv("trip_data.csv",index=False)
df =pd.read_csv("trip_data.csv")
df.head()