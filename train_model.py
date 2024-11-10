import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load your data
data = pd.read_csv('data.csv')  # Replace with your actual data file

# Preprocess data
X = data.drop(['label'], axis=1)  # Drop the target label column
y = data['label']  # Target variable

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'model.pkl')
print("Model training complete and saved as 'model.pkl'.")
