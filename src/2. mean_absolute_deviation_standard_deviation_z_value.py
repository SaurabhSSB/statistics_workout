import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/medical_expenses.csv")
df.bmi.describe()
sns.histplot(df.bmi, kde= True,color= 'yellow')
plt.show()

mean= df.bmi.mean()
float(mean)

std_dev= df.bmi.std()
float(std_dev)

float(mean - 3 * std_dev)
float(mean + 3 * std_dev)

df[(df.bmi< 12.368836125949507) | (df.bmi> 48.95795759602359)]
df_new= df[(df.bmi>= 12.368836125949507) & (df.bmi<= 48.95795759602359)]
df_new.head()
df_new.shape

df["z_score"]= (df.bmi - df.bmi.mean())/df.bmi.std()
df.head()

df[(df.z_score>3) | (df.z_score<-3)]
df_outlier_removed= df[(df.z_score<3) & (df.z_score>-3)]
