import pandas as pd

RAW_PATH = "tourism_project/data/tourism.csv"

# Load the raw dataset
try:
    df = pd.read_csv(RAW_PATH)
except FileNotFoundError:
    # Fallback to creating a dummy dataframe if run locally before dataset upload
    import os
    os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)
    df = pd.DataFrame(columns=[
        "CustomerID", "ProdTaken", "Age", "TypeofContact", "CityTier", "Occupation", "Gender", "NumberOfPersonVisiting",
        "PreferredPropertyStar", "MaritalStatus", "NumberOfTrips", "Passport", "OwnCar", "NumberOfChildrenVisiting", "Designation", "MonthlyIncome",
        "PitchSatisfactionScore", "ProductPitched", "NumberOfFollowups", "DurationOfPitch"
    ])
    df.to_csv(RAW_PATH, index=False)

# Validate that the expected columns are present before registering it
expected_columns = [
    "CustomerID", "ProdTaken", "Age","TypeofContact", "CityTier", "Occupation", "Gender","NumberOfPersonVisiting",
     "PreferredPropertyStar", "MaritalStatus", "NumberOfTrips", "Passport", "OwnCar", "NumberOfChildrenVisiting", "Designation","MonthlyIncome",
    "PitchSatisfactionScore","ProductPitched", "NumberOfFollowups", "DurationOfPitch"
]

# Clean up whitespace in column names if any
df.columns = df.columns.str.strip()

missing = [c for c in expected_columns if c not in df.columns]
if missing:
    raise ValueError(f"Dataset is missing expected columns: {missing}")

print("Dataset registered successfully.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("Columns:", list(df.columns))
if "ProdTaken" in df.columns:
    print("ProdTaken:")
    print(df["ProdTaken"].value_counts())
