from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import joblib
import re
import pandas as pd

# Load and preprocess your data
df = pd.read_csv('dataset/archive/sentimentdataset.csv', encoding='latin1')
df = df.dropna()
label_mapping = {'negative': 0, 'neutral': 1, 'positive': 2}
df['label'] = df['label'].map(label_mapping)

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = ''.join(char for char in text if ord(char) < 128)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = ' '.join(text.split())
    return text

df['comment'] = df['comment'].apply(clean_text)

# Define X and y
X = df['comment']
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline with GridSearchCV for hyperparameter tuning
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),  # Start with TfidfVectorizer
    ('classifier', MultinomialNB()),  # Start with MultinomialNB
])

# Define parameter grid for GridSearch
param_grid = [
    {
        'vectorizer': [TfidfVectorizer(), CountVectorizer()],
        'vectorizer__ngram_range': [(1, 1), (1, 2)],  # Unigrams and bigrams
        'classifier': [MultinomialNB()],
        'classifier__alpha': [0.1, 1.0, 10.0]  # For Naive Bayes
    },
    {
        'vectorizer': [TfidfVectorizer(), CountVectorizer()],
        'vectorizer__ngram_range': [(1, 1), (1, 2)],  # Unigrams and bigrams
        'classifier': [SVC()],
        'classifier__C': [0.1, 1, 10, 100],  # For SVM
        'classifier__kernel': ['linear', 'rbf'],  # SVM kernels
        'classifier__gamma': ['scale', 'auto']  # SVM gamma values
    }
]

# GridSearchCV to find the best parameters
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Get the best model and its accuracy
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Best Model: {best_model}')
print(f'Best Model Accuracy: {accuracy}')

# Save the best model
joblib.dump(best_model, 'improved_sentiment_detection_model.pkl')
