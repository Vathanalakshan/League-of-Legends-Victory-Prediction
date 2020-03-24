import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('challenger.csv')
Label = data['win']#La listes des wins
data.drop(data.columns[0:19], axis=1, inplace=True)#La liste des donnees qu'on va utlisee
#ax = Label.plot.hist(bins=5) #Repartition des victoires
data['damege_taken_20m_top_team_1'].plot.kde(c='red')
data['damege_taken_20m_top_team_2'].plot.kde(c='blue')

plt.show()
