import pandas as pd
import numpy as np
df= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/cc_charge.csv")
df.head()
df.describe()
df.info()
float(df.HH_Size.quantile(0.75))
float(df.HH_Size.quantile(0.75, interpolation= 'lower'))
float(df.HH_Size.quantile(0.75, interpolation= 'higher'))

percentile_90= float(df.HH_Size.quantile(0.90))
df_outlier= df[df.HH_Size> percentile_90]
df_no_outlier= df[df.HH_Size<= percentile_90]

df.head()
df_outlier.head()
df_no_outlier.head()

df['HH_Size'][21]= np.nan
df.loc[22, 'HH_Size'] = np.nan
df.iloc[21]
df.iloc[22]

float(df.HH_Size.mean())
float(df.HH_Size.median())
df_new= df.fillna(df.HH_Size.median())
df_new.iloc[[21,22]]
