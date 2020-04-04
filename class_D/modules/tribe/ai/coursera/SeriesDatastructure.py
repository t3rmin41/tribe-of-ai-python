import pandas as pd
import numpy as np

animals = ["Tiger", "Bear", "Moose"]

#print(pd.Series(animals))

animals = ["Tiger", "Bear", None]
#print(animals[:]) # ":" means "from the first element to the last"

#print(pd.Series(animals))

#Querying a Series

sports = {"Archery": "Bhutan", "Golf": "Scotland", "Sumo": "Japan", "Taekwondo": "South Korea"}

s = pd.Series(sports)


#print(s.iloc[3])
#print(s.loc["Golf"])
#print(s[3])

s = pd.Series([100.0, 120, 101])
#print(s)

total = np.sum(s)
#print(total)

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ["Store 1", "Store 1", "Store 2"])
#print(df.head())

#print(df.loc[:]["Item Purchased"])
#print(df["Item Purchased"])
print(df.T) # Transpose matrix

df["Cost"] = df["Cost"] - df["Cost"]*0.2
print(df)