import pandas as pd

data =[
 {"name":"Bhaskar","age":27,"city":"Kakinada"},
 {"name":"Tanuja","age":24,"city":"Vizag"},
 {"name":"Arnika","age":4,"city":"India"},
]

df = pd.DataFrame(data)
df.to_csv("data/data.csv",index=False)

