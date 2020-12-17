import pandas as pd
import matplotlib.pyplot as plt
file='dream.csv'
col=['期数','date','red1','red2','red3','red4','red5','red6','blue']
#col=[0,1,2,3,4,5,6,7,8]
df=pd.read_csv(file,usecols=col)


red1=df['red1'].value_counts().sort_index()
red2=df['red2'].value_counts().sort_index()
red3=df['red3'].value_counts().sort_index()
red4=df['red4'].value_counts().sort_index()
red5=df['red5'].value_counts().sort_index()
red6=df['red6'].value_counts().sort_index()
blue=df['blue'].value_counts().sort_index()

#print(print(pd.merge(red1,red2)))
# print(red1)
# col1=pd.DataFrame(red1)
# col2=pd.DataFrame(red2)

n1=pd.concat([red1,red2,red3,red4,red5,red6], axis=1)
n2=n1.fillna(0)
n2["总和"] =n2.apply(lambda x:x.sum(),axis =1)
n3=pd.DataFrame(n2['总和'].values,columns=['nn'])
print(n3)
n3.plot(kind='bar')
n3.plot(kind='area')
n3.plot(kind='box')
n3.plot(kind='kde')
plt.show()

