import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

data=pd.read_csv('specific-challenger')
data.drop_duplicates()

kill=["kills_bottom_duo_carry_team_2","kills_bottom_duo_carry_team_1","kills_top_team_1","kills_top_team_2","kills_middle_team_1","kills_middle_team_2",]
for i, row in data.iterrows():
    for j in kill:
        if (row[j] > 40):
            print(i)
            break

print(data)

for i in data:
    sns.lmplot(i, hue="win", height=3)
    plt.show()

"""
inputs = data.drop(data.columns[0:19],axis='columns')
target = data["win"]

i_train,i_test,t_train,t_test=train_test_split(inputs[:100],target[:100],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("100")
print(DTree.score(i_test,t_test))


"""