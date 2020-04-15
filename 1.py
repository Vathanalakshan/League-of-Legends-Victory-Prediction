import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('challenger.csv')

inputs = data.drop(['win','vilemaw_kills_team_1', 'vilemaw_kills_team_2'],axis='columns')
target = data["win"]

i_train,i_test,t_train,t_test=train_test_split(inputs[:100],target[:100],test_size=0.33)

DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)

print(DTree.score(i_test,t_test))
