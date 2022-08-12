import pandas as pd

print("Hello world! :)")


titanic=pd.read_excel("proba.xlsx")

print(titanic.info())
#print(titanic.head(10))

ages = titanic["Age"]
age_sex = titanic[["Age", "Sex"]]
above_35 = titanic[titanic["Age"] > 35]
print(age_sex.shape)
#print(above_35["Age"])
print(titanic.iloc[9:25, 2:5])
print(titanic.iloc[0:,[2,5]])           #IDEMOOO TO MI TREBA

for i in range(9,25):
    for j in range(2,5):
        print(titanic.iloc[i,j])        #IDEMOOO TO MI TREBA

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

#df = pd.read_csv("C:\\Users\\Andrea\\Downloads\\dataset\\flight-dataset\\csv-data\\const2\\const2-trial1-tdoa2.csv")
#a = df.as_matrix()
#print(df.dtypes)
#print(df.get(['t_tdoa','idA']))

#print(df['t_tdoa'].iloc[0])
#print(df.to_numpy)
#print(df.ndim)