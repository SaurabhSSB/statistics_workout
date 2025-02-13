import pandas as pd
df= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/cc_charge.csv")
df.head()
df.describe()
float(df.HH_Size.quantile(0.75))
float(df.HH_Size.quantile(0.75, interpolation= 'lower'))
float(df.HH_Size.quantile(0.75, interpolation= 'higher'))

percentile_90= float(df.HH_Size.quantile(0.90))
df_outlier= df[df.HH_Size> percentile_90]
df_no_outlier= df[df.HH_Size<= percentile_90]

df.head()
df_outlier_removal.head()
df_no_outlier.head()
