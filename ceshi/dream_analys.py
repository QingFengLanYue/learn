import pandas as pd

file='dream.csv'
col=['期数','date','red1','red2','red3','red4','red5','red6','blue']
#col=[0,1,2,3,4,5,6,7,8]
df=pd.read_csv(file,usecols=col)
print(df.shape)
print(df.columns)

print(df)
