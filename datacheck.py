import pandas

# Loading the dataset and checking the first five rows
data = pandas.read_csv("data/emails.csv")

print("First five rows:")
print(data.head())

# Checking the size of the dataset
print("\nNumber of rows and columns:")
print(data.shape)

# Checking the names of the columns
print("\nColumn names:")
print(data.columns)

# Checking for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Checking the number of safe and phishing emails
print("\nNumber of safe and phishing emails:")
print(data["Email Type"].value_counts())

# Checking the number of duplicate rows after removing missing values
dwo_miss = data.dropna(subset=["Email Text"])
print("\nNumber of duplicate rows:")
print(dwo_miss.duplicated(subset=["Email Text"]).sum())