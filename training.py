import pandas

# Loading the dataset and checking the first five rows.
data = pandas.read_csv("data/emails.csv")
print(data.head())

# Removing rows with missing values and duplicates in Email Text
data = data.dropna(subset=["Email Text"])

data = data.drop_duplicates(subset=["Email Text"])

print("\nNumber of rows after removal of missing values and duplicates:")
print(data.shape)

# First five rows of Email Text and Email Type after cleaning
print("\nFirst five rows of Email Text and Email Type after cleaning:")
print(data[["Email Text", "Email Type"]].head())
