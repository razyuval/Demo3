import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
titanic_df = pd.read_excel("titanic3.xls")
# print(titanic_df.head(10))
# print (titanic_df.describe())
# print (titanic_df.drop('ticket', axis=1))

# plt.show(pd.value_counts(titanic_df['survived']).plot.bar())

plt.show(pd.value_counts(titanic_df['survived'].loc[titanic_df['sex']=='female']).plot.bar())
