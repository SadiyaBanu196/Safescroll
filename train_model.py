import pandas as pd 
import pickle 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, classification_report 

# Load dataset 
df = pd.read_csv("dataset.csv")

# Show label counts 
print(df["label"].value_counts()) 

# Features and labels 
X = df["text"] 
y = df["label"] 

# Convert text into vectors 
vectorizer = TfidfVectorizer(stop_words="english") 
X_vectorized = vectorizer.fit_transform(X) 

# Split dataset 
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42 
)
 
# Train model 
model = LogisticRegression(max_iter=1000) 
model.fit(X_train, y_train)

# Predictions 
y_pred = model.predict(X_test) 

# Accuracy 
accuracy = accuracy_score(y_test, y_pred) 
print("\nAccuracy:", accuracy) 
print("\nClassification Report:\n") 
print(classification_report(y_test, y_pred)) 

# Save model 
pickle.dump(model, open("model.pkl", "wb")) 

# Save vectorizer 
pickle.dump(vectorizer, open("vectorizer.pkl", "wb")) 
print("\nModel and vectorizer saved successfully.")