import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a= pd.read_csv("C:/Users/Hp/Desktop/Study ITM/Semester 2/Applied Machine Learning/Datasets/Travel_Time.csv")
a.columns
a.info()
a.head()
a.Population.describe()
type(a)
a.isna().sum()
a.loc[a.Highway_Type.isna(), "Highway_Type"]= "None"
a.head()

plt.subplots_adjust(bottom=0.3)  # Increase bottom margin
a["Highway_Type"].value_counts().plot(kind="bar")
plt.xlabel("Highway Type")
plt.ylabel("Count")
plt.title("Frequency of Highway Types")
plt.xticks(rotation=0)
plt.show()

df= a.head(6)
df.plot(x="Highway_Type", y="Population",kind= "bar")
plt.xticks(rotation= 0)
plt.subplots_adjust(bottom= 0.3)
plt.tight_layout()
plt.show()
df.at[0, "Highway_Type"] = "NH_A"
df.at[1, "Highway_Type"] = "NH_B"
df.at[2, "Highway_Type"] = "NH_C"
df.at[3, "Highway_Type"] = "NH_D"
df.at[4, "Highway_Type"] = "NH_E"
df.at[5, "Highway_Type"] = "NH_F"
df.head()
df.plot(x="Highway_Type", y="Population",kind= "bar",color= "orange")
plt.title("Highway_Population")
plt.xlabel("Highway")
plt.ylabel("Population")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation= 0)
plt.tight_layout()
plt.show()

df.plot(x="Highway_Type", y="Population",kind= "bar",color= "orange", logy= True)
plt.tight_layout()
plt.show()
