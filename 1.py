import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sklearn
import pandas as pd

data=pd.read_csv('challenger.csv')
data['win'].plot(kind='hist',bins=50,figsize=(12,6))
Label = data['win']#La listes des wins
data.drop(data.columns[0:19], axis=1, inplace=True)#La liste des donnees qu'on va utlisee
print(Label)
