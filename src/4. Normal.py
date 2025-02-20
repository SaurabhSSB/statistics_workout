import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/Credit_Rating.csv")
df.columns.to_list()
df.head()
df_new= df[[ "Income", "Credit_Limit"]].head()
df_new

sns.set(rc= {"figure.figsize": ( 11.7, 8.27)})
graph= sns.barplot(x= "Income",y= "Credit_Limit",data= df_new)
graph.set_xticklabels(graph.get_xticklabels(), rotation= 45, horizontalalignment= "right")
graph.set(xscale= "log")   
plt.tight_layout()
plt.show()
