import pandas as pd
import numpy as np
df= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/Prestige.csv")
df.head()
df.tail()
df.shape
df.info()
df.isnull().sum()
df.duplicated().sum(),"duplicated rows"
df.dtypes
df.income.describe()

df_income_mean= df.income.mean()
df_income_std= df.income.std()
pos_3_std= df_income_mean + 3 * df_income_std
neg_3_std= df_income_mean - 3 * df_income_std

df_new= df[(df.income<= pos_3_std) & (df.income>= neg_3_std)] # Since income is alway +ve can skip neg_3_std
df_new.income.describe()

_,mean_income,std_income,*_= df.income.describe()
mean_income, std_income
def z_value(variable, mean, std):
  return (variable- mean)/std


df["z_score"]= df["income"].apply(lambda x: z_value(x, mean_income, std_income))
df.head()    
df_new_2= df[(df.z_score<3) & (df.z_score> -3)]  # Since income is alway +ve can skip -3 
df_new_2.income.describe()

# Modified Z-score
def get_median_absolute_deviation(x):
  median= np.median(x)
  abs_diff= abs(x-median)
  mad= np.median(abs_diff)
  return mad
mad= get_median_absolute_deviation(df.income)
median= np.median(df.income)
float(mad), float(median)

def modified_z_score(x, median, mad):
  return 0.6745 * (x - median)/mad

df["mod_z_score"]= df.income.apply(lambda x: modified_z_score( x, median, mad))
df_new_3= df[df.mod_z_score> 3.5]
