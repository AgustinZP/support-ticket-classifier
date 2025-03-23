import pandas as pd
import nltk
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words_es = stopwords.words('spanish')

df = pd.read_csv('data/tickets.csv')

# Split dataset with traning and test
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['category'], test_size=0.2, random_state=42)

# Model Pipeline
model = make_pipeline(
    TfidfVectorizer(stop_words=stop_words_es),
    MultinomialNB()
)

# Training
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/ticket_model.pkl')
print("Modelo entrenado y guardado.")

# Save data for test
joblib.dump((X_test, y_test), 'model/test_data.pkl')
print("Dataset de prueba guardado.")