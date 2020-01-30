import matplotlib.pyplot as plt  
import seaborn as sns
import pandas as pd

df_iris = pd.read_csv('iris.csv')  
 
# corrmat = df_iris[df_iris.columns[:4]].corr()

sns.set(style="ticks")    # 使用默认配色  
sns.pairplot(df_iris,hue="species")   # hue 选择分类列  

plt.show()  