import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

print("Loading dataset...")

# Load dataset
data = pd.read_csv("spam.csv")

print("Dataset loaded:")
print(data.head(), "\n")

# Encode labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

X = data['message']
y = data['label']

# Vectorization
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.25, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Test custom input
test_msg = ["Free offer win money"]
test_vec = vectorizer.transform(test_msg)
result = model.predict(test_vec)

print("\nTest Message:", test_msg[0])
print("Prediction:", "SPAM" if result[0] == 1 else "HAM")
