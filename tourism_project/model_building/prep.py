import pandas as pd
from sklearn.model_selection import train_test_split

df1 = pd.read_csv("tourism_project/data/tourism.csv")
# dropping the Customer ID column
df1.drop(columns=["CustomerID"], inplace=True)

#check for missing values
missing= df1.isnull().sum()
print(missing)
# print categorical columns
categorical_columns = df1.select_dtypes(
    include=["object", "category", "string"]
).columns.tolist()

numerical_columns = df1.select_dtypes(
    include=["number"]
).columns.tolist()

print(categorical_columns)
print(numerical_columns)


# let us treat Gender and marital status seems to have Typo
# replacing the Fe male with Female
#replacing the Single with Unmarried
#Data Cleaning

df1['Gender'] = df1['Gender'].replace('Fe Male', 'Female')
df1['MaritalStatus'] = df1['MaritalStatus'].replace('Single', 'Unmarried')
print( df1.describe())

X = df1.drop(columns=["ProdTaken"])
y = df1["ProdTaken"]

# stratify=y keeps the (imbalanced) failure ratio consistent across splits
Xtrain, Xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)



# Save datasets
Xtrain.to_csv("Xtrain.csv", index=False)
Xtest.to_csv("Xtest.csv", index=False)
ytrain.to_csv("ytrain.csv", index=False)
ytest.to_csv("ytest.csv", index=False)

print("Data preparation completed.")
print("Training samples:", len(Xtrain))
print("Testing samples:", len(Xtest))

print("Data prepared: train/test splits written.")
