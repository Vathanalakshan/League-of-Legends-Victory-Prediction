import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('challenger.csv')

inputs = data.drop(data.columns[0:19],axis='columns')
target = data["win"]

i_train,i_test,t_train,t_test=train_test_split(inputs[:100],target[:100],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("100")
print(DTree.score(i_test,t_test))

i_train,i_test,t_train,t_test=train_test_split(inputs[:200],target[:200],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("200")
print(DTree.score(i_test,t_test))

i_train,i_test,t_train,t_test=train_test_split(inputs[:300],target[:300],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("300")
print(DTree.score(i_test,t_test))

i_train,i_test,t_train,t_test=train_test_split(inputs[:400],target[:400],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("400")
print(DTree.score(i_test,t_test))

i_train,i_test,t_train,t_test=train_test_split(inputs[:500],target[:500],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("500")
print(DTree.score(i_test,t_test))

i_train,i_test,t_train,t_test=train_test_split(inputs[:600],target[:600],test_size=0.2)
DTree= DecisionTreeClassifier()
DTree.fit(i_train,t_train)
print("600")
print(DTree.score(i_test,t_test))