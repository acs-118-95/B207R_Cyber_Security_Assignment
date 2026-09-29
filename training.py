import pandas
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Loading the dataset and checking the first five rows.
data = pandas.read_csv("data/emails.csv")
print(data.head())

# Removing rows with missing values and duplicates in Email Text
data = data.dropna(subset=["Email Text"])

data = data.drop_duplicates(subset=["Email Text"])

print(f"\nNumber of rows after removal of missing values and duplicates: {data.shape}")

# First five rows of Email Text and Email Type after cleaning
email_text = data["Email Text"]
email_type = data["Email Type"]
print("\nFirst five rows of Email Text and Email Type after cleaning:")
print(email_text.head())
print(email_type.head())

# Converting Email Type into numbers
email_label = email_type.map({"Safe Email": 0, "Phishing Email": 1})
print("\nFirst five rows of Email Type after changing values into numbers:")
print(email_label.head())

# Splitting the dataset into training and testing sets
train_text, test_text, train_label, test_label = train_test_split(
    email_text, email_label, test_size=0.2, random_state=42)
print(f"\nSize of training text: {train_text.shape}")
print(f"\nSize of testing text: {test_text.shape}")

# Converting Email Text to numerical values using TF-IDF vectorization
converter = TfidfVectorizer()
tr_text_conv = converter.fit_transform(train_text)
te_text_conv = converter.transform(test_text)
print(f"\nShape of training data after TF-IDF: {tr_text_conv.shape}")
print(f"\nShape of testing data after TF-IDF: {te_text_conv.shape}")

# Training the Logistic Regression model
model = LogisticRegression()
model.fit(tr_text_conv, train_label)

# Checking the prediction
prdct_label = model.predict(te_text_conv)

# Comparing predicted label to actual label
print(f"\nFirst five predicted labels: {prdct_label [:5]}")
print(f"\nFirst five actual labels: \n{test_label.head()}")