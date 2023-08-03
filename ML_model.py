import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore",
                        message="X does not have valid feature names, but RandomForestClassifier was fitted with "
                                "feature names")

# Specify the path to the CSV data file
data = "/Users/daddy/Downloads/loan_approval_dataset.csv"

# Define column names for the DataFrame
names = ["Loan ID", "# of dependants", "education", "self employed", "annual income", "loan amount", "loan term",
         "credit score", "residental assets", "commercial assets", "luxury assets", "bank assets", "loan status"]

# Read the CSV data into a DataFrame 'df' using the specified column names
df = pd.read_csv(data, names=names)

# Convert specific columns to numeric data types
numeric_columns = ["annual income", "loan amount", "loan term", "credit score", "residental assets",
                   "commercial assets", "luxury assets", "bank assets"]

# Apply 'pd.to_numeric' to convert the values in the specified columns to numeric data type
# If there are any errors during conversion, they will be coerced to 'NaN'
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Convert the "loan status" column to binary values (0 or 1)
# Map " Approved" to 1 and " Rejected" to 0
df["loan status"] = df["loan status"].map({" Approved": 1, " Rejected": 0})

# One-hot encode the "education" and "self employed" columns to convert them into binary representations
# Drop the first column of each one-hot encoded feature to avoid multicollinearity
df = pd.get_dummies(df, columns=["education", "self employed"], drop_first=True)

# Split the dataset into features (X) and target (y)
# 'X' will contain the features (columns) used for prediction, and 'y' will contain the target variable to be predicted.
X = df[numeric_columns]  # Extract the columns specified in 'numeric_columns' from the DataFrame 'df' to create 'X'.
y = df["loan status"]    # Extract the "loan status" column from the DataFrame 'df' to create 'y'.

# Split the dataset into training and test sets
# The train_test_split() function splits the data into random train and test subsets.
# The test_size=0.7 parameter specifies that 70% of the data will be used for testing, and 30% for training.
# The random_state=42 parameter sets a seed for reproducibility of the split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# Initialize and fit the Random Forest classifier
# RandomForestClassifier is a class for building random forest models.
# random_state=42 sets a seed for reproducibility of the model training.
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)  # Fit the random forest classifier using the training data (X_train and y_train).

# Get the accuracy score of the trained model on the test data
# The 'score()' method of the classifier returns the mean accuracy on the given test data and labels.
accuracy = rf_classifier.score(X_test, y_test)  # Calculate the accuracy of the model on the test data.

# Predict the loan approval for the test set
y_pred = rf_classifier.predict(X_test)

# Calculate and print the classification report, which includes precision, recall, and F1-score.
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Calculate the ROC-AUC score, which measures the area under the Receiver Operating Characteristic (ROC) curve.
roc_auc = roc_auc_score(y_test, y_pred)
print("ROC-AUC Score:", roc_auc)

print("Model Accuracy:", accuracy)  # Print the accuracy of the model on the test data.


correlation_matrix = df.corr()

# Plot the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
# plt.show()

# Box plots for numerical features
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[numeric_columns], orient="h", palette="coolwarm")
plt.title("Box Plots: Numerical Features")
plt.xlabel("Feature Values")
# plt.show()

# plot the scatter plot
sns.scatterplot(x='credit score', y='loan term', hue='loan status', data=df)

# plt.show()


# Function to predict loan approval
def predict_loan_approval(annual_income, loan_amount, loan_term, credit_score, residental_assets,
                          commercial_assets, luxury_assets, bank_assets):
    loan_data = np.array([[annual_income, loan_amount, loan_term, credit_score, residental_assets,
                           commercial_assets, luxury_assets, bank_assets]])
    prediction = rf_classifier.predict(loan_data)
    return "Approved" if prediction[0] == 1 else "Rejected"
