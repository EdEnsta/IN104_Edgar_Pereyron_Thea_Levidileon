from numpy import *
import pandas as pd
import  pandas_profiling
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("train.csv")

print("Le fichier a " + str(df.shape[0]) + " lignes et " + str(df.shape[1]) + " colonnes",end='\n')
print()

#liste des données et leur type

print(df.dtypes, end='\n')
print()

#Analyse de la qualités des données
pandas_profiling.ProfileReport(df)
# pfr.to_file("C:/Users/perey/Desktop/example.html")

#Analyse des corrélations
cor = df.corr()
sns.heatmap(cor, cmap="coolwarm",linewidth=.5,annot=True)
plt.show()

#suppresion des colonnes non significative
df.drop(columns = ['PassengerId','Name','Ticket','Cabin'],inplace=True)




#stockage de la variable dans un array de numpy
cible = array(df['Survived'])

#suppresion de survived du dataset
df.drop('Survived',axis=1,inplace = True)

#conservation des noms des variables
liste_variables = list(df.columns)

#conversion du dataset en array
df = array(df)

#importation de l'algorithme
from sklearn.ensemble import RandomForestRegressor

#création d'un random forest de 100 arbres
rf = RandomForestRegressor(100,random_state = 2020)

#entraînement de l'algorithme
rf.fit(df,cible)