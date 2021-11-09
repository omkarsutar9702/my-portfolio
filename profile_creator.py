#import libraries
import random
import pandas as pd
import numpy as np
import plotly.express as px

#create the dataset
data={"ticker" :["ashoka" , "bepl" , "central bank","coilindia" ,"goldbee" , "ioc" ,"kgdeim" ,"nifttybee" , "tatamotors"]
,"Amount" :[10,2,15,5,7,9,4,5,3],
"avg_value":[533 , 348 , 389 , 297 , 245 , 546 , 689 , 544 , 786 ]}

#convert into dataframe
df = pd.DataFrame(data)
size = df["Amount"]*df['avg_value']
df["size"] = size

#get the total investment
portfolio_size = sum(df["Amount"]*df["avg_value"])
portfolio_size

#create the pie chart
fig = px.pie(df , values=size , names=ticker , title="my portfolio")
fig.show()
