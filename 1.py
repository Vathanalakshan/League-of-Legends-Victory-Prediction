import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()

data = pd.read_csv('challenger.csv')
print(data.shape)

data = data.drop_duplicates()

print(data.shape)
kill = ["kills_bottom_duo_support_team_2", "kills_bottom_duo_support_team_1", "kills_bottom_duo_carry_team_2",
        "kills_bottom_duo_carry_team_1", "kills_top_team_1", "kills_top_team_2", "kills_middle_team_1",
        "kills_middle_team_2", "kills_jungle_team_1", "kills_jungle_team_2"]
k = []
for i, row in data.iterrows():
    for j in kill:
        if (row[j] > 40):
            k.append(i)
            break

data = data.drop(k, axis=0)
print(data.shape)
kill1 = ["kills_top_team_1", "kills_jungle_team_1", "kills_middle_team_1", "kills_bottom_duo_carry_team_1",
         "kills_bottom_duo_support_team_1"]
kill2 = ["kills_top_team_2", "kills_jungle_team_2", "kills_middle_team_2", "kills_bottom_duo_carry_team_2",
         "kills_bottom_duo_support_team_2"]


def meanplotter(d, a):
    mean = {}
    for y in d:
        if y in a:
            mean[y] = (d[y].mean(axis=0))
    print(mean)

    keys=mean.keys()
    vals=mean.values()

    plt.bar(keys, np.divide(list(vals), sum(vals)), label="Real distribution")
    plt.tight_layout()

    plt.show()


meanplotter(data,kill1)

meanplotter(data,kill2)